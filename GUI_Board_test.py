import sys # For sys.argv and sys.exit
sys.path.append('/opt/rh/python210/root/usr/lib64/python2.10/lib-tk')
import Tkinter as tk
import ttk as ttk
import os
import tkFont as font
###imports for SCA###
import random # For randint
import uhal
import time
###import functions###
import GUI_button_functions as button_functions
import GUI_global as Gg

#######################################################################
### Initializing Global Variables for SCA Functions ###
#######################################################################
if __name__ == '__main__':

    # PART 1: Argument parsing
    #if not(len(sys.argv) == 1 or len(sys.argv) == 2):
    #    print "Incorrect usage!"
    #    print "usage: read_write_single_register.py only"
    #    sys.exit(1)
    #if len(sys.argv) == 2:
    #    print(hex(int(sys.argv[1], 16)))
 
    uhal.disableLogging()

    connectionFilePath = "GUI_Real_connections.xml";
    deviceId = "KCU105real";

       
    # PART 2: Creating the HwInterface
    connectionMgr = uhal.ConnectionManager("file://" + connectionFilePath);
    hw = connectionMgr.getDevice(deviceId);

    Init_EC_IC_moduls   = hw.getNode("A2")

    EC_Tx_Elink_Header  = hw.getNode("EC_Tx_Elink_Header")
    EC_Tx_SCA_Header 	= hw.getNode("EC_Tx_SCA_Header")
    EC_Tx_SCA_Data 	= hw.getNode("EC_Tx_SCA_Data")
    SCA_Rst_CMD 	= hw.getNode("SCA_Rst_CMD")
    SCA_Connect_CMD 	= hw.getNode("SCA_Connect_CMD")
    SCA_Test_CMD 	= hw.getNode("SCA_Test_CMD")
    SCA_Start_CMD 	= hw.getNode("SCA_Start_CMD")
    nFRAME              = hw.getNode("nFRAME")

    #EC_Rx_Elink_Header = hw.getNode("ECTxElinkHRAM")
    EC_Rx_SCA_Header = hw.getNode("EC_Rx_SCA_Header")
    EC_Rx_SCA_Data = hw.getNode("EC_Rx_SCA_Data")

    
    wait = .2
    # initialize IC and EC moduls
    TxValue = 1  
    Init_EC_IC_moduls.write(int(TxValue)); 
    hw.dispatch();

    # EOF register for SCA
    TxValue = 0 
    nFRAME.write(int(TxValue)); 
    hw.dispatch();

#######################################################################
### Setting up GUI Notebook, tabs, etc. ###
#######################################################################
#root = tk.Tk()

myfont = font.Font(size=12)
s = ttk.Style()
s.configure('TNotebook.Tab', font=('helvetica','12'))

main_notebook = ttk.Notebook(Gg.root, width=1440, height=900)
notebook = ttk.Notebook(main_notebook)
notebook2 = ttk.Notebook(main_notebook)
notebook3 = ttk.Notebook(main_notebook)
main_notebook.add(notebook, text='Debug')
main_notebook.add(notebook2, text='Data Taking')
main_notebook.add(notebook3, text='Commissioning')

### Debug subtabs ###
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)
tab8 = ttk.Frame(notebook)
#notebook.add(tab1, text='Beam Test')
notebook.add(tab8, text='GPIO')
notebook.add(tab3, text='Digital IO')
notebook.add(tab4, text='Analog IO')
notebook.add(tab5, text='Testboard IO')
notebook.add(tab6, text='PRBS')
notebook.add(tab7, text='Clock Freq')
notebook.add(tab2, text='Scripts')

### GPIO sub Frames ###
GBT_SCA4_GPIO_frame = ttk.Frame(tab8, borderwidth=2, relief="ridge")
GBT_SCA4_GPIO_frame.grid(column=0, row=0)
GBT_SCA1_GPIO_frame = ttk.Frame(tab8, borderwidth=2, relief="ridge")
GBT_SCA1_GPIO_frame.grid(column=1, row=0)
LpGBT1_GPIO_frame = ttk.Frame(tab8, borderwidth=2, relief="ridge")
LpGBT1_GPIO_frame.grid(column=2, row=0)
LpGBT2_GPIO_frame = ttk.Frame(tab8, borderwidth=2, relief="ridge")
LpGBT2_GPIO_frame.grid(column=3, row=0)

### Analog IO sub Frames ###
GBT_SCA4_AnIO_frame = ttk.Frame(tab4, borderwidth=2, relief="ridge")
GBT_SCA4_AnIO_frame.grid(column=0, row=0)
GBT_SCA1_AnIO_frame = ttk.Frame(tab4, borderwidth=2, relief="ridge")
GBT_SCA1_AnIO_frame.grid(column=1, row=0)
LpGBT1_AnIO_frame = ttk.Frame(tab4, borderwidth=2, relief="ridge")
LpGBT1_AnIO_frame.grid(column=0, row=1)
LpGBT2_AnIO_frame = ttk.Frame(tab4, borderwidth=2, relief="ridge")
LpGBT2_AnIO_frame.grid(column=1, row=1)

### Scripts sub Frames ###
GBT_SCA4_scripts_frame = ttk.Frame(tab2, borderwidth=2, relief="ridge")
GBT_SCA4_scripts_frame.grid(column=0, row=0)
GBT_SCA1_scripts_frame = ttk.Frame(tab2, borderwidth=2, relief="ridge")
GBT_SCA1_scripts_frame.grid(column=0, row=1)
LpGBT_version_frame = ttk.Frame(tab2, borderwidth=2, relief="ridge")
LpGBT_version_frame.grid(column=1, row=0)

#####################################################################
### GPIO tab buttons and configuration ###
#####################################################################
### IC4D GBT-SCA ###
####################
GBT_SCA4_label = tk.Label(GBT_SCA4_GPIO_frame, text='IC4D GBT-SCA')
GBT_SCA4_label.grid(column=0, row=0)
GBT_SCA4_label['font'] = myfont

GBT_SCA4_label_array = [
    tk.Label(GBT_SCA4_GPIO_frame, text='FE9 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='FE9 ALDO Enable1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='PCC B EN IV8 1') , tk.Label(GBT_SCA4_GPIO_frame, text='PCC B EN IV8 2'),
    tk.Label(GBT_SCA4_GPIO_frame, text='cSS B'), tk.Label(GBT_SCA4_GPIO_frame, text='FE10 ALDO Enable1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE10 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='cEN B'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE7 ALDO Enable1'), tk.Label(GBT_SCA4_GPIO_frame, text='FE7 ALDO Enable2'),
    tk.Label(GBT_SCA4_GPIO_frame, text='eSS B'), tk.Label(GBT_SCA4_GPIO_frame, text='FE3 ALDO Enable1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE5 ALDO Enable1'), tk.Label(GBT_SCA4_GPIO_frame, text='oEN B'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE6 ALDO Enable1'), tk.Label(GBT_SCA4_GPIO_frame, text='FE6 ALDO Enable2'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE12 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='FE3 ALDO Enable2'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE4 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='FE12 ALDO Enable1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='PCC A EN IV8 2'), tk.Label(GBT_SCA4_GPIO_frame, text='PCC A EN IV8 1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE11 ALDO Enable1'), tk.Label(GBT_SCA4_GPIO_frame, text='FE2 ALDO Enable1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE4 ALDO Enable1'), tk.Label(GBT_SCA4_GPIO_frame, text='FE11 ALDO Enable2'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE2 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='FE1 ALDO Enable1'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE5 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='FE1 ALDO Enable2'),
    tk.Label(GBT_SCA4_GPIO_frame, text='FE8 ALDO Enable1'), tk.Label(GBT_SCA4_GPIO_frame, text='FE8 ALDO Enable2')
]
for i in range(len(GBT_SCA4_label_array)):
    GBT_SCA4_label_array[i]['font'] = myfont
    if i < 16:
        GBT_SCA4_label_array[i].grid(column=0, row=i+1)
    else:
        GBT_SCA4_label_array[i].grid(column=3, row=i-15)

