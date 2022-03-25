import sys # For sys.argv and sys.exit
import random # For randint
import uhal
import time
import Tkinter as tk
import GUI_getNode_functions as getNode_functions
from random import randrange


def Connect(output_textbox, sentarg):
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";
    
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);
    
    output_textbox.insert(tk.END, "\n************************************************")
    # Read SCA ID frame
    # SCA v2

    # set SCA address
    TxValue = 0x00000000  # Address field
    getNode_functions.EC_Tx_Elink_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write address = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    # Check if commening this works fine YM: 24-Mar-2022

    TxValue = 1;
    output_textbox.insert(tk.END, "\n send SCA reset CMD!")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Rst_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();

    wait = .005
    time.sleep(wait) # wait 1 sec

    output_textbox.insert(tk.END, "\n send SCA connect CMD!")
    output_textbox.insert(tk.END, "\n************************************************")
    getNode_functions.SCA_Connect_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();

    return True

##############################################################################
#
# This is the template code that communicates with GBT-SCA
#
##############################################################################
def ExecuteSCACommand(output_textbox, gbtsca_num, header, dataField, scaHeader):
    # reset the last RxValue to return
    RxLast = -1
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    # Send the SCA header 
    trID = randrange(10)
    TxValue = header | trID;
    ###print "1:", hex(trID), hex(TxValue)
    getNode_functions.EC_Tx_SCA_Header(gbtsca_num, hw).write(int(TxValue | trID)); 
    hw.dispatch();
    if output_textbox:
        output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr. ID = " + (hex(TxValue)))

    # Send the SCA data field
    getNode_functions.EC_Tx_SCA_Data(gbtsca_num, hw).write(int(dataField | trID));
    hw.dispatch();
    if output_textbox:
        output_textbox.insert(tk.END, "\n write Data = " + (hex(dataField)))
    
    # Execute transferred command
    if output_textbox:
        output_textbox.insert(tk.END, "\n send SCA start CMD!")
    getNode_functions.SCA_Start_CMD(gbtsca_num, hw).write(int(dataField));
    hw.dispatch();
    ###print "2:", hex(trID), hex(dataField)

    retrycount = 0    
    RxValue = 0
    while RxValue != (scaHeader | trID) and retrycount < 20:
        RxValue = getNode_functions.EC_Rx_SCA_Header(gbtsca_num, hw).read();
        hw.dispatch();
        retrycount += 1;

    ###print "3:", hex(scaHeader), hex(trID), hex(TxValue)

    if RxValue != (scaHeader | trID):
        if output_textbox:
            output_textbox.insert(tk.END, "\n error! ",  RxValue, ", trcount =", trID, " and retrycount = ", retrycount)
        return [False, RxValue];

    # Read out data
    RxValue = getNode_functions.EC_Rx_SCA_Data(gbtsca_num, hw).read(); 
    hw.dispatch();
    if output_textbox:
        output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))
    RxLast = RxValue;
    return [True, RxValue];


##############################################################################
def EnableGPIO(output_textbox, sentarg):

    # Register B
    if not ExecuteSCACommand(output_textbox, sentarg, 0x02040001, 0x04000000, 0x20001)[0]:
        return False;
    
    # Register D
    if not ExecuteSCACommand(output_textbox, sentarg, 0x03040002, 0x00000000, 0x20002)[0]:
        return False;

    return True

##############################################################################
def EnableAtoD(output_textbox, sentarg):
    
    if not ExecuteSCACommand(output_textbox, sentarg, 0x06040001, 0x10000000, 0x20001)[0]:
        return False;
    if not ExecuteSCACommand(output_textbox, sentarg, 0x07040002, 0x00000000, 0x20002)[0]:
        return False;

    return True

##############################################################################
def Bread(Bread_label, output_textbox, sentarg):

    # read control register D
    RxValue = -1
    output = ExecuteSCACommand(output_textbox, sentarg, 0x03040002, 0x0, 0x20002); 
    if not output[0]:
        return False;
    
    Bread_label.configure(text=hex(output[1]));
    return True

