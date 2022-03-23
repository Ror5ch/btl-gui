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

#######################################################################
### Initializing Global Variables for SCA Functions ###
#######################################################################
if __name__ == '__main__':

    # PART 1: Argument parsing
    if not(len(sys.argv) == 1 or len(sys.argv) == 2):
        print "Incorrect usage!"
        print "usage: read_write_single_register.py only"
        sys.exit(1)
    if len(sys.argv) == 2:
        print(hex(int(sys.argv[1], 16)))
 
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

    
    wait = .005
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
root = tk.Tk()

myfont = font.Font(size=12)
s = ttk.Style()
s.configure('TNotebook.Tab', font=('helvetica','12'))

main_notebook = ttk.Notebook(root, width=1440, height=900)
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
    tk.Label(GBT_SCA4_GPIO_frame, text='FE10 ALDO Enable2'), tk.Label(GBT_SCA4_GPIO_frame, text='cEn B'),
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

GBT_SCA4_button0 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000001, GBT_SCA4_button0, output_textbox, 1))
GBT_SCA4_button1 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000002, GBT_SCA4_button1, output_textbox, 1))
GBT_SCA4_button2 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000004, GBT_SCA4_button2, output_textbox, 1))
GBT_SCA4_button3 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000008, GBT_SCA4_button3, output_textbox, 1))
GBT_SCA4_button4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000010, GBT_SCA4_button4, output_textbox, 1))
GBT_SCA4_button5 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000020, GBT_SCA4_button5, output_textbox, 1))
GBT_SCA4_button6 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000040, GBT_SCA4_button6, output_textbox, 1))
GBT_SCA4_button7 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000080, GBT_SCA4_button7, output_textbox, 1))
GBT_SCA4_button8 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000100, GBT_SCA4_button8, output_textbox, 1))
GBT_SCA4_button9 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000200, GBT_SCA4_button9, output_textbox, 1))
GBT_SCA4_button10 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000400, GBT_SCA4_button10, output_textbox, 1))
GBT_SCA4_button11 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000800, GBT_SCA4_button11, output_textbox, 1))
GBT_SCA4_button12 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00001000, GBT_SCA4_button12, output_textbox, 1))
GBT_SCA4_button13 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00002000, GBT_SCA4_button13, output_textbox, 1))
GBT_SCA4_button14 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00004000, GBT_SCA4_button14, output_textbox, 1))
GBT_SCA4_button15 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00008000, GBT_SCA4_button15, output_textbox, 1))
GBT_SCA4_button16 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00010000, GBT_SCA4_button16, output_textbox, 1))
GBT_SCA4_button17 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00020000, GBT_SCA4_button17, output_textbox, 1))
GBT_SCA4_button18 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00040000, GBT_SCA4_button18, output_textbox, 1))
GBT_SCA4_button19 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00080000, GBT_SCA4_button19, output_textbox, 1))
GBT_SCA4_button20 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00100000, GBT_SCA4_button20, output_textbox, 1))
GBT_SCA4_button21 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00200000, GBT_SCA4_button21, output_textbox, 1))
GBT_SCA4_button22 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00400000, GBT_SCA4_button22, output_textbox, 1))
GBT_SCA4_button23 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00800000, GBT_SCA4_button23, output_textbox, 1))
GBT_SCA4_button24 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x01000000, GBT_SCA4_button24, output_textbox, 1))
GBT_SCA4_button25 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x02000000, GBT_SCA4_button25, output_textbox, 1))
GBT_SCA4_button26 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x04000000, GBT_SCA4_button26, output_textbox, 1))
GBT_SCA4_button27 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x08000000, GBT_SCA4_button27, output_textbox, 1))
GBT_SCA4_button28 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x10000000, GBT_SCA4_button28, output_textbox, 1))
GBT_SCA4_button29 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x20000000, GBT_SCA4_button29, output_textbox, 1))
GBT_SCA4_button30 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x40000000, GBT_SCA4_button30, output_textbox, 1))
GBT_SCA4_button31 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x80000000, GBT_SCA4_button31, output_textbox, 1))