Gg.FE9_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable2_onoff4())
Gg.FE9_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable1_onoff4())
Gg.PCC_B_EN_IV8_1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_1_onoff4())
Gg.PCC_B_EN_IV8_2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_2_onoff4())
Gg.cSS_B_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.cSS_B_onoff4())
Gg.FE10_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable1_onoff4())
Gg.FE10_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable2_onoff4())
Gg.cEN_B_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.cEN_B_onoff4())
Gg.FE7_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable1_onoff4())
Gg.FE7_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable2_onoff4())
Gg.eSS_B_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.eSS_B_onoff4())
Gg.FE3_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable1_onoff4())
Gg.FE5_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable1_onoff4())
Gg.oEN_B_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.oEN_B_onoff4())
Gg.FE6_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable1_onoff4())
Gg.FE6_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable2_onoff4())
Gg.FE12_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable2_onoff4())
Gg.FE3_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable2_onoff4())
Gg.FE4_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable2_onoff4())
Gg.FE12_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable1_onoff4())
Gg.PCC_A_EN_IV8_2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_2_onoff4())
Gg.PCC_A_EN_IV8_1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_1_onoff4())
Gg.FE11_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable1_onoff4())
Gg.FE2_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable1_onoff4())
Gg.FE4_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable1_onoff4())
Gg.FE11_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable2_onoff4())
Gg.FE2_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable2_onoff4())
Gg.FE1_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable1_onoff4())
Gg.FE5_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable2_onoff4())
Gg.FE1_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable2_onoff4())
Gg.FE8_ALDO_En1_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable1_onoff4())
Gg.FE8_ALDO_En2_onoff_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable2_onoff4())

Gg.GBT_SCA4_button_array = [
    Gg.FE9_ALDO_En2_onoff_button4, Gg.FE9_ALDO_En1_onoff_button4, Gg.PCC_B_EN_IV8_1_onoff_button4, Gg.PCC_B_EN_IV8_2_onoff_button4,
    Gg.cSS_B_onoff_button4, Gg.FE10_ALDO_En1_onoff_button4, Gg.FE10_ALDO_En2_onoff_button4, Gg.cEN_B_onoff_button4,
    Gg.FE7_ALDO_En1_onoff_button4, Gg.FE7_ALDO_En2_onoff_button4, Gg.eSS_B_onoff_button4, Gg.FE3_ALDO_En1_onoff_button4,
    Gg.FE5_ALDO_En1_onoff_button4, Gg.oEN_B_onoff_button4, Gg.FE6_ALDO_En1_onoff_button4, Gg.FE6_ALDO_En2_onoff_button4,
    Gg.FE12_ALDO_En2_onoff_button4, Gg.FE3_ALDO_En2_onoff_button4, Gg.FE4_ALDO_En2_onoff_button4, Gg.FE12_ALDO_En1_onoff_button4,
    Gg.PCC_A_EN_IV8_2_onoff_button4, Gg.PCC_A_EN_IV8_1_onoff_button4, Gg.FE11_ALDO_En1_onoff_button4, Gg.FE2_ALDO_En1_onoff_button4,
    Gg.FE4_ALDO_En1_onoff_button4, Gg.FE11_ALDO_En2_onoff_button4, Gg.FE2_ALDO_En2_onoff_button4, Gg.FE1_ALDO_En1_onoff_button4,
    Gg.FE5_ALDO_En2_onoff_button4, Gg.FE1_ALDO_En2_onoff_button4, Gg.FE8_ALDO_En1_onoff_button4, Gg.FE8_ALDO_En2_onoff_button4
]
for i in range(len(Gg.GBT_SCA4_button_array)):
    Gg.GBT_SCA4_button_array[i]['font'] = myfont
    if i < 16:
        Gg.GBT_SCA4_button_array[i].grid(column=1, row=i+1)
    else:
        Gg.GBT_SCA4_button_array[i].grid(column=4, row=i-15)

Gg.FE9_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable2_setclr4())
Gg.FE9_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable1_setclr4())
Gg.PCC_B_EN_IV8_1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_1_setclr4())
Gg.PCC_B_EN_IV8_2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_2_setclr4())
Gg.cSS_B_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.cSS_B_setclr4())
Gg.FE10_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable1_setclr4())
Gg.FE10_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable2_setclr4())
Gg.cEN_B_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.cEN_B_setclr4())
Gg.FE7_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable1_setclr4())
Gg.FE7_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable2_setclr4())
Gg.eSS_B_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.eSS_B_setclr4())
Gg.FE3_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable1_setclr4())
Gg.FE5_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable1_setclr4())
Gg.oEN_B_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.oEN_B_setclr4())
Gg.FE6_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable1_setclr4())
Gg.FE6_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable2_setclr4())
Gg.FE12_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable2_setclr4())
Gg.FE3_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable2_setclr4())
Gg.FE4_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable2_setclr4())
Gg.FE12_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable1_setclr4())
Gg.PCC_A_EN_IV8_2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_2_setclr4())
Gg.PCC_A_EN_IV8_1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_1_setclr4())
Gg.FE11_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable1_setclr4())
Gg.FE2_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable1_setclr4())
Gg.FE4_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable1_setclr4())
Gg.FE11_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable2_setclr4())
Gg.FE2_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable2_setclr4())
Gg.FE1_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable1_setclr4())
Gg.FE5_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable2_setclr4())
Gg.FE1_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable2_setclr4())
Gg.FE8_ALDO_En1_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable1_setclr4())
Gg.FE8_ALDO_En2_setclr_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable2_setclr4())

