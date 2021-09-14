import sys # For sys.argv and sys.exit
import random # For randint
import uhal
import time
import Tkinter as tk
import GUI_getNode_functions as getNode_functions

def Connect(output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

    # PART 2: Creating the HwInterface
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

    TxValue = 1;
    output_textbox.insert(tk.END, "\n send SCA reset CMD!")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Rst_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    wait = 1
    time.sleep(wait) # wait 1 sec

    output_textbox.insert(tk.END, "\n send SCA connect CMD!")
    output_textbox.insert(tk.END, "\n************************************************")
    getNode_functions.SCA_Connect_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();

    return True
##############################################################################

def EnableGPIO(output_textbox, sentarg):
    
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);
    
    ###############################################################################
    # set GPIO Enable Register B
    ###############################################################################
    # write control register B
    TxValue = 0x02040001  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x02040001:
        return False

    TxValue = 0x04000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x04000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write control register D (Enable Serial Number reading)")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))

    if RxValue != 0x20001:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read control register D
    TxValue = 0x03040002  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x03040002:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read control register D (Enable Serial Number reading)")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x20002:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")

    if RxValue != 0x04000000:
        return False

    return True
##############################################################################

def EnableAtoD(output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    ###############################################################################
    # set Analog to Digital converter enable flag eFuses/Serial Number reading bit4
    ###############################################################################
    # write control register D
    TxValue = 0x06040001  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr. ID = " + (hex(TxValue)))
    if TxValue != 0x06040001:
        return False

    TxValue = 0x10000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x10000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write control register D (Enable Serial Number reading)")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x20001:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read control register D
    TxValue = 0x07040002  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x07040002:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read control register D (Enable Serial Number reading)")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x20002:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n *********************************************")

    return True
########################################################################