GBT_SCA4_button_array = [
    GBT_SCA4_button0, GBT_SCA4_button1, GBT_SCA4_button2, GBT_SCA4_button3,
    GBT_SCA4_button4, GBT_SCA4_button5, GBT_SCA4_button6, GBT_SCA4_button7,
    GBT_SCA4_button8, GBT_SCA4_button9, GBT_SCA4_button10, GBT_SCA4_button11,
    GBT_SCA4_button12, GBT_SCA4_button13, GBT_SCA4_button14, GBT_SCA4_button15,
    GBT_SCA4_button16, GBT_SCA4_button17, GBT_SCA4_button18, GBT_SCA4_button19,
    GBT_SCA4_button20, GBT_SCA4_button21, GBT_SCA4_button22, GBT_SCA4_button23,
    GBT_SCA4_button24, GBT_SCA4_button25, GBT_SCA4_button26, GBT_SCA4_button27,
    GBT_SCA4_button28, GBT_SCA4_button29, GBT_SCA4_button30, GBT_SCA4_button31
]
for i in range(len(GBT_SCA4_button_array)):
    GBT_SCA4_button_array[i]['font'] = myfont
    if i < 16:
        GBT_SCA4_button_array[i].grid(column=1, row=i+1)
    else:
        GBT_SCA4_button_array[i].grid(column=4, row=i-15)

GBT_SCA4_button2_0 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000001, GBT_SCA4_button2_0, output_textbox, 1))
GBT_SCA4_button2_1 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000002, GBT_SCA4_button2_1, output_textbox, 1))
GBT_SCA4_button2_2 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000004, GBT_SCA4_button2_2, output_textbox, 1))
GBT_SCA4_button2_3 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000008, GBT_SCA4_button2_3, output_textbox, 1))
GBT_SCA4_button2_4 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000010, GBT_SCA4_button2_4, output_textbox, 1))
GBT_SCA4_button2_5 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000020, GBT_SCA4_button2_5, output_textbox, 1))
GBT_SCA4_button2_6 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000040, GBT_SCA4_button2_6, output_textbox, 1))
GBT_SCA4_button2_7 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000080, GBT_SCA4_button2_7, output_textbox, 1))
GBT_SCA4_button2_8 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000100, GBT_SCA4_button2_8, output_textbox, 1))
GBT_SCA4_button2_9 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000200, GBT_SCA4_button2_9, output_textbox, 1))
GBT_SCA4_button2_10 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000400, GBT_SCA4_button2_10, output_textbox, 1))
GBT_SCA4_button2_11 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000800, GBT_SCA4_button2_11, output_textbox, 1))
GBT_SCA4_button2_12 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00001000, GBT_SCA4_button2_12, output_textbox, 1))
GBT_SCA4_button2_13 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00002000, GBT_SCA4_button2_13, output_textbox, 1))
GBT_SCA4_button2_14 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00004000, GBT_SCA4_button2_14, output_textbox, 1))
GBT_SCA4_button2_15 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00008000, GBT_SCA4_button2_15, output_textbox, 1))
GBT_SCA4_button2_16 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00010000, GBT_SCA4_button2_16, output_textbox, 1))
GBT_SCA4_button2_17 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00020000, GBT_SCA4_button2_17, output_textbox, 1))
GBT_SCA4_button2_18 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00040000, GBT_SCA4_button2_18, output_textbox, 1))
GBT_SCA4_button2_19 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00080000, GBT_SCA4_button2_19, output_textbox, 1))
GBT_SCA4_button2_20 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00100000, GBT_SCA4_button2_20, output_textbox, 1))
GBT_SCA4_button2_21 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00200000, GBT_SCA4_button2_21, output_textbox, 1))
GBT_SCA4_button2_22 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00400000, GBT_SCA4_button2_22, output_textbox, 1))
GBT_SCA4_button2_23 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00800000, GBT_SCA4_button2_23, output_textbox, 1))
GBT_SCA4_button2_24 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x01000000, GBT_SCA4_button2_24, output_textbox, 1))
GBT_SCA4_button2_25 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x02000000, GBT_SCA4_button2_25, output_textbox, 1))
GBT_SCA4_button2_26 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x04000000, GBT_SCA4_button2_26, output_textbox, 1))
GBT_SCA4_button2_27 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x08000000, GBT_SCA4_button2_27, output_textbox, 1))
GBT_SCA4_button2_28 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x10000000, GBT_SCA4_button2_28, output_textbox, 1))
GBT_SCA4_button2_29 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x20000000, GBT_SCA4_button2_29, output_textbox, 1))
GBT_SCA4_button2_30 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x40000000, GBT_SCA4_button2_30, output_textbox, 1))
GBT_SCA4_button2_31 = tk.Button(GBT_SCA4_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x80000000, GBT_SCA4_button2_31, output_textbox, 1))