Gg.GBT_SCA4_button_array2 = [
    Gg.FE9_ALDO_En2_setclr_button4, Gg.FE9_ALDO_En1_setclr_button4, Gg.PCC_B_EN_IV8_1_setclr_button4, Gg.PCC_B_EN_IV8_2_setclr_button4,
    Gg.cSS_B_setclr_button4, Gg.FE10_ALDO_En1_setclr_button4, Gg.FE10_ALDO_En2_setclr_button4, Gg.cEN_B_setclr_button4,
    Gg.FE7_ALDO_En1_setclr_button4, Gg.FE7_ALDO_En2_setclr_button4, Gg.eSS_B_setclr_button4, Gg.FE3_ALDO_En1_setclr_button4,
    Gg.FE5_ALDO_En1_setclr_button4, Gg.oEN_B_setclr_button4, Gg.FE6_ALDO_En1_setclr_button4, Gg.FE6_ALDO_En2_setclr_button4,
    Gg.FE12_ALDO_En2_setclr_button4, Gg.FE3_ALDO_En2_setclr_button4, Gg.FE4_ALDO_En2_setclr_button4, Gg.FE12_ALDO_En1_setclr_button4,
    Gg.PCC_A_EN_IV8_2_setclr_button4, Gg.PCC_A_EN_IV8_1_setclr_button4, Gg.FE11_ALDO_En1_setclr_button4, Gg.FE2_ALDO_En1_setclr_button4,
    Gg.FE4_ALDO_En1_setclr_button4, Gg.FE11_ALDO_En2_setclr_button4, Gg.FE2_ALDO_En2_setclr_button4, Gg.FE1_ALDO_En1_setclr_button4,
    Gg.FE5_ALDO_En2_setclr_button4, Gg.FE1_ALDO_En2_setclr_button4, Gg.FE8_ALDO_En1_setclr_button4, Gg.FE8_ALDO_En2_setclr_button4
]
for i in range(len(Gg.GBT_SCA4_button_array2)):
    Gg.GBT_SCA4_button_array2[i]['font'] = myfont
    if i < 16:
        Gg.GBT_SCA4_button_array2[i].grid(column=2, row=i+1)
    else:
        Gg.GBT_SCA4_button_array2[i].grid(column=5, row=i-15)

####################
### IC1D GBT-SCA ###
####################
GBT_SCA1_label = tk.Label(GBT_SCA1_GPIO_frame, text='IC1D GBT-SCA')
GBT_SCA1_label.grid(column=6, row=0)
GBT_SCA1_label['font'] = myfont

GBT_SCA1_label_array = [
    tk.Label(GBT_SCA1_GPIO_frame, text='FE2 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='FE5 ALDO Enable2'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE8 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='FE8 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE11 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='FE1 ALDO Enable2'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE1 ALDO Enable1'), tk.Label(GBT_SCA1_GPIO_frame, text='FE11 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE2 ALDO Enable1'), tk.Label(GBT_SCA1_GPIO_frame, text='FE4 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE12 ALDO Enable1'), tk.Label(GBT_SCA1_GPIO_frame, text='PCC A EN IV8 2'),
    tk.Label(GBT_SCA1_GPIO_frame, text='PCC A EN IV8 1'), tk.Label(GBT_SCA1_GPIO_frame, text='FE12 ALDO Enable2'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE3 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='FE4 ALDO Enable2'),
    tk.Label(GBT_SCA1_GPIO_frame, text='oEN A'), tk.Label(GBT_SCA1_GPIO_frame, text='FE6 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE6 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='eSS A'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE3 ALDO Enable1'), tk.Label(GBT_SCA1_GPIO_frame, text='FE5 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='cEN A'), tk.Label(GBT_SCA1_GPIO_frame, text='FE7 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE7 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='cSS A'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE9 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='FE9 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='PCC B EN IV8 2'), tk.Label(GBT_SCA1_GPIO_frame, text='FE10 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE10 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='PCC B EN IV8 1')
]
for i in range(len(GBT_SCA1_label_array)):
    GBT_SCA1_label_array[i]['font'] = myfont
    if i < 16:
        GBT_SCA1_label_array[i].grid(column=6, row=i+1)
    else:
        GBT_SCA1_label_array[i].grid(column=9, row=i-15)

Gg.FE2_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable2_onoff1())
Gg.FE5_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable2_onoff1())
Gg.FE8_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable2_onoff1())
Gg.FE8_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable1_onoff1())
Gg.FE11_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable2_onoff1())
Gg.FE1_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable2_onoff1())
Gg.FE1_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable1_onoff1())
Gg.FE11_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable1_onoff1())
Gg.FE2_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable1_onoff1())
Gg.FE4_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable1_onoff1())
Gg.FE12_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable1_onoff1())
Gg.PCC_A_EN_IV8_2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_2_onoff1())
Gg.PCC_A_EN_IV8_1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_1_onoff1())
Gg.FE12_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable2_onoff1())
Gg.FE3_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable2_onoff1())
Gg.FE4_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable2_onoff1())
Gg.oEN_A_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.oEN_A_onoff1())
Gg.FE6_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable1_onoff1())
Gg.FE6_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable2_onoff1())
Gg.eSS_A_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.eSS_A_onoff1())
Gg.FE3_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable1_onoff1())
Gg.FE5_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable1_onoff1())
Gg.cEN_A_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.cEN_A_onoff1())
Gg.FE7_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable1_onoff1())
Gg.FE7_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable2_onoff1())
Gg.cSS_A_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.cSS_A_onoff1())
Gg.FE9_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable2_onoff1())
Gg.FE9_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable1_onoff1())
Gg.PCC_B_EN_IV8_2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_2_onoff1())
Gg.FE10_ALDO_En1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable1_onoff1())
Gg.FE10_ALDO_En2_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable2_onoff1())
Gg.PCC_B_EN_IV8_1_onoff_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_1_onoff1())

Gg.GBT_SCA1_button_array = [
    Gg.FE2_ALDO_En2_onoff_button1, Gg.FE5_ALDO_En2_onoff_button1, Gg.FE8_ALDO_En2_onoff_button1, Gg.FE8_ALDO_En1_onoff_button1,
    Gg.FE11_ALDO_En2_onoff_button1, Gg.FE1_ALDO_En2_onoff_button1, Gg.FE1_ALDO_En1_onoff_button1, Gg.FE11_ALDO_En1_onoff_button1,
    Gg.FE2_ALDO_En1_onoff_button1, Gg.FE4_ALDO_En1_onoff_button1, Gg.FE12_ALDO_En1_onoff_button1, Gg.PCC_A_EN_IV8_2_onoff_button1,
    Gg.PCC_A_EN_IV8_1_onoff_button1, Gg.FE12_ALDO_En2_onoff_button1, Gg.FE3_ALDO_En2_onoff_button1, Gg.FE4_ALDO_En2_onoff_button1,
    Gg.oEN_A_onoff_button1, Gg.FE6_ALDO_En1_onoff_button1, Gg.FE6_ALDO_En2_onoff_button1, Gg.eSS_A_onoff_button1,
    Gg.FE3_ALDO_En1_onoff_button1, Gg.FE5_ALDO_En1_onoff_button1, Gg.cEN_A_onoff_button1, Gg.FE7_ALDO_En1_onoff_button1,
    Gg.FE7_ALDO_En2_onoff_button1, Gg.cSS_A_onoff_button1, Gg.FE9_ALDO_En2_onoff_button1, Gg.FE9_ALDO_En1_onoff_button1,
    Gg.PCC_B_EN_IV8_2_onoff_button1, Gg.FE10_ALDO_En1_onoff_button1, Gg.FE10_ALDO_En2_onoff_button1, Gg.PCC_B_EN_IV8_1_onoff_button1
]
for i in range(len(Gg.GBT_SCA1_button_array)):
    Gg.GBT_SCA1_button_array[i]['font'] = myfont
    if i < 16:
        Gg.GBT_SCA1_button_array[i].grid(column=7, row=i+1)
    else:
        Gg.GBT_SCA1_button_array[i].grid(column=10, row=i-15)