##############################################################################
def DIRread(DIRread_label, output_textbox, sentarg):

    # read GPIO Direction Register
    output = ExecuteSCACommand(output_textbox, sentarg, 0x21010202, 0x0, 0x40202);
    if output[0]:
        DIRread_label.configure(text=hex(output[1]))
        output_textbox.insert(tk.END, "\n Direction Register = " + (hex(output[1])))
        output_textbox.insert(tk.END, "\n ************************************************")
    else:
        return False
    
    return True

####################################################################
def DATAOUTread(DATAOUTread_label, output_textbox, sentarg):

    # read GPIO Direction Register
    output = ExecuteSCACommand(output_textbox, sentarg, 0x11010202, 0x0, 0x40202);
    if output[0]:
        DATAOUTread_label.configure(text=hex(output[1]))
        output_textbox.insert(tk.END, "\n DATAOUT Register = " + (hex(output[1])))
        output_textbox.insert(tk.END, "\n ************************************************")
    else:
        return False

    return True

#########################################################################
def IDread(IDread_label, output_textbox, sentarg):

    # Read SCA ID register
    output = ExecuteSCACommand(output_textbox, sentarg, 0xD1041403, 0x1, 0x41403);
    if output[0]:
        output_textbox.insert(tk.END, "\n Data = " + (hex(output[1])))
        IDread_label.configure(text=hex(output[1]))
    else:
        return False
    
    return True

########################################################################
def GPIOon(passedarg, output_textbox, sentarg):
    ###print "In GPIOon ", passedarg, sentarg

    # read GPIO Direction Register
    output = ExecuteSCACommand(output_textbox, sentarg, 0x21010202, 0x0, 0x40202);
    if not output[0]:
        return False
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(output[1])))
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n passedarg = " + passedarg)
    NewValue = output[1] | int(passedarg, 16);
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n txvalue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n ************************************************")

    # write DIRECTION register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2
    output = ExecuteSCACommand(output_textbox, sentarg, 0x20040201, NewValue, 0x201);
    if not output[0]:
        return False
    output_textbox.insert(tk.END, "\n Response " + (hex(output[1])));

    # read GPIO Direction Register
    if not ExecuteSCACommand(output_textbox, sentarg, 0x21010202, 0x0, 0x40202)[0]:
        return False

    ###print "GPIOon is successful"
    return True

#######################################################################
def GPIOset(passedarg, output_textbox, sentarg):

    # read GPIO Dataout Register
    output = ExecuteSCACommand(output_textbox, sentarg, 0x11010202, 0x0, 0x40202);
    if not output[0]:
        return False;
    RxValue = output[1]
    output_textbox.insert(tk.END, "\n Dataout Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n **************************************************")
    NewValue = RxValue | passedarg
    output_textbox.insert(tk.END, "\n **************************************************")
    output_textbox.insert(tk.END, "\n NewValue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n **************************************************")

    ###############################################################################
    # set GPIO_W_Dataout
    ###############################################################################
    # write Dataout register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2

    if not ExecuteSCACommand(output_textbox, sentarg, 0x10040201, NewValue, 0x201)[0]:
        return False

    if not ExecuteSCACommand(output_textbox, sentarg, 0x11010202, 0x0, 0x40202)[0]:
        return False

    return True