GBT_SCA4_button_array2 = [
    GBT_SCA4_button2_0, GBT_SCA4_button2_1, GBT_SCA4_button2_2, GBT_SCA4_button2_3,
    GBT_SCA4_button2_4, GBT_SCA4_button2_5, GBT_SCA4_button2_6, GBT_SCA4_button2_7,
    GBT_SCA4_button2_8, GBT_SCA4_button2_9, GBT_SCA4_button2_10, GBT_SCA4_button2_11,
    GBT_SCA4_button2_12, GBT_SCA4_button2_13, GBT_SCA4_button2_14, GBT_SCA4_button2_15,
    GBT_SCA4_button2_16, GBT_SCA4_button2_17, GBT_SCA4_button2_18, GBT_SCA4_button2_19,
    GBT_SCA4_button2_20, GBT_SCA4_button2_21, GBT_SCA4_button2_22, GBT_SCA4_button2_23,
    GBT_SCA4_button2_24, GBT_SCA4_button2_25, GBT_SCA4_button2_26, GBT_SCA4_button2_27,
    GBT_SCA4_button2_28, GBT_SCA4_button2_29, GBT_SCA4_button2_30, GBT_SCA4_button2_31
]
for i in range(len(GBT_SCA4_button_array2)):
    GBT_SCA4_button_array2[i]['font'] = myfont
    if i < 16:
        GBT_SCA4_button_array2[i].grid(column=2, row=i+1)
    else:
        GBT_SCA4_button_array2[i].grid(column=5, row=i-15)

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
    tk.Label(GBT_SCA1_GPIO_frame, text='FE6 ALDO Enable2'), tk.Label(GBT_SCA1_GPIO_frame, text='ess A'),
    tk.Label(GBT_SCA1_GPIO_frame, text='FE3 ALDO Enable1'), tk.Label(GBT_SCA1_GPIO_frame, text='FE5 ALDO Enable1'),
    tk.Label(GBT_SCA1_GPIO_frame, text='cEn A'), tk.Label(GBT_SCA1_GPIO_frame, text='FE7 ALDO Enable1'),
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

GBT_SCA1_button0 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000001, GBT_SCA1_button0, output_textbox, 2))
GBT_SCA1_button1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000002, GBT_SCA1_button1, output_textbox, 2))
GBT_SCA1_button2 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000004, GBT_SCA1_button2, output_textbox, 2))
GBT_SCA1_button3 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000008, GBT_SCA1_button3, output_textbox, 2))
GBT_SCA1_button4 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000010, GBT_SCA1_button4, output_textbox, 2))
GBT_SCA1_button5 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000020, GBT_SCA1_button5, output_textbox, 2))
GBT_SCA1_button6 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000040, GBT_SCA1_button6, output_textbox, 2))
GBT_SCA1_button7 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000080, GBT_SCA1_button7, output_textbox, 2))
GBT_SCA1_button8 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000100, GBT_SCA1_button8, output_textbox, 2))
GBT_SCA1_button9 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000200, GBT_SCA1_button9, output_textbox, 2))
GBT_SCA1_button10 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000400, GBT_SCA1_button10, output_textbox, 2))
GBT_SCA1_button11 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00000800, GBT_SCA1_button11, output_textbox, 2))
GBT_SCA1_button12 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00001000, GBT_SCA1_button12, output_textbox, 2))
GBT_SCA1_button13 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00002000, GBT_SCA1_button13, output_textbox, 2))
GBT_SCA1_button14 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00004000, GBT_SCA1_button14, output_textbox, 2))
GBT_SCA1_button15 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00008000, GBT_SCA1_button15, output_textbox, 2))
GBT_SCA1_button16 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00010000, GBT_SCA1_button16, output_textbox, 2))
GBT_SCA1_button17 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00020000, GBT_SCA1_button17, output_textbox, 2))
GBT_SCA1_button18 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00040000, GBT_SCA1_button18, output_textbox, 2))
GBT_SCA1_button19 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00080000, GBT_SCA1_button19, output_textbox, 2))
GBT_SCA1_button20 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00100000, GBT_SCA1_button20, output_textbox, 2))
GBT_SCA1_button21 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00200000, GBT_SCA1_button21, output_textbox, 2))
GBT_SCA1_button22 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00400000, GBT_SCA1_button22, output_textbox, 2))
GBT_SCA1_button23 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x00800000, GBT_SCA1_button23, output_textbox, 2))
GBT_SCA1_button24 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x01000000, GBT_SCA1_button24, output_textbox, 2))
GBT_SCA1_button25 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x02000000, GBT_SCA1_button25, output_textbox, 2))
GBT_SCA1_button26 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x04000000, GBT_SCA1_button26, output_textbox, 2))
GBT_SCA1_button27 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x08000000, GBT_SCA1_button27, output_textbox, 2))
GBT_SCA1_button28 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x10000000, GBT_SCA1_button28, output_textbox, 2))
GBT_SCA1_button29 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x20000000, GBT_SCA1_button29, output_textbox, 2))
GBT_SCA1_button30 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x40000000, GBT_SCA1_button30, output_textbox, 2))
GBT_SCA1_button31 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOon_off_button(0x80000000, GBT_SCA1_button31, output_textbox, 2))