Gg.FE2_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable2_setclr1())
Gg.FE5_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable2_setclr1())
Gg.FE8_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable2_setclr1())
Gg.FE8_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE8_ALDO_Enable1_setclr1())
Gg.FE11_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable2_setclr1())
Gg.FE1_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable2_setclr1())
Gg.FE1_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE1_ALDO_Enable1_setclr1())
Gg.FE11_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE11_ALDO_Enable1_setclr1())
Gg.FE2_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE2_ALDO_Enable1_setclr1())
Gg.FE4_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable1_setclr1())
Gg.FE12_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable1_setclr1())
Gg.PCC_A_EN_IV8_2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_2_setclr1())
Gg.PCC_A_EN_IV8_1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_A_EN_IV8_1_setclr1())
Gg.FE12_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE12_ALDO_Enable2_setclr1())
Gg.FE3_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable2_setclr1())
Gg.FE4_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE4_ALDO_Enable2_setclr1())
Gg.oEN_A_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.oEN_A_setclr1())
Gg.FE6_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable1_setclr1())
Gg.FE6_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE6_ALDO_Enable2_setclr1())
Gg.eSS_A_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.eSS_A_setclr1())
Gg.FE3_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE3_ALDO_Enable1_setclr1())
Gg.FE5_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE5_ALDO_Enable1_setclr1())
Gg.cEN_A_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.cEN_A_setclr1())
Gg.FE7_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable1_setclr1())
Gg.FE7_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE7_ALDO_Enable2_setclr1())
Gg.cSS_A_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.cSS_A_setclr1())
Gg.FE9_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable2_setclr1())
Gg.FE9_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE9_ALDO_Enable1_setclr1())
Gg.PCC_B_EN_IV8_2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_2_setclr1())
Gg.FE10_ALDO_En1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable1_setclr1())
Gg.FE10_ALDO_En2_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.FE10_ALDO_Enable2_setclr1())
Gg.PCC_B_EN_IV8_1_setclr_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.PCC_B_EN_IV8_1_setclr1())

Gg.GBT_SCA1_button_array2 = [
    Gg.FE2_ALDO_En2_setclr_button1, Gg.FE5_ALDO_En2_setclr_button1, Gg.FE8_ALDO_En2_setclr_button1, Gg.FE8_ALDO_En1_setclr_button1,
    Gg.FE11_ALDO_En2_setclr_button1, Gg.FE1_ALDO_En2_setclr_button1, Gg.FE1_ALDO_En1_setclr_button1, Gg.FE11_ALDO_En1_setclr_button1,
    Gg.FE2_ALDO_En1_setclr_button1, Gg.FE4_ALDO_En1_setclr_button1, Gg.FE12_ALDO_En1_setclr_button1, Gg.PCC_A_EN_IV8_2_setclr_button1,
    Gg.PCC_A_EN_IV8_1_setclr_button1, Gg.FE12_ALDO_En2_setclr_button1, Gg.FE3_ALDO_En2_setclr_button1, Gg.FE4_ALDO_En2_setclr_button1,
    Gg.oEN_A_setclr_button1, Gg.FE6_ALDO_En1_setclr_button1, Gg.FE6_ALDO_En2_setclr_button1, Gg.eSS_A_setclr_button1,
    Gg.FE3_ALDO_En1_setclr_button1, Gg.FE5_ALDO_En1_setclr_button1, Gg.cEN_A_setclr_button1, Gg.FE7_ALDO_En1_setclr_button1,
    Gg.FE7_ALDO_En2_setclr_button1, Gg.cSS_A_setclr_button1, Gg.FE9_ALDO_En2_setclr_button1, Gg.FE9_ALDO_En1_setclr_button1,
    Gg.PCC_B_EN_IV8_2_setclr_button1, Gg.FE10_ALDO_En1_setclr_button1, Gg.FE10_ALDO_En2_setclr_button1, Gg.PCC_B_EN_IV8_1_setclr_button1
]
for i in range(len(Gg.GBT_SCA1_button_array2)):
    Gg.GBT_SCA1_button_array2[i]['font'] = myfont
    if i < 16:
        Gg.GBT_SCA1_button_array2[i].grid(column=8, row=i+1)
    else:
        Gg.GBT_SCA1_button_array2[i].grid(column=11, row=i-15)

#####################
### IC3D LpGBT L0 ###
#####################
LpGBT3_label = tk.Label(LpGBT1_GPIO_frame, text='IC3D LpGBT L0')
LpGBT3_label.grid(column=0, row=0)
LpGBT3_label['font'] = myfont

LpGBT3_label_array = [
    tk.Label(LpGBT1_GPIO_frame, text='N13'), tk.Label(LpGBT1_GPIO_frame, text='N12'),
    tk.Label(LpGBT1_GPIO_frame, text='clkEnS'), tk.Label(LpGBT1_GPIO_frame, text='PCC A PG 1V8 2'),
    tk.Label(LpGBT1_GPIO_frame, text='PCC A PG 1V2'), tk.Label(LpGBT1_GPIO_frame, text='PCC A PG 1V8 1'),
    tk.Label(LpGBT1_GPIO_frame, text='calEnPE'), tk.Label(LpGBT1_GPIO_frame, text='calEnS'),
    tk.Label(LpGBT1_GPIO_frame, text='eEnPE'), tk.Label(LpGBT1_GPIO_frame, text='eEnS'),
    tk.Label(LpGBT1_GPIO_frame, text='clkEnPE'), tk.Label(LpGBT1_GPIO_frame, text='N8'),
    tk.Label(LpGBT1_GPIO_frame, text='L7'), tk.Label(LpGBT1_GPIO_frame, text='L6'),
    tk.Label(LpGBT1_GPIO_frame, text='L5'), tk.Label(LpGBT1_GPIO_frame, text='R3')
]
for i in range(len(LpGBT3_label_array)):
    LpGBT3_label_array[i]['font'] = myfont
    LpGBT3_label_array[i].grid(column=0, row=i+1)