def Bread(Bread_label, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #------------------------------------------------------------------------------
    # read control register D
    TxValue = 0x03040002  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x03040002:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read control register D (Enable Serial Number reading)")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x20002:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    Bread_label.configure(text=hex(RxValue))
    output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n *************************************************")

    return True
##############################################################################

def DIRread(DIRread_label, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #------------------------------------------------------------------------------
    # read GPIO Direction Register
    TxValue = 0x21010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x21010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Direction")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    DIRread_label.configure(text=hex(RxValue))
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    return True
####################################################################

def DATAOUTread(DATAOUTread_label, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #--------------------------------------------------------------
    # read GPIO Direction Register
    TxValue = 0x11010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x11010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Direction")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    DATAOUTread_label.configure(text=hex(RxValue))
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")

    return True
#########################################################################

def IDread(IDread_label, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    ###############################################################################
    # Read SCA ID
    ###############################################################################
    # Read SCA ID register
    TxValue = 0xD1041403  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
#    output_textbox.delete("1.0", "50.100") #delete previous lines in textbox
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0xD1041403:
        return False

    TxValue = 0x00000001  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000001:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read SCA ID register")
    output_textbox.insert(tk.END, "\n ************************************************")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x41403:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Data = " + (hex(RxValue)))
    IDread_label.configure(text=hex(RxValue))
       
    output_textbox.insert(tk.END, "\n ")
    output_textbox.insert(tk.END, "\n SCA ID value = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n End!")
    output_textbox.insert(tk.END, "\n ************************************************")
    
    return True
########################################################################

def GPIOon(passedarg, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #------------------------------------------------------------------------
    # read GPIO Direction Register
    TxValue = 0x21010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x21010202:
        return False


    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Direction")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    if TxValue != 0x00000000:
        return False
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n passedarg = " + (hex(passedarg)))
    NewValue = RxValue | passedarg
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n txvalue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    ###############################################################################
    # set GPIO_W_Direction
    ###############################################################################
    # write DIRECTION register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2
    TxValue = 0x20040201  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x20040201:
        return False

#    TxValue = 0x00412080  # data field
#    TxValue = 0xffffffff  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(NewValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write Direction Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x201:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read GPIO Direction Register
    TxValue = 0x21010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x21010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Direction")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    if TxValue != 0x00000000:
        return False
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    if RxValue != NewValue:
        return False

    return True
#######################################################################

def GPIOset(passedarg, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #--------------------------------------------------------------
    # read GPIO Dataout Register
    TxValue = 0x11010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x11010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Dataout")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr. ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
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
    TxValue = 0x10040201  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x10040201:
        return False

#    TxValue = 0x00412080  # data field
#    TxValue = 0xffffffff  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(NewValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write Dataout Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x201:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read GPIO Dataout Register
    TxValue = 0x11010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x11010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Dataout")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Dataout Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    return True
######################################################################

def GPIOclr(passedarg, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #--------------------------------------------------------------
    # read GPIO Dataout Register
    TxValue = 0x11010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x11010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Dataout")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Dataout Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    NewValue = RxValue & ~passedarg
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n NewValue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    ###############################################################################
    # set GPIO_W_Dataout
    ###############################################################################
    # write Dataout register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2
    TxValue = 0x10040201  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x10040201:
        return False

#    TxValue = 0x00412080  # data field
#    TxValue = 0xffffffff  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(NewValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write Dataout Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x201:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read GPIO Dataout Register
    TxValue = 0x11010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x11010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Dataout")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Dataout Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    if RxValue != NewValue:
        return False

    return True
#####################################################################

def GPIOoff(passedarg, output_textbox, sentarg):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    #------------------------------------------------------------------------------
    # read GPIO Direction Register
    TxValue = 0x21010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x21010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Direction")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    NewValue = RxValue & ~passedarg
    output_textbox.insert(tk.END, "\n ************************************************")
    output_textbox.insert(tk.END, "\n txvalue = " + (hex(NewValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    
    ###############################################################################
    # set GPIO_W_Direction
    ###############################################################################
    # write DIRECTION register set gpio 10 and 19 to hit bot gbt-sca A and B on cc2
    TxValue = 0x20040201  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x20040201:
        return False

#    TxValue = 0x00412080  # data field
#    TxValue = 0xffffffff  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(NewValue)))

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Write Direction Register")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(NewValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x201:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response = " + (hex(RxValue)))

    #------------------------------------------------------------------------------
    # read GPIO Direction Register
    TxValue = 0x21010202  # CMD & LEN & CH & Tr.ID field
    getNode_functions.EC_Tx_SCA_Header(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write CMD & LEN & CH & Tr.ID = " + (hex(TxValue)))
    if TxValue != 0x21010202:
        return False

    TxValue = 0x00000000  # data field
    getNode_functions.EC_Tx_SCA_Data(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    output_textbox.insert(tk.END, "\n write Data = " + (hex(TxValue)))
    if TxValue != 0x00000000:
        return False

    output_textbox.insert(tk.END, "\n send SCA start CMD!")
    output_textbox.insert(tk.END, "\n Read GPIO Direction")
    getNode_functions.SCA_Start_CMD(sentarg, hw).write(int(TxValue)); 
    hw.dispatch();
    time.sleep(wait) # wait 1 sec
    
    # read SCA results from RxRAM
    RxValue = getNode_functions.EC_Rx_SCA_Header(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Response LEN & ERR & CH & Tr.ID = " + (hex(RxValue)))
    if RxValue != 0x40202:
        return False

    RxValue = getNode_functions.EC_Rx_SCA_Data(sentarg, hw).read();
    hw.dispatch();
    output_textbox.insert(tk.END, "\n Direction Register = " + (hex(RxValue)))
    output_textbox.insert(tk.END, "\n ************************************************")
    if RxValue != NewValue:
        return False

    return True
#######################################################################

def SCAADCread(output_textbox, sentarg, i):
    wait = .2
    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    wait = .05
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