GBT_SCA1_button_array = [
    GBT_SCA1_button0, GBT_SCA1_button1, GBT_SCA1_button2, GBT_SCA1_button3,
    GBT_SCA1_button4, GBT_SCA1_button5, GBT_SCA1_button6, GBT_SCA1_button7,
    GBT_SCA1_button8, GBT_SCA1_button9, GBT_SCA1_button10, GBT_SCA1_button11,
    GBT_SCA1_button12, GBT_SCA1_button13, GBT_SCA1_button14, GBT_SCA1_button15,
    GBT_SCA1_button16, GBT_SCA1_button17, GBT_SCA1_button18, GBT_SCA1_button19,
    GBT_SCA1_button20, GBT_SCA1_button21, GBT_SCA1_button22, GBT_SCA1_button23,
    GBT_SCA1_button24, GBT_SCA1_button25, GBT_SCA1_button26, GBT_SCA1_button27,
    GBT_SCA1_button28, GBT_SCA1_button29, GBT_SCA1_button30, GBT_SCA1_button31
]
for i in range(len(GBT_SCA1_button_array)):
    GBT_SCA1_button_array[i]['font'] = myfont
    if i < 16:
        GBT_SCA1_button_array[i].grid(column=7, row=i+1)
    else:
        GBT_SCA1_button_array[i].grid(column=10, row=i-15)

GBT_SCA1_button2_0 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000001, GBT_SCA1_button2_0, output_textbox, 2))
GBT_SCA1_button2_1 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000002, GBT_SCA1_button2_1, output_textbox, 2))
GBT_SCA1_button2_2 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000004, GBT_SCA1_button2_2, output_textbox, 2))
GBT_SCA1_button2_3 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000008, GBT_SCA1_button2_3, output_textbox, 2))
GBT_SCA1_button2_4 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000010, GBT_SCA1_button2_4, output_textbox, 2))
GBT_SCA1_button2_5 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000020, GBT_SCA1_button2_5, output_textbox, 2))
GBT_SCA1_button2_6 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000040, GBT_SCA1_button2_6, output_textbox, 2))
GBT_SCA1_button2_7 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000080, GBT_SCA1_button2_7, output_textbox, 2))
GBT_SCA1_button2_8 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000100, GBT_SCA1_button2_8, output_textbox, 2))
GBT_SCA1_button2_9 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000200, GBT_SCA1_button2_9, output_textbox, 2))
GBT_SCA1_button2_10 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000400, GBT_SCA1_button2_10, output_textbox, 2))
GBT_SCA1_button2_11 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00000800, GBT_SCA1_button2_11, output_textbox, 2))
GBT_SCA1_button2_12 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00001000, GBT_SCA1_button2_12, output_textbox, 2))
GBT_SCA1_button2_13 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00002000, GBT_SCA1_button2_13, output_textbox, 2))
GBT_SCA1_button2_14 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00004000, GBT_SCA1_button2_14, output_textbox, 2))
GBT_SCA1_button2_15 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00008000, GBT_SCA1_button2_15, output_textbox, 2))
GBT_SCA1_button2_16 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00010000, GBT_SCA1_button2_16, output_textbox, 2))
GBT_SCA1_button2_17 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00020000, GBT_SCA1_button2_17, output_textbox, 2))
GBT_SCA1_button2_18 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00040000, GBT_SCA1_button2_18, output_textbox, 2))
GBT_SCA1_button2_19 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00080000, GBT_SCA1_button2_19, output_textbox, 2))
GBT_SCA1_button2_20 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00100000, GBT_SCA1_button2_20, output_textbox, 2))
GBT_SCA1_button2_21 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00200000, GBT_SCA1_button2_21, output_textbox, 2))
GBT_SCA1_button2_22 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00400000, GBT_SCA1_button2_22, output_textbox, 2))
GBT_SCA1_button2_23 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x00800000, GBT_SCA1_button2_23, output_textbox, 2))
GBT_SCA1_button2_24 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x01000000, GBT_SCA1_button2_24, output_textbox, 2))
GBT_SCA1_button2_25 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x02000000, GBT_SCA1_button2_25, output_textbox, 2))
GBT_SCA1_button2_26 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x04000000, GBT_SCA1_button2_26, output_textbox, 2))
GBT_SCA1_button2_27 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x08000000, GBT_SCA1_button2_27, output_textbox, 2))
GBT_SCA1_button2_28 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x10000000, GBT_SCA1_button2_28, output_textbox, 2))
GBT_SCA1_button2_29 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x20000000, GBT_SCA1_button2_29, output_textbox, 2))
GBT_SCA1_button2_30 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x40000000, GBT_SCA1_button2_30, output_textbox, 2))
GBT_SCA1_button2_31 = tk.Button(GBT_SCA1_GPIO_frame, bg="white", command=lambda: button_functions.GPIOset_clr_button(0x80000000, GBT_SCA1_button2_31, output_textbox, 2))