Gg.N13_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button0, output_textbox, 0, 0))
Gg.N12_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button1, output_textbox, 0, 1))
Gg.clkEnS_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button2, output_textbox, 0, 2))
Gg.PCC_A_PG_1V8_2_onoff_label3 = tk.Label(LpGBT1_GPIO_frame, width='10', text='output')
Gg.PCC_A_PG_1V2_onoff_label3 = tk.Label(LpGBT1_GPIO_frame, width='10', text='output')
Gg.PCC_A_PG_1V8_1_onoff_label3 = tk.Label(LpGBT1_GPIO_frame, width='10', text='output')
Gg.calEnPE_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button6, output_textbox, 0, 6))
Gg.calEnS_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button7, output_textbox, 0, 7))
Gg.eEnPE_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button8, output_textbox, 0, 8))
Gg.eEnS_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button9, output_textbox, 0, 9))
Gg.clkEnPE_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button10, output_textbox, 0, 10))
Gg.N8_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button11, output_textbox, 0, 11))
Gg.L7_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button12, output_textbox, 0, 12))
Gg.L6_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button13, output_textbox, 0, 13))
Gg.L5_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button14, output_textbox, 0, 14))
Gg.R3_onoff_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button15, output_textbox, 0, 15))

LpGBT3_button_array = [
    N13_onoff_button3, N12_onoff_button3, clkEnS_onoff_button3, PCC_A_PG_1V8_2_onoff_label3,
    PCC_A_PG_1V2_onoff_label3, PCC_A_PG_1V8_1_onoff_label3, calEnPE_onoff_button3, calEnS_onoff_button3,
    eEnPE_onoff_button3, eEnS_onoff_button3, clkEnPE_onoff_button3, N8_onoff_button3,
    L7_onoff_button3, L6_onoff_button3, L5_onoff_button3, R3_onoff_button3
]
for i in range(len(LpGBT3_button_array)):
    LpGBT3_button_array[i]['font'] = myfont
    LpGBT3_button_array[i].grid(column=1, row=i+1)

Gg.N13_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_0, output_textbox, 0, 0))
Gg.N12_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_1, output_textbox, 0, 1))
Gg.clkEnS_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_2, output_textbox, 0, 2))
Gg.PCC_A_PG_1V8_2_setclr_label3 = tk.Label(LpGBT1_GPIO_frame, text="")
Gg.PCC_A_PG_1V2_setclr_label3= tk.Label(LpGBT1_GPIO_frame, text="")
Gg.PCC_A_PG_1V8_1_setclr_label3 = tk.Label(LpGBT1_GPIO_frame, text="")
Gg.calEnPE_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_6, output_textbox, 0, 6))
Gg.calEnS_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_7, output_textbox, 0, 7))
Gg.eEnPE_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_8, output_textbox, 0, 8))
Gg.eEnS_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_9, output_textbox, 0, 9))
Gg.clkEnPE_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_10, output_textbox, 0, 10))
Gg.N8_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_11, output_textbox, 0, 11))
Gg.L7_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_12, output_textbox, 0, 12))
Gg.L6_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_13, output_textbox, 0, 13))
Gg.L5_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_14, output_textbox, 0, 14))
Gg.R3_setclr_button3 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_15, output_textbox, 0, 15))

LpGBT3_button_array2 = [
    N13_setclr_button3, N12_setclr_button3, clkEnS_setclr_button3, PCC_A_PG_1V8_2_setclr_label3,
    PCC_A_PG_1V2_setclr_label3, PCC_A_PG_1V8_1_setclr_label3, calEnPE_setclr_button3, calEnS_setclr_button3,
    eEnPE_setclr_button3, eEnS_setclr_button3, clkEnPE_setclr_button3, N8_setclr_button3,
    L7_setclr_button3, L6_setclr_button3, L5_setclr_button3, R3_setclr_button3
]
for i in range(len(LpGBT3_button_array2)):
    LpGBT3_button_array2[i]['font'] = myfont
    LpGBT3_button_array2[i].grid(column=2, row=i+1)

#####################
### IC2D LpGBT L1 ###
#####################
LpGBT2_label = tk.Label(LpGBT2_GPIO_frame, text='IC2D LpGBT L1')
LpGBT2_label.grid(column=0, row=0)
LpGBT2_label['font'] = myfont

LpGBT2_label_array = [
    tk.Label(LpGBT2_GPIO_frame, text='clkEnPE L1'), tk.Label(LpGBT2_GPIO_frame, text='eEnS L1'),
    tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 7'), tk.Label(LpGBT2_GPIO_frame, text='calEnS L1'),
    tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 3'), tk.Label(LpGBT2_GPIO_frame, text='clkEnS L1'),
    tk.Label(LpGBT2_GPIO_frame, text='PCC B PG 1V8 1'), tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 6'),
    tk.Label(LpGBT2_GPIO_frame, text='eEnPE L1'), tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 1'),
    tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 5'), tk.Label(LpGBT2_GPIO_frame, text='calEnPE L1'),
    tk.Label(LpGBT2_GPIO_frame, text='PCC B PG 1V8 2'), tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 2'),
    tk.Label(LpGBT2_GPIO_frame, text='PCC B PG 2V5'), tk.Label(LpGBT2_GPIO_frame, text='UnusedL1 4')
]
for i in range(len(LpGBT2_label_array)):
    LpGBT2_label_array[i]['font'] = myfont
    LpGBT2_label_array[i].grid(column=0, row=i+1)

Gg.clkEnPE_L1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button0, output_textbox, 1, 0))
Gg.eEnS_L1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button1, output_textbox, 1, 1))
Gg.UnusedL1_7_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button2, output_textbox, 1, 2))
Gg.calEnS_L1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button3, output_textbox, 1, 3))
Gg.UnusedL1_3_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button4, output_textbox, 1, 4))
Gg.clkEnS_L1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button5, output_textbox, 1, 5))
Gg.PCC_B_PG_1V8_1_onoff_label2 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
Gg.UnusedL1_6_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button7, output_textbox, 1, 7))
Gg.eEnPE_L1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button8, output_textbox, 1, 8))
Gg.UnusedL1_1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button9, output_textbox, 1, 9))
Gg.UnusedL1_5_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button10, output_textbox, 1, 10))
Gg.calEnPE_L1_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button11, output_textbox, 1, 11))
Gg.PCC_B_PG_1V8_2_onoff_label2 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
Gg.Unused_L1_2_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button13, output_textbox, 1, 13))
Gg.PCC_B_PG_2V5_onoff_label2 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
Gg.UnusedL1_4_onoff_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button15, output_textbox, 1, 15))

LpGBT2_button_array = [
    clkEnPE_L1_onoff_button2, eEnS_L1_onoff_button2, UnusedL1_7_onoff_button2, calEnS_L1_onoff_button2,
    UnusedL1_3_onoff_button2, clkEnS_L1_onoff_button2, PCC_B_PG_1V8_1_onoff_label2, UnusedL1_6_onoff_button2,
    eEnPE_L1_onoff_button2, UnusedL1_1_onoff_button2, UnusedL1_5_onoff_button2, calEnPE_L1_onoff_button2,
    PCC_B_PG_1V8_2_onoff_label2, Unused_L1_2_onoff_button2, PCC_B_PG_2V5_onoff_label2, UnusedL1_4_onoff_button2
]
for i in range(len(LpGBT2_button_array)):
    LpGBT2_button_array[i]['font'] = myfont
    LpGBT2_button_array[i].grid(column=1, row=i+1)