######################################################################
def GPIOclr(passedarg, output_textbox, sentarg):
    if type(passedarg) == type(1):
        passedarg = hex(passedarg)

    # read GPIO Dataout Register
    output = ExecuteSCACommand(output_textbox, sentarg, 0x11010202, 0x0, 0x40202);
    if not output[0]:
        return False;
    RxValue = output[1]
    output_textbox.insert(tk.END, "\n Dataout Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    NewValue = RxValue & int(passedarg, 16)
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n NewValue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    # set GPIO_W_Dataout
    # write Dataout register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2
    if not ExecuteSCACommand(output_textbox, sentarg, 0x10040201, NewValue, 0x201)[0]:
        return False

    if not ExecuteSCACommand(output_textbox, sentarg, 0x11010202, 0x0, 0x40202)[0]:
        return False

    return True

#####################################################################
def GPIOoff(passedarg, output_textbox, sentarg):
    ###print "Turning GPIO off", passedarg, sentarg
    if type(passedarg) == type(1):
        passedarg = hex(passedarg)

    # read GPIO Direction Register
    output = ExecuteSCACommand(output_textbox, sentarg, 0x21010202, 0x0, 0x40202);
    if not output[0]:
        return False;

    RxValue = output[1];
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    NewValue = RxValue & ~int(passedarg, 16)
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n txvalue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    # set GPIO_W_Direction
    # write DIRECTION register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2
    if not ExecuteSCACommand(output_textbox, sentarg, 0x20040201, NewValue, 0x201)[0]:
        return False;

    # read GPIO Direction Register
    if not ExecuteSCACommand(output_textbox, sentarg, 0x21010202, 0x0, 0x40202)[0]:
        return False

    ###print "GPIOoff is successful"
    return True

#######################################################################
def SCAADCread(output_textbox, sentarg, i):

    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    wait = .005
    # initialize IC and EC moduls
    TxValue = 1  
    getNode_functions.Init_EC_IC_moduls(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();

    # EOF register for SCA
    TxValue = 0 
    getNode_functions.nFRAME(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();

    ###############################################################################
    # set ADC_W_Curr
    ###############################################################################
    # write adc current register
    TxValue = 0x60041401  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))

    TxValue = 0x78480000  # data field
#    TxValue = 0x00000000  # data field
#    TxValue = 0xffffffff  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write ADC_CURR Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read adc curr Register
    TxValue = 0x61011402  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read ADC Curr Reg")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n ADC Curr Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")


    #for i in range(32):   ### From SCAADCreadB.py, needed to go through each adc register at once
    ###############################################################################
    # set ADC_W_mux
    ###############################################################################
    # write adc current register
    TxValue = 0x50041400 | (i+2) # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))

    TxValue = i  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write ADC_MUX Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
        
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read adc curr Register
    TxValue = 0x51011400 | (i+34)  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read ADC_MUX Reg")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
        
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n ADC MUX Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")

    ###############################################################################
    # start ADC_GO
    ###############################################################################
    # write adc current register
    TxValue = 0x02041400 | (i+64) # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))

    TxValue = 0x00000001  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write ADC_GO Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
        
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response ADC Value = " + (hex(RxValue)))              #Value needed for calculations
    output_textbox.insert(tk.END, "\n ************************************************")
    return RxValue

#################################
### Previous getNode Notation ###
#################################
#    Init_EC_IC_moduls   = hw.getNode("A2")

#    EC_Tx_Elink_Header  = hw.getNode("EC_Tx_Elink_Header")
#    EC_Tx_SCA_Header 	= hw.getNode("EC_Tx_SCA_Header")
#    EC_Tx_SCA_Data 	= hw.getNode("EC_Tx_SCA_Data")
#    SCA_Rst_CMD 	= hw.getNode("SCA_Rst_CMD")
#    SCA_Connect_CMD 	= hw.getNode("SCA_Connect_CMD")
#    SCA_Test_CMD 	= hw.getNode("SCA_Test_CMD")
#    SCA_Start_CMD 	= hw.getNode("SCA_Start_CMD")
#    nFRAME              = hw.getNode("nFRAME")

#    EC_Rx_Elink_Header = hw.getNode("ECTxElinkHRAM")
#    EC_Rx_SCA_Header = hw.getNode("EC_Rx_SCA_Header")
#    EC_Rx_SCA_Data = hw.getNode("EC_Rx_SCA_Data")