GBT_SCA1_button_array2 = [
    GBT_SCA1_button2_0, GBT_SCA1_button2_1, GBT_SCA1_button2_2, GBT_SCA1_button2_3,
    GBT_SCA1_button2_4, GBT_SCA1_button2_5, GBT_SCA1_button2_6, GBT_SCA1_button2_7,
    GBT_SCA1_button2_8, GBT_SCA1_button2_9, GBT_SCA1_button2_10, GBT_SCA1_button2_11,
    GBT_SCA1_button2_12, GBT_SCA1_button2_13, GBT_SCA1_button2_14, GBT_SCA1_button2_15,
    GBT_SCA1_button2_16, GBT_SCA1_button2_17, GBT_SCA1_button2_18, GBT_SCA1_button2_19,
    GBT_SCA1_button2_20, GBT_SCA1_button2_21, GBT_SCA1_button2_22, GBT_SCA1_button2_23,
    GBT_SCA1_button2_24, GBT_SCA1_button2_25, GBT_SCA1_button2_26, GBT_SCA1_button2_27,
    GBT_SCA1_button2_28, GBT_SCA1_button2_29, GBT_SCA1_button2_30, GBT_SCA1_button2_31
]
for i in range(len(GBT_SCA1_button_array2)):
    GBT_SCA1_button_array2[i]['font'] = myfont
    if i < 16:
        GBT_SCA1_button_array2[i].grid(column=8, row=i+1)
    else:
        GBT_SCA1_button_array2[i].grid(column=11, row=i-15)

##################
### IC5D LpGBT ###
##################
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

LpGBT3_button0 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button0, output_textbox, 3, 0))
LpGBT3_button1 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button1, output_textbox, 3, 1))
LpGBT3_button2 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button2, output_textbox, 3, 2))
LpGBT3_label3 = tk.Label(LpGBT1_GPIO_frame, width='10', text='output')
LpGBT3_label4 = tk.Label(LpGBT1_GPIO_frame, width='10', text='output')
LpGBT3_label5 = tk.Label(LpGBT1_GPIO_frame, width='10', text='output')
LpGBT3_button6 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button6, output_textbox, 3, 6))
LpGBT3_button7 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button7, output_textbox, 3, 7))
LpGBT3_button8 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button8, output_textbox, 3, 8))
LpGBT3_button9 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button9, output_textbox, 3, 9))
LpGBT3_button10 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button10, output_textbox, 3, 10))
LpGBT3_button11 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button11, output_textbox, 3, 11))
LpGBT3_button12 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button12, output_textbox, 3, 12))
LpGBT3_button13 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button13, output_textbox, 3, 13))
LpGBT3_button14 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button14, output_textbox, 3, 14))
LpGBT3_button15 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT3_button15, output_textbox, 3, 15))

LpGBT3_button_array = [
    LpGBT3_button0, LpGBT3_button1, LpGBT3_button2, LpGBT3_label3, LpGBT3_label4, LpGBT3_label5,
    LpGBT3_button6, LpGBT3_button7, LpGBT3_button8, LpGBT3_button9, LpGBT3_button10, LpGBT3_button11,
    LpGBT3_button12, LpGBT3_button13, LpGBT3_button14, LpGBT3_button15
]
for i in range(len(LpGBT3_button_array)):
    LpGBT3_button_array[i]['font'] = myfont
    LpGBT3_button_array[i].grid(column=1, row=i+1)

LpGBT3_button2_0 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_0, output_textbox, 3, 0))
LpGBT3_button2_1 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_1, output_textbox, 3, 1))
LpGBT3_button2_2 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_2, output_textbox, 3, 2))
LpGBT3_label2_3 = tk.Label(LpGBT1_GPIO_frame, text="")
LpGBT3_label2_4 = tk.Label(LpGBT1_GPIO_frame, text="")
LpGBT3_label2_5 = tk.Label(LpGBT1_GPIO_frame, text="")
LpGBT3_button2_6 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_6, output_textbox, 3, 6))
LpGBT3_button2_7 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_7, output_textbox, 3, 7))
LpGBT3_button2_8 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_8, output_textbox, 3, 8))
LpGBT3_button2_9 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_9, output_textbox, 3, 9))
LpGBT3_button2_10 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_10, output_textbox, 3, 10))
LpGBT3_button2_11 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_11, output_textbox, 3, 11))
LpGBT3_button2_12 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_12, output_textbox, 3, 12))
LpGBT3_button2_13 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_13, output_textbox, 3, 13))
LpGBT3_button2_14 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_14, output_textbox, 3, 14))
LpGBT3_button2_15 = tk.Button(LpGBT1_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT3_button2_15, output_textbox, 3, 15))