Gg.clkEnPE_L1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button0, output_textbox, 1, 0))
Gg.eEnS_L1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button1, output_textbox, 1, 1))
Gg.UnusedL1_7_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2, output_textbox, 1, 2))
Gg.calEnS_L1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button3, output_textbox, 1, 3))
Gg.UnusedL1_3_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button4, output_textbox, 1, 4))
Gg.clkEnS_L1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button5, output_textbox, 1, 5))
Gg.PCC_B_PG_1V8_1_setclr_label2 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
Gg.UnusedL1_6_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button7, output_textbox, 1, 7))
Gg.eEnPE_L1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button8, output_textbox, 1, 8))
Gg.UnusedL1_1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button9, output_textbox, 1, 9))
Gg.UnusedL1_5_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button10, output_textbox, 1, 10))
Gg.calEnPE_L1_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button11, output_textbox, 1, 11))
Gg.PCC_B_PG_1V8_2_setclr_label2 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
Gg.Unused_L1_2_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button13, output_textbox, 1, 13))
Gg.PCC_B_PG_2V5_setclr_label2 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
Gg.UnusedL1_4_setclr_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button15, output_textbox, 1, 15))

LpGBT2_button_array2 = [
    clkEnPE_L1_setclr_button2, eEnS_L1_setclr_button2, UnusedL1_7_setclr_button2, calEnS_L1_setclr_button2,
    UnusedL1_3_setclr_button2, clkEnS_L1_setclr_button2, PCC_B_PG_1V8_1_setclr_label2, UnusedL1_6_setclr_button2,
    eEnPE_L1_setclr_button2, UnusedL1_1_setclr_button2, UnusedL1_5_setclr_button2, calEnPE_L1_setclr_button2,
    PCC_B_PG_1V8_2_setclr_label2, Unused_L1_2_setclr_button2, PCC_B_PG_2V5_setclr_label2, UnusedL1_4_setclr_button2
]
for i in range(len(LpGBT2_button_array2)):
    LpGBT2_button_array2[i]['font'] = myfont
    LpGBT2_button_array2[i].grid(column=2, row=i+1)

### Refresh Button ###
GPIO_refresh_button = tk.Button(tab8, text="Refresh")#, command=lambda: button_functions.GPIO_refresh())
GPIO_refresh_button['font'] = myfont
GPIO_refresh_button.grid(column=3, row=1)

#####################################################################
### Analog IO tab configuration ###
#####################################################################
### IC4B GBT-SCA ###
####################
IC4B_label = tk.Label(GBT_SCA4_AnIO_frame, text='IC4B GBT-SCA')
IC4B_label['font'] = myfont
IC4B_label.grid(column=0, row=0)

IC4B_label_array = [
    tk.Label(GBT_SCA4_AnIO_frame, text='FE10 Bias I4'), tk.Label(GBT_SCA4_AnIO_frame, text='FE12 BiasI4'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE10 Bias I3'), tk.Label(GBT_SCA4_AnIO_frame, text='FE12 BiasI3'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE8 Bias I4'), tk.Label(GBT_SCA4_AnIO_frame, text='FE10 Bias I2'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE12 BiasI2'), tk.Label(GBT_SCA4_AnIO_frame, text='FE8 Bias I3'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE10 Bias I1'), tk.Label(GBT_SCA4_AnIO_frame, text='FE12 BiasI1'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE8 Bias I2'), tk.Label(GBT_SCA4_AnIO_frame, text='FE9 Bias I4'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE11 Bias I4'), tk.Label(GBT_SCA4_AnIO_frame, text='FE8 Bias I1'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE9 Bias I3'), tk.Label(GBT_SCA4_AnIO_frame, text='FE11 Bias I3'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE7 Bias I4'), tk.Label(GBT_SCA4_AnIO_frame, text='FE9 Bias I2'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE11 Bias I2'), tk.Label(GBT_SCA4_AnIO_frame, text='FE7 SIPM Temp1'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE9 Bias I1'), tk.Label(GBT_SCA4_AnIO_frame, text='FE11 Bias I1'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE7 SIPM Temp2'), tk.Label(GBT_SCA4_AnIO_frame, text='FE7 Bias I3'),
    tk.Label(GBT_SCA4_AnIO_frame, text='V BiasB mon'), tk.Label(GBT_SCA4_AnIO_frame, text='FE7 Bias I1'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE7 Bias I2'), tk.Label(GBT_SCA4_AnIO_frame, text='FE11 SIPM Temp2'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE8 SIPM Temp2'), tk.Label(GBT_SCA4_AnIO_frame, text='FE8 SIPM Temp1'),
    tk.Label(GBT_SCA4_AnIO_frame, text='FE11 SIPM Temp1')
]
for i in range(len(IC4B_label_array)):
    IC4B_label_array[i]['font'] = myfont
    if i < 16:
        IC4B_label_array[i].grid(column=0, row=i+1)
    else:
        IC4B_label_array[i].grid(column=4, row=i-15)

IC4B_label_array2 = [
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame)
]
for i in range(len(IC4B_label_array2)):
    IC4B_label_array2[i]['font'] = myfont
    IC4B_label_array2[i].configure(width=10, text="output")
    if i < 16:
        IC4B_label_array2[i].grid(column=1, row=i+1)
    else:
        IC4B_label_array2[i].grid(column=5, row=i-15)

IC4B_label_array3 = [
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame), tk.Label(GBT_SCA4_AnIO_frame),
    tk.Label(GBT_SCA4_AnIO_frame)
]
for i in range(len(IC4B_label_array3)):
    IC4B_label_array3[i]['font'] = myfont
    IC4B_label_array3[i].configure(width=10, text="output")
    if i < 16:
        IC4B_label_array3[i].grid(column=2, row=i+1)
    else:
        IC4B_label_array3[i].grid(column=6, row=i-15)

####################
### IC1B GBT-SCA ###
####################
IC1B_label = tk.Label(GBT_SCA1_AnIO_frame, text='IC1B GBT-SCA')
IC1B_label['font'] = myfont
IC1B_label.grid(column=0, row=0)