LpGBT3_button_array2 = [
    LpGBT3_button2_0, LpGBT3_button2_1, LpGBT3_button2_2, LpGBT3_label2_3, LpGBT3_label2_4,
    LpGBT3_label2_5, LpGBT3_button2_6, LpGBT3_button2_7, LpGBT3_button2_8, LpGBT3_button2_9,
    LpGBT3_button2_10, LpGBT3_button2_11, LpGBT3_button2_12, LpGBT3_button2_13, LpGBT3_button2_14,
    LpGBT3_button2_15
]
for i in range(len(LpGBT3_button_array2)):
    LpGBT3_button_array2[i]['font'] = myfont
    LpGBT3_button_array2[i].grid(column=2, row=i+1)

##################
### IC2D LpGBT ###
##################
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

LpGBT2_button0 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button0, output_textbox, 2, 0))
LpGBT2_button1 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button1, output_textbox, 2, 1))
LpGBT2_button2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button2, output_textbox, 2, 2))
LpGBT2_button3 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button3, output_textbox, 2, 3))
LpGBT2_button4 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button4, output_textbox, 2, 4))
LpGBT2_button5 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button5, output_textbox, 2, 5))
LpGBT2_label6 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
LpGBT2_button7 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button7, output_textbox, 2, 7))
LpGBT2_button8 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button8, output_textbox, 2, 8))
LpGBT2_button9 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button9, output_textbox, 2, 9))
LpGBT2_button10 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button10, output_textbox, 2, 10))
LpGBT2_button11 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button11, output_textbox, 2, 11))
LpGBT2_label12 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
LpGBT2_button13 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button13, output_textbox, 2, 13))
LpGBT2_label14 = tk.Label(LpGBT2_GPIO_frame, width='10', text='output')
LpGBT2_button15 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTon_off_button(LpGBT2_button15, output_textbox, 2, 15))

LpGBT2_button_array = [
    LpGBT2_button0, LpGBT2_button1, LpGBT2_button2, LpGBT2_button3, LpGBT2_button4, LpGBT2_button5,
    LpGBT2_label6, LpGBT2_button7, LpGBT2_button8, LpGBT2_button9, LpGBT2_button10, LpGBT2_button11,
    LpGBT2_label12, LpGBT2_button13, LpGBT2_label14, LpGBT2_button15
]
for i in range(len(LpGBT2_button_array)):
    LpGBT2_button_array[i]['font'] = myfont
    LpGBT2_button_array[i].grid(column=1, row=i+1)

LpGBT2_button2_0 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_0, output_textbox, 2, 0))
LpGBT2_button2_1 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_1, output_textbox, 2, 1))
LpGBT2_button2_2 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_2, output_textbox, 2, 2))
LpGBT2_button2_3 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_3, output_textbox, 2, 3))
LpGBT2_button2_4 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_4, output_textbox, 2, 4))
LpGBT2_button2_5 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_5, output_textbox, 2, 5))
LpGBT2_label2_6 = tk.Label(LpGBT2_GPIO_frame, text="")
LpGBT2_button2_7 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_7, output_textbox, 2, 7))
LpGBT2_button2_8 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_8, output_textbox, 2, 8))
LpGBT2_button2_9 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_9, output_textbox, 2, 9))
LpGBT2_button2_10 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_10, output_textbox, 2, 10))
LpGBT2_button2_11 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_11, output_textbox, 2, 11))
LpGBT2_label2_12 = tk.Label(LpGBT2_GPIO_frame, text="")
LpGBT2_button2_13 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_13, output_textbox, 2, 13))
LpGBT2_label2_14 = tk.Label(LpGBT2_GPIO_frame, text="")
LpGBT2_button2_15 = tk.Button(LpGBT2_GPIO_frame, bg="white", command=lambda: button_functions.LpGBTset_clr_button(LpGBT2_button2_15, output_textbox, 2, 15))

LpGBT2_button_array2 = [
    LpGBT2_button2_0, LpGBT2_button2_1, LpGBT2_button2_2, LpGBT2_button2_3, LpGBT2_button2_4,
    LpGBT2_button2_5, LpGBT2_label2_6, LpGBT2_button2_7, LpGBT2_button2_8, LpGBT2_button2_9,
    LpGBT2_button2_10, LpGBT2_button2_11, LpGBT2_label2_12, LpGBT2_button2_13, LpGBT2_label2_14,
    LpGBT2_button2_15
]
for i in range(len(LpGBT2_button_array2)):
    LpGBT2_button_array2[i]['font'] = myfont
    LpGBT2_button_array2[i].grid(column=2, row=i+1)

### Refresh Button ###
GPIO_refresh_button = tk.Button(tab8, text="Refresh")#, command=button_functions.LpGBTread)
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

Connect_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="Connect", 
    command=lambda: button_functions.Connect(Connect_button, EnableGPIO_button, EnableAtoD_button, Bread_button, 
    DIRread_button, DATAOUTread_button, IDread_button, GPIOon_button, GPIOset_button, 
    GPIOclr_button, GPIOoff_button, output_textbox, 1, GBT_SCA4_button_array, GBT_SCA4_button_array2))
Connect_button['font'] = myfont
Connect_button.grid(column=0, row=1)

EnableGPIO_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="EnableGPIO", 
    command=lambda: button_functions.EnableGPIO(EnableGPIO_button, output_textbox, 1))
EnableGPIO_button['font'] = myfont
EnableGPIO_button.grid(column=1, row=1)

EnableAtoD_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="EnableAtoD", 
    command=lambda: button_functions.EnableAtoD(EnableAtoD_button, output_textbox, 1))
EnableAtoD_button['font'] = myfont
EnableAtoD_button.grid(column=2,row=1)

Bread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="Bread", 
    command=lambda: button_functions.Bread(Bread_button, Bread_label, output_textbox, 1))
Bread_button['font'] = myfont
Bread_button.grid(column=0, row=3)

Bread_label = tk.Label(GBT_SCA4_scripts_frame, text="Bread output")
Bread_label['font'] = myfont
Bread_label.grid(column=1, row=3)

DIRread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="DIRread", 
    command=lambda: button_functions.DIRread(DIRread_button, DIRread_label, output_textbox, 1))
DIRread_button['font'] = myfont
DIRread_button.grid(column=0,row=4)

DIRread_label = tk.Label(GBT_SCA4_scripts_frame, text="DIRread output")
DIRread_label['font'] = myfont
DIRread_label.grid(column=1, row=4)

DATAOUTread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="DATAOUTread", 
    command=lambda: button_functions.DATAOUTread(DATAOUTread_button, DATAOUTread_label, output_textbox, 1))
DATAOUTread_button['font'] = myfont
DATAOUTread_button.grid(column=0,row=5)

DATAOUTread_label = tk.Label(GBT_SCA4_scripts_frame, text="DATAOUTread output")
DATAOUTread_label['font'] = myfont
DATAOUTread_label.grid(column=1, row=5)

IDread_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="IDread", 
    command=lambda: button_functions.IDread(IDread_button, IDread_label, output_textbox, 1))
IDread_button['font'] = myfont
IDread_button.grid(column=0,row=2)

IDread_label = tk.Label(GBT_SCA4_scripts_frame, text="IDread output")
IDread_label['font'] = myfont
IDread_label.grid(column=1, row=2)

GPIO_label = tk.Label(GBT_SCA4_scripts_frame, text="enter GPIO value:")
GPIO_label['font'] = myfont
GPIO_label.grid(column=0, row=6)

GPIO_entry = tk.Entry(GBT_SCA4_scripts_frame, width=20, font=("Helvetica","12"))
GPIO_entry.grid(column=1, row=6)

GPIO_enter = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIO enter", command=lambda: button_functions.GPIOenter)
GPIO_enter['font'] = myfont
GPIO_enter.grid(column=2, row=6)

GPIOon_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOon", 
    command=lambda: button_functions.GPIOon(GPIO_entry.get(), GPIOon_button, output_textbox, 1))
GPIOon_button['font'] = myfont
GPIOon_button.grid(column=0, row=7)

GPIOset_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOset", 
    command=lambda: button_functions.GPIOset(GPIO_entry.get(), GPIOset_button, output_textbox, 1))
GPIOset_button['font'] = myfont
GPIOset_button.grid(column=1, row=7)

GPIOclr_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOclr", 
    command=lambda: button_functions.GPIOclr(GPIO_entry.get(), GPIOclr_button, output_textbox, 1))
GPIOclr_button['font'] = myfont
GPIOclr_button.grid(column=2, row=7)