IC1B_label_array = [
    tk.Label(GBT_SCA1_AnIO_frame, text='FE4 Bias I4'), tk.Label(GBT_SCA1_AnIO_frame, text='FE6 BiasI4'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE4 Bias I3'), tk.Label(GBT_SCA1_AnIO_frame, text='FE6 BiasI3'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE2 Bias I4'), tk.Label(GBT_SCA1_AnIO_frame, text='FE4 Bias I2'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE6 BiasI2'), tk.Label(GBT_SCA1_AnIO_frame, text='FE2 Bias I3'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE4 Bias I1'), tk.Label(GBT_SCA1_AnIO_frame, text='FE6 BiasI1'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE2 Bias I2'), tk.Label(GBT_SCA1_AnIO_frame, text='FE3 Bias I4'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE5 Bias I4'), tk.Label(GBT_SCA1_AnIO_frame, text='FE2 Bias I1'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE3 Bias I3'), tk.Label(GBT_SCA1_AnIO_frame, text='FE5 Bias I3'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE1 Bias I4'), tk.Label(GBT_SCA1_AnIO_frame, text='FE3 Bias I2'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE5 Bias I2'), tk.Label(GBT_SCA1_AnIO_frame, text='FE1 SIPM Temp1'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE3 Bias I1'), tk.Label(GBT_SCA1_AnIO_frame, text='FE5 Bias I1'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE1 SIPM Temp2'), tk.Label(GBT_SCA1_AnIO_frame, text='FE1 Bias I3'),
    tk.Label(GBT_SCA1_AnIO_frame, text='V BiasA mon'), tk.Label(GBT_SCA1_AnIO_frame, text='FE1 Bias I1'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE1 Bias I2'), tk.Label(GBT_SCA1_AnIO_frame, text='FE5 SIPM Temp2'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE2 SIPM Temp2'), tk.Label(GBT_SCA1_AnIO_frame, text='FE2 SIPM Temp1'),
    tk.Label(GBT_SCA1_AnIO_frame, text='FE5 SIPM Temp1')
]
for i in range(len(IC1B_label_array)):
    IC1B_label_array[i]['font'] = myfont
    if i < 16:
        IC1B_label_array[i].grid(column=0, row=i+1)
    else:
        IC1B_label_array[i].grid(column=4, row=i-15)

IC1B_label_array2 = [
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame)
]
for i in range(len(IC1B_label_array2)):
    IC1B_label_array2[i]['font'] = myfont
    IC1B_label_array2[i].configure(width=10, text="output")
    if i < 16:
        IC1B_label_array2[i].grid(column=1, row=i+1)
    else:
        IC1B_label_array2[i].grid(column=5, row=i-15)

IC1B_label_array3 = [
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame), tk.Label(GBT_SCA1_AnIO_frame),
    tk.Label(GBT_SCA1_AnIO_frame)
]
for i in range(len(IC1B_label_array3)):
    IC1B_label_array3[i]['font'] = myfont
    IC1B_label_array3[i].configure(width=10, text="output")
    if i < 16:
        IC1B_label_array3[i].grid(column=2, row=i+1)
    else:
        IC1B_label_array3[i].grid(column=6, row=i-15)

##################
### IC3D LpGBT ###
##################
IC3D_AnIO_label = tk.Label(LpGBT1_AnIO_frame, text='IC3D LpGBT L0')
IC3D_AnIO_label['font'] = myfont
IC3D_AnIO_label.grid(column=0, row=0)

IC3D_AnIO_label_array = [
    tk.Label(LpGBT1_AnIO_frame, text='FE6 SIPM Temp1'), tk.Label(LpGBT1_AnIO_frame, text='FE6 SIPM Temp2'),
    tk.Label(LpGBT1_AnIO_frame, text='PCC A Temp 1'), tk.Label(LpGBT1_AnIO_frame, text='PCC A Temp 2'),
    tk.Label(LpGBT1_AnIO_frame, text='vmon 1V8 A'), tk.Label(LpGBT1_AnIO_frame, text='vmon 1V8 B'),
    tk.Label(LpGBT1_AnIO_frame, text='Vin mon'), tk.Label(LpGBT1_AnIO_frame, text='Cp Temp 1')
]
for i in range(len(IC3D_AnIO_label_array)):
    IC3D_AnIO_label_array[i]['font'] = myfont
    IC3D_AnIO_label_array[i].grid(column=0, row=i+1)

IC3D_AnIO_label_array2 =[
    tk.Label(LpGBT1_AnIO_frame), tk.Label(LpGBT1_AnIO_frame),
    tk.Label(LpGBT1_AnIO_frame), tk.Label(LpGBT1_AnIO_frame),
    tk.Label(LpGBT1_AnIO_frame), tk.Label(LpGBT1_AnIO_frame),
    tk.Label(LpGBT1_AnIO_frame), tk.Label(LpGBT1_AnIO_frame)
]
for i in range(len(IC3D_AnIO_label_array2)):
    IC3D_AnIO_label_array2[i]['font'] = myfont
    IC3D_AnIO_label_array2[i].configure(width=10, text="output")
    IC3D_AnIO_label_array2[i].grid(column=1,row=i+1)

##################
### IC2D LpGBT ###
##################
IC2D_AnIO_label = tk.Label(LpGBT2_AnIO_frame, text='IC2D LpGBT L1')
IC2D_AnIO_label['font'] = myfont
IC2D_AnIO_label.grid(column=0, row=0)

IC2D_AnIO_label_array = [
    tk.Label(LpGBT2_AnIO_frame, text='FE12 SIPM Temp1'), tk.Label(LpGBT2_AnIO_frame, text='FE12 SIPM Temp2'),
    tk.Label(LpGBT2_AnIO_frame, text='PCC B Temp 1'), tk.Label(LpGBT2_AnIO_frame, text='PCC B Temp 2'),
    tk.Label(LpGBT2_AnIO_frame, text='vmon 1V8 C'), tk.Label(LpGBT2_AnIO_frame, text='vmon 1V8 D'),
    tk.Label(LpGBT2_AnIO_frame, text='Cp Temp 2'), tk.Label(LpGBT2_AnIO_frame, text='Cp Temp 3')
]
for i in range(len(IC2D_AnIO_label_array)):
    IC2D_AnIO_label_array[i]['font'] = myfont
    IC2D_AnIO_label_array[i].grid(column=0, row=i+1)

IC2D_AnIO_label_array2 =[
    tk.Label(LpGBT2_AnIO_frame), tk.Label(LpGBT2_AnIO_frame),
    tk.Label(LpGBT2_AnIO_frame), tk.Label(LpGBT2_AnIO_frame),
    tk.Label(LpGBT2_AnIO_frame), tk.Label(LpGBT2_AnIO_frame),
    tk.Label(LpGBT2_AnIO_frame), tk.Label(LpGBT2_AnIO_frame)
]
for i in range(len(IC2D_AnIO_label_array2)):
    IC2D_AnIO_label_array2[i]['font'] = myfont
    IC2D_AnIO_label_array2[i].configure(width=10, text="output")
    IC2D_AnIO_label_array2[i].grid(column=1,row=i+1)

### Refresh Button ###
AnIO_refresh_button = tk.Button(tab4, text="Refresh", command=lambda: button_functions.AnIO_refresh(IC4B_label_array2, IC4B_label_array3, IC1B_label_array2, IC1B_label_array3, output_textbox))
AnIO_refresh_button['font'] = myfont
AnIO_refresh_button.grid(column=1, row=2)

#####################################################################
### Script tab buttons and configuration ###
#####################################################################
### IC4D GBT-SCA ###
IC4D_scripts_label = tk.Label(GBT_SCA4_scripts_frame, text="IC4D GBT-SCA")
IC4D_scripts_label['font'] = myfont
IC4D_scripts_label.grid(column=0, row=0)

Gg.Connect_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="Connect", command=lambda: button_functions.Connect())
Gg.Connect_button['font'] = myfont
Gg.Connect_button.grid(column=0, row=1)

Gg.EnableGPIO_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="EnableGPIO", command=lambda: button_functions.EnableGPIO())
Gg.EnableGPIO_button['font'] = myfont
Gg.EnableGPIO_button.grid(column=1, row=1)