GPIOoff_button = tk.Button(GBT_SCA4_scripts_frame, bg="white", text="GPIOoff", 
    command=lambda: button_functions.GPIOoff(GPIO_entry.get(), GPIOoff_button, output_textbox, 1))
GPIOoff_button['font'] = myfont
GPIOoff_button.grid(column=3, row=7)

error_entry = tk.Entry(GBT_SCA4_scripts_frame, width=20, font=("Helvetica","12"))
error_entry.grid(column=4, row=1)
error_entry.insert(tk.END, "error output")

#####################################################################
### IC1D GBT-SCA ###
IC1D_scripts_label = tk.Label(GBT_SCA1_scripts_frame, text="IC1D GBT-SCA")
IC1D_scripts_label['font'] = myfont
IC1D_scripts_label.grid(column=0, row=0)

Connect_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="Connect",
    command=lambda: button_functions.Connect(Connect_button2, EnableGPIO_button2, EnableAtoD_button2, Bread_button2, 
    DIRread_button2, DATAOUTread_button2, IDread_button2, GPIOon_button2, GPIOset_button2, 
    GPIOclr_button2, GPIOoff_button2, output_textbox, 2, GBT_SCA1_button_array, GBT_SCA1_button_array2))
Connect_button2['font'] = myfont
Connect_button2.grid(column=0, row=1)

EnableGPIO_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="EnableGPIO",
    command=lambda: button_functions.EnableGPIO(EnableGPIO_button2, output_textbox, 2))
EnableGPIO_button2['font'] = myfont
EnableGPIO_button2.grid(column=1, row=1)

EnableAtoD_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="EnableAtoD", 
    command=lambda: button_functions.EnableAtoD(EnableAtoD_button2, output_textbox, 2))
EnableAtoD_button2['font'] = myfont
EnableAtoD_button2.grid(column=2,row=1)

Bread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="Bread",
    command=lambda: button_functions.Bread(Bread_button2, Bread_label2, output_textbox, 2))
Bread_button2['font'] = myfont
Bread_button2.grid(column=0, row=3)

Bread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="Bread output")
Bread_label2['font'] = myfont
Bread_label2.grid(column=1, row=3)

DIRread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="DIRread", 
    command=lambda: button_functions.DIRread(DIRread_button2, DIRread_label2, output_textbox, 2))
DIRread_button2['font'] = myfont
DIRread_button2.grid(column=0,row=4)

DIRread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="DIRread output")
DIRread_label2['font'] = myfont
DIRread_label2.grid(column=1, row=4)

DATAOUTread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="DATAOUTread", 
    command=lambda: button_functions.DATAOUTread(DATAOUTread_button2, DATAOUTread_label2, output_textbox, 2))
DATAOUTread_button2['font'] = myfont
DATAOUTread_button2.grid(column=0,row=5)

DATAOUTread_label2 = tk.Label(GBT_SCA1_scripts_frame, text="DATAOUTread output")
DATAOUTread_label2['font'] = myfont
DATAOUTread_label2.grid(column=1, row=5)

IDread_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="IDread", 
    command=lambda: button_functions.IDread(IDread_button2, IDread_label2, output_textbox, 2))
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

GPIOon_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOon", 
    command=lambda: button_functions.GPIOon(GPIO_entry.get(), GPIOon_button, output_textbox, 2))
GPIOon_button2['font'] = myfont
GPIOon_button2.grid(column=0, row=7)

GPIOset_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOset", 
    command=lambda: button_functions.GPIOset(GPIO_entry.get(), GPIOset_button, output_textbox, 2))
GPIOset_button2['font'] = myfont
GPIOset_button2.grid(column=1, row=7)

GPIOclr_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOclr", 
    command=lambda: button_functions.GPIOclr(GPIO_entry.get(), GPIOclr_button, output_textbox, 2))
GPIOclr_button2['font'] = myfont
GPIOclr_button2.grid(column=2, row=7)

GPIOoff_button2 = tk.Button(GBT_SCA1_scripts_frame, bg="white", text="GPIOoff", 
    command=lambda: button_functions.GPIOoff(GPIO_entry.get(), GPIOoff_button, output_textbox, 2))
GPIOoff_button2['font'] = myfont
GPIOoff_button2.grid(column=3, row=7)

error_entry2 = tk.Entry(GBT_SCA1_scripts_frame, width=20, font=("Helvetica","12"))
error_entry2.grid(column=4, row=1)
error_entry2.insert(tk.END, "error output")

### Output Textbox ###
output_textbox = tk.Text(tab2, font=("Helvetica","12"))
output_textbox.place(x=0, y=525, height=340, width=900)

#####################################################################

main_notebook.pack(expand = 1, fill = "both")

root.mainloop()