Gg.EnableAtoD_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="EnableAtoD", command=lambda: button_functions.EnableAtoD())
Gg.EnableAtoD_button['font'] = myfont
Gg.EnableAtoD_button.grid(column=2,row=1)

Gg.Bread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="Bread", command=lambda: button_functions.Bread())
Gg.Bread_button['font'] = myfont
Gg.Bread_button.grid(column=0, row=3)

Gg.Bread_label = tk.Label(GBT_SCA4_scripts_frame, text="Bread output")
Gg.Bread_label['font'] = myfont
Gg.Bread_label.grid(column=1, row=3)

Gg.DIRread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="DIRread", command=lambda: button_functions.DIRread())
Gg.DIRread_button['font'] = myfont
Gg.DIRread_button.grid(column=0,row=4)

Gg.DIRread_label = tk.Label(GBT_SCA4_scripts_frame, text="DIRread output")
Gg.DIRread_label['font'] = myfont
Gg.DIRread_label.grid(column=1, row=4)

Gg.DATAOUTread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="DATAOUTread", command=lambda: button_functions.DATAOUTread())
Gg.DATAOUTread_button['font'] = myfont
Gg.DATAOUTread_button.grid(column=0,row=5)

Gg.DATAOUTread_label = tk.Label(GBT_SCA4_scripts_frame, text="DATAOUTread output")
Gg.DATAOUTread_label['font'] = myfont
Gg.DATAOUTread_label.grid(column=1, row=5)

Gg.IDread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="IDread", command=lambda: button_functions.IDread())
Gg.IDread_button['font'] = myfont
Gg.IDread_button.grid(column=0,row=2)

Gg.IDread_label = tk.Label(GBT_SCA4_scripts_frame, text="IDread output")
Gg.IDread_label['font'] = myfont
Gg.IDread_label.grid(column=1, row=2)

GPIO_label = tk.Label(GBT_SCA4_scripts_frame, text="enter GPIO value:")
GPIO_label['font'] = myfont
GPIO_label.grid(column=0, row=6)

Gg.GPIO_entry = tk.Entry(GBT_SCA4_scripts_frame, width=20, font=("Helvetica","12"))
Gg.GPIO_entry.grid(column=1, row=6)

GPIO_enter = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIO enter", command=lambda: button_functions.GPIOenter)
GPIO_enter['font'] = myfont
GPIO_enter.grid(column=2, row=6)

Gg.GPIOon_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOon", command=lambda: button_functions.GPIOon())
Gg.GPIOon_button['font'] = myfont
Gg.GPIOon_button.grid(column=0, row=7)

Gg.GPIOset_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOset", command=lambda: button_functions.GPIOset())
Gg.GPIOset_button['font'] = myfont
Gg.GPIOset_button.grid(column=1, row=7)

Gg.GPIOclr_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOclr", command=lambda: button_functions.GPIOclr())
Gg.GPIOclr_button['font'] = myfont
Gg.GPIOclr_button.grid(column=2, row=7)

Gg.GPIOoff_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOoff", command=lambda: button_functions.GPIOoff())
Gg.GPIOoff_button['font'] = myfont
Gg.GPIOoff_button.grid(column=3, row=7)

error_entry = tk.Entry(GBT_SCA4_scripts_frame, width=20, font=("Helvetica","12"))
error_entry.grid(column=4, row=1)
error_entry.insert(tk.END, "error output")

#####################################################################
### IC1D GBT-SCA ###
IC1D_scripts_label = tk.Label(GBT_SCA1_scripts_frame, text="IC1D GBT-SCA")
IC1D_scripts_label['font'] = myfont
IC1D_scripts_label.grid(column=0, row=0)

Connect_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="Connect", command=lambda: button_functions.Connect())
Connect_button2['font'] = myfont
Connect_button2.grid(column=0, row=1)

EnableGPIO_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="EnableGPIO", command=lambda: button_functions.EnableGPIO())
EnableGPIO_button2['font'] = myfont
EnableGPIO_button2.grid(column=1, row=1)

EnableAtoD_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="EnableAtoD", command=lambda: button_functions.EnableAtoD())
EnableAtoD_button2['font'] = myfont
EnableAtoD_button2.grid(column=2,row=1)

Bread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="Bread", command=lambda: button_functions.Bread())
Bread_button2['font'] = myfont
Bread_button2.grid(column=0, row=3)

Bread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="Bread output")
Bread_label2['font'] = myfont
Bread_label2.grid(column=1, row=3)

DIRread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="DIRread", command=lambda: button_functions.DIRread())
DIRread_button2['font'] = myfont
DIRread_button2.grid(column=0,row=4)

DIRread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="DIRread output")
DIRread_label2['font'] = myfont
DIRread_label2.grid(column=1, row=4)

DATAOUTread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="DATAOUTread", command=lambda: button_functions.DATAOUTread())
DATAOUTread_button2['font'] = myfont
DATAOUTread_button2.grid(column=0,row=5)

DATAOUTread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="DATAOUTread output")
DATAOUTread_label2['font'] = myfont
DATAOUTread_label2.grid(column=1, row=5)

IDread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="IDread", command=lambda: button_functions.IDread())
IDread_button2['font'] = myfont
IDread_button2.grid(column=0,row=2)

IDread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="IDread output")
IDread_label2['font'] = myfont
IDread_label2.grid(column=1, row=2)

GPIO_label2 = tk.Label(GBT_SCA1_scripts_frame, text="enter GPIO value:")
GPIO_label2['font'] = myfont
GPIO_label2.grid(column=0, row=6)

GPIO_entry2 = tk.Entry(GBT_SCA1_scripts_frame, width=20, font=("Helvetica","12"))
GPIO_entry2.grid(column=1, row=6)

GPIO_enter2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIO enter", command=lambda: button_functions.GPIOenter)
GPIO_enter2['font'] = myfont
GPIO_enter2.grid(column=2, row=6)

GPIOon_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOon", command=lambda: button_functions.GPIOon())
GPIOon_button2['font'] = myfont
GPIOon_button2.grid(column=0, row=7)

GPIOset_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOset", command=lambda: button_functions.GPIOset())
GPIOset_button2['font'] = myfont
GPIOset_button2.grid(column=1, row=7)

GPIOclr_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOclr", command=lambda: button_functions.GPIOclr())
GPIOclr_button2['font'] = myfont
GPIOclr_button2.grid(column=2, row=7)

GPIOoff_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOoff", command=lambda: button_functions.GPIOoff())
GPIOoff_button2['font'] = myfont
GPIOoff_button2.grid(column=3, row=7)

error_entry2 = tk.Entry(GBT_SCA1_scripts_frame, width=20, font=("Helvetica","12"))
error_entry2.grid(column=4, row=1)
error_entry2.insert(tk.END, "error output")

### Output Textbox ###
Gg.output_textbox = tk.Text(tab2, font=("Helvetica","12"))
Gg.output_textbox.place(x=0, y=525, height=340, width=900)

#####################################################################

main_notebook.pack(expand = 1, fill = "both")

Gg.root.mainloop()
