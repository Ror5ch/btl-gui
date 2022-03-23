import sys # For sys.argv and sys.exit
sys.path.append('/opt/rh/python210/root/usr/lib64/python2.10/lib-tk')
import Tkinter as tk
import ttk as ttk
import os
import tkFont as font
import subprocess
###imports for SCA###
import random # For randint
import uhal
import time
###import functions###
import SCA_functions
import GUI_global as Gg

############################################################
### Sending GPIO argument ###
############################################################
def GPIOenter():
    sendarg = Gg.GPIO_entry.get()
    output_textbox.insert(tk.END, "\n " + sendarg)
    sendarg = int(sendarg, 0)

############################################################
### SCA Functions and Checks ###
############################################################
### Scripts tab specific functions ###
### GBT-SCA4 ###
def Connect():
    check = SCA_functions.Connect(1)
    if check:
        # reset script button colors and label text
        Gg.Connect_button.configure(bg="green")
        Gg.EnableGPIO_button.configure(bg="white")
        Gg.EnableAtoD_button.configure(bg="white")
        Gg.Bread_button.configure(bg="white")
        Gg.DIRread_button.configure(bg="white")
        Gg.DATAOUTread_button.configure(bg="white")
        Gg.IDread_button.configure(bg="white")
        Gg.GPIOon_button.configure(bg="white")
        Gg.GPIOset_button.configure(bg="white")
        Gg.GPIOclr_button.configure(bg="white")
        Gg.GPIOoff_button.configure(bg="white")

        Gg.Bread_label.configure(text="Bread output")
        Gg.DIRread_label.configure(text="DIRread output")
        Gg.DATAOUTread_label.configure(text="DATAOUTread output")
        Gg.IDread_label.configure(text="IDread output")
        # reset GPIO GBT-SCA button colors
	    for i in range(len(Gg.GBT_SCA4_button_array)):
		    Gg.GBT_SCA4_button_array[i].configure(bg="white")
	    for i in range(len(Gg.GBT_SCA4_button_array2)):
		    Gg.GBT_SCA4_button_array2[i].configure(bg="white")
        # reset Analog IO label text
        for i in range(len())
    else:
        Gg.Connect_button.configure(bg="red")

def EnableGPIO():
    check = SCA_functions.EnableGPIO(1)
    if check:
        Gg.EnableGPIO_button.configure(bg="green")
    else:
        Gg.EnableGPIO_button.configure(bg="red")

def EnableAtoD():
    check = SCA_functions.EnableAtoD(1)
    if check:
        Gg.EnableAtoD_button.configure(bg="green")
    else:
        Gg.EnableAtoD_button.configure(bg="red")

def IDread():
    check = SCA_functions.IDread(1)
    if check:
        Gg.IDread_button.configure(bg="green")
    else:
        Gg.IDread_button.configure(bg="red")

def Bread():
    check = SCA_functions.Bread(1)
    if check:
        Gg.Bread_button.configure(bg="green")
    else:
        Gg.Bread_button.configure(bg="red")

def DIRread():
    check = SCA_functions.DIRread(1)
    if check:
        Gg.DIRread_button.configure(bg="green")
    else:
        Gg.DIRread_button.configure(bg="red")

def DATAOUTread():
    check = SCA_functions.DATAOUTread(1)
    if check:
        Gg.DATAOUTread_button.configure(bg="green")
    else:
        Gg.DATAOUTread_button.configure(bg="red")

def GPIOon():
    entry = Gg.GPIO_entry.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)
    check = SCA_functions.GPIOon(value, 1)
    if check:
        Gg.GPIOon_button.configure(bg="green")
    else:
        Gg.GPIOon_button.configure(bg="red")

def GPIOset():
    entry = Gg.GPIO_entry.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)   
    check = SCA_functions.GPIOset(value, 1)
    if check:
        Gg.GPIOset_button.configure(bg="green")
    else:
        Gg.GPIOset_button.configure(bg="red")

def GPIOclr():
    entry = Gg.GPIO_entry.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)
    check = SCA_functions.GPIOclr(value, 1)
    if check:
        Gg.GPIOclr_button.configure(bg="green")
    else:
        Gg.GPIOclr_button.configure(bg="red")

def GPIOoff():
    entry = Gg.GPIO_entry.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)
    check = SCA_functions.GPIOoff(value, 1)
    if check:
        Gg.GPIOoff_button.configure(bg="green")
    else:
        Gg.GPIOoff_button.configure(bg="red")

### GBT-SCA1 ###
def Connect2():
    check = SCA_functions.Connect(2)
    if check:
        Gg.Connect_button2.configure(bg="green")
        Gg.EnableGPIO_button2.configure(bg="white")
        Gg.EnableAtoD_button2.configure(bg="white")
        Gg.Bread_button2.configure(bg="white")
        Gg.DIRread_button2.configure(bg="white")
        Gg.DATAOUTread_button2.configure(bg="white")
        Gg.IDread_button2.configure(bg="white")
        Gg.GPIOon_button2.configure(bg="white")
        Gg.GPIOset_button2.configure(bg="white")
        Gg.GPIOclr_button2.configure(bg="white")
        Gg.GPIOoff_button2.configure(bg="white")

        Gg.Bread_label2.configure(text="Bread output")
        Gg.DIRread_label2.configure(text="DIRread output")
        Gg.DATAOUTread_label2.configure(text="DATAOUTread output")
        Gg.IDread_label2.configure(text="IDread output")
	    for i in range(len(Gg.GBT_SCA1_button_array)):
		    Gg.GBT_SCA1_button_array[i].configure(bg="white")
	    for i in range(len(Gg.GBT_SCA1_button_array2)):
		    Gg.GBT_SCA1_button_array2[i].configure(bg="white")
    else:
        Gg.Connect_button2.configure(bg="red")

def EnableGPIO2():
    check = SCA_functions.EnableGPIO(2)
    if check:
        Gg.EnableGPIO_button2.configure(bg="green")
    else:
        Gg.EnableGPIO_button2.configure(bg="red")

def EnableAtoD2():
    check = SCA_functions.EnableAtoD(2)
    if check:
        Gg.EnableAtoD_button2.configure(bg="green")
    else:
        Gg.EnableAtoD_button2.configure(bg="red")

def IDread2():
    check = SCA_functions.IDread(2)
    if check:
        Gg.IDread_button2.configure(bg="green")
    else:
        Gg.IDread_button2.configure(bg="red")

def Bread2():
    check = SCA_functions.Bread(2)
    if check:
        Gg.Bread_button2.configure(bg="green")
    else:
        Gg.Bread_button2.configure(bg="red")

def DIRread2():
    check = SCA_functions.DIRread(2)
    if check:
        Gg.DIRread_button2.configure(bg="green")
    else:
        Gg.DIRread_button2.configure(bg="red")

def DATAOUTread2():
    check = SCA_functions.DATAOUTread(2)
    if check:
        Gg.DATAOUTread_button2.configure(bg="green")
    else:
        Gg.DATAOUTread_button2.configure(bg="red")

def GPIOon2():
    entry = Gg.GPIO_entry2.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)
    check = SCA_functions.GPIOon(value, 2)
    if check:
        Gg.GPIOon_button2.configure(bg="green")
    else:
        Gg.GPIOon_button2.configure(bg="red")

def GPIOset2():
    entry = Gg.GPIO_entry2.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)   
    check = SCA_functions.GPIOset(value, 2)
    if check:
        Gg.GPIOset_button2.configure(bg="green")
    else:
        Gg.GPIOset_button2.configure(bg="red")

def GPIOclr2():
    entry = Gg.GPIO_entry2.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)
    check = SCA_functions.GPIOclr(value, 2)
    if check:
        Gg.GPIOclr_button2.configure(bg="green")
    else:
        Gg.GPIOclr_button2.configure(bg="red")

def GPIOoff2():
    entry = Gg.GPIO_entry2.get()
    Gg.output_textbox.insert(tk.END, "\n " + entry)
    value = int(entry, 0)
    check = SCA_functions.GPIOoff(value, 2)
    if check:
        Gg.GPIOoff_button2.configure(bg="green")
    else:
        Gg.GPIOoff_button2.configure(bg="red")

#################################################################################
### GPIO tab specific functions #################################################
#################################################################################
def FE9_ALDO_Enable2_onoff4():
    if Gg.FE9_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE9_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000001, 1)
        if check:
            Gg.FE9_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE9_ALDO_En2_onoff_button4.configure(bg="red")
    elif Gg.FE9_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000001, 1)
        if check:
            Gg.FE9_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE9_ALDO_En2_onoff_button4.configure(bg="red")

def FE9_ALDO_Enable1_onoff4():
    if Gg.FE9_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE9_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000002, 1)
        if check:
            Gg.FE9_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE9_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE9_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000002, 1)
        if check:
            Gg.FE9_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE9_ALDO_En1_onoff_button4.configure(bg="red")

def PCC_B_EN_IV8_1_onoff4():
    if Gg.PCC_B_EN_IV8_1_onoff_button4.cget('bg') == "white" or Gg.PCC_B_EN_IV8_1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000004, 1)
        if check:
            Gg.PCC_B_EN_IV8_1_onoff_button4.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_1_onoff_button4.configure(bg="red")                          
    elif Gg.PCC_B_EN_IV8_1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000004, 1)
        if check:
            Gg.PCC_B_EN_IV8_1_onoff_button4.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_1_onoff_button4.configure(bg="red")

def PCC_B_EN_IV8_2_onoff4():
    if Gg.PCC_B_EN_IV8_2_onoff_button4.cget('bg') == "white" or Gg.PCC_B_EN_IV8_2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000008, 1)
        if check:
            Gg.PCC_B_EN_IV8_2_onoff_button4.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_2_onoff_button4.configure(bg="red")                          
    elif Gg.PCC_B_EN_IV8_2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000008, 1)
        if check:
            Gg.PCC_B_EN_IV8_2_onoff_button4.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_2_onoff_button4.configure(bg="red")

def cSS_B_onoff4():
    if Gg.cSS_B_onoff_button4.cget('bg') == "white" or Gg.cSS_B_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000010, 1)
        if check:
            Gg.cSS_B_onoff_button4.configure(bg="green")
        else:
            Gg.cSS_B_onoff_button4.configure(bg="red")                          
    elif Gg.cSS_B_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000010, 1)
        if check:
            Gg.cSS_B_onoff_button4.configure(bg="white")
        else:
            Gg.cSS_B_onoff_button4.configure(bg="red")

def FE10_ALDO_Enable1_onoff4():
    if Gg.FE10_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE10_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000020, 1)
        if check:
            Gg.FE10_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE10_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE10_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000020, 1)
        if check:
            Gg.FE10_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE10_ALDO_En1_onoff_button4.configure(bg="red")

def FE10_ALDO_Enable2_onoff4():
    if Gg.FE10_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE10_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000040, 1)
        if check:
            Gg.FE10_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE10_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE10_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000040, 1)
        if check:
            Gg.FE10_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE10_ALDO_En2_onoff_button4.configure(bg="red")

def cEN_B_onoff4():
    if Gg.cEN_B_onoff_button4.cget('bg') == "white" or Gg.cEN_B_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000080, 1)
        if check:
            Gg.cEN_B_onoff_button4.configure(bg="green")
        else:
            Gg.cEN_B_onoff_button4.configure(bg="red")                          
    elif Gg.cEN_B_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000080, 1)
        if check:
            Gg.cEN_B_onoff_button4.configure(bg="white")
        else:
            Gg.cEN_B_onoff_button4.configure(bg="red")

def FE7_ALDO_Enable1_onoff4():
    if Gg.FE7_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE7_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000100, 1)
        if check:
            Gg.FE7_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE7_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE7_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000100, 1)
        if check:
            Gg.FE7_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE7_ALDO_En1_onoff_button4.configure(bg="red")

def FE7_ALDO_Enable2_onoff4():
    if Gg.FE7_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE7_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000200, 1)
        if check:
            Gg.FE7_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE7_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE7_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000200, 1)
        if check:
            Gg.FE7_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE7_ALDO_En2_onoff_button4.configure(bg="red")

def eSS_B_onoff4():
    if Gg.eSS_B_onoff_button4.cget('bg') == "white" or Gg.eSS_B_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000400, 1)
        if check:
            Gg.eSS_B_onoff_button4.configure(bg="green")
        else:
            Gg.eSS_B_onoff_button4.configure(bg="red")                          
    elif Gg.eSS_B_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000400, 1)
        if check:
            Gg.eSS_B_onoff_button4.configure(bg="white")
        else:
            Gg.eSS_B_onoff_button4.configure(bg="red")

def FE3_ALDO_Enable1_onoff4():
    if Gg.FE3_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE3_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000800, 1)
        if check:
            Gg.FE3_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE3_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE3_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000800, 1)
        if check:
            Gg.FE3_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE3_ALDO_En1_onoff_button4.configure(bg="red")

def FE5_ALDO_Enable1_onoff4():
    if Gg.FE5_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE5_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00001000, 1)
        if check:
            Gg.FE5_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE5_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE5_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00001000, 1)
        if check:
            Gg.FE5_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE5_ALDO_En1_onoff_button4.configure(bg="red")

def oEN_B_onoff4():
    if Gg.oEN_B_onoff_button4.cget('bg') == "white" or Gg.oEN_B_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00002000, 1)
        if check:
            Gg.oEN_B_onoff_button4.configure(bg="green")
        else:
            Gg.oEN_B_onoff_button4.configure(bg="red")                          
    elif Gg.oEN_B_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00002000, 1)
        if check:
            Gg.oEN_B_onoff_button4.configure(bg="white")
        else:
            Gg.oEN_B_onoff_button4.configure(bg="red")

def FE6_ALDO_Enable1_onoff4():
    if Gg.FE6_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE6_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00004000, 1)
        if check:
            Gg.FE6_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE6_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE6_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00004000, 1)
        if check:
            Gg.FE6_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE6_ALDO_En1_onoff_button4.configure(bg="red")

def FE6_ALDO_Enable2_onoff4():
    if Gg.FE6_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE6_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00008000, 1)
        if check:
            Gg.FE6_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE6_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE6_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00008000, 1)
        if check:
            Gg.FE6_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE6_ALDO_En2_onoff_button4.configure(bg="red")

def FE12_ALDO_Enable2_onoff4():
    if Gg.FE12_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE12_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00010000, 1)
        if check:
            Gg.FE12_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE12_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE12_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00010000, 1)
        if check:
            Gg.FE12_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE12_ALDO_En2_onoff_button4.configure(bg="red")

def FE3_ALDO_Enable2_onoff4():
    if Gg.FE3_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE3_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00020000, 1)
        if check:
            Gg.FE3_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE3_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE3_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00020000, 1)
        if check:
            Gg.FE3_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE3_ALDO_En2_onoff_button4.configure(bg="red")

def FE4_ALDO_Enable2_onoff4():
    if Gg.FE4_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE4_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00040000, 1)
        if check:
            Gg.FE4_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE4_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE4_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00040000, 1)
        if check:
            Gg.FE4_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE4_ALDO_En2_onoff_button4.configure(bg="red")

def FE12_ALDO_Enable1_onoff4():
    if Gg.FE12_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE12_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00080000, 1)
        if check:
            Gg.FE12_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE12_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE12_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00080000, 1)
        if check:
            Gg.FE12_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE12_ALDO_En1_onoff_button4.configure(bg="red")

def PCC_A_EN_IV8_2_onoff4():
    if Gg.PCC_A_EN_IV8_2_onoff_button4.cget('bg') == "white" or Gg.PCC_A_EN_IV8_2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00100000, 1)
        if check:
            Gg.PCC_A_EN_IV8_2_onoff_button4.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_2_onoff_button4.configure(bg="red")                          
    elif Gg.PCC_A_EN_IV8_2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00100000, 1)
        if check:
            Gg.PCC_A_EN_IV8_2_onoff_button4.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_2_onoff_button4.configure(bg="red")

def PCC_A_EN_IV8_1_onoff4():
    if Gg.PCC_A_EN_IV8_1_onoff_button4.cget('bg') == "white" or Gg.PCC_A_EN_IV8_1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00200000, 1)
        if check:
            Gg.PCC_A_EN_IV8_1_onoff_button4.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_1_onoff_button4.configure(bg="red")                          
    elif Gg.PCC_A_EN_IV8_1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00200000, 1)
        if check:
            Gg.PCC_A_EN_IV8_1_onoff_button4.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_1_onoff_button4.configure(bg="red")

def FE11_ALDO_Enable1_onoff4():
    if Gg.FE11_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE11_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00400000, 1)
        if check:
            Gg.FE11_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE11_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE11_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00400000, 1)
        if check:
            Gg.FE11_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE11_ALDO_En1_onoff_button4.configure(bg="red")

def FE2_ALDO_Enable1_onoff4():
    if Gg.FE2_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE2_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00800000, 1)
        if check:
            Gg.FE2_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE2_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE2_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00800000, 1)
        if check:
            Gg.FE2_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE2_ALDO_En1_onoff_button4.configure(bg="red")

def FE4_ALDO_Enable1_onoff4():
    if Gg.FE4_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE4_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x01000000, 1)
        if check:
            Gg.FE4_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE4_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE4_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x01000000, 1)
        if check:
            Gg.FE4_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE4_ALDO_En1_onoff_button4.configure(bg="red")

def FE11_ALDO_Enable2_onoff4():
    if Gg.FE11_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE11_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x02000000, 1)
        if check:
            Gg.FE11_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE11_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE11_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x02000000, 1)
        if check:
            Gg.FE11_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE11_ALDO_En2_onoff_button4.configure(bg="red")

def FE2_ALDO_Enable2_onoff4():
    if Gg.FE2_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE2_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x04000000, 1)
        if check:
            Gg.FE2_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE2_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE2_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x04000000, 1)
        if check:
            Gg.FE2_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE2_ALDO_En2_onoff_button4.configure(bg="red")

def FE1_ALDO_Enable1_onoff4():
    if Gg.FE1_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE1_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x08000000, 1)
        if check:
            Gg.FE1_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE1_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE1_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x08000000, 1)
        if check:
            Gg.FE1_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE1_ALDO_En1_onoff_button4.configure(bg="red")

def FE5_ALDO_Enable2_onoff4():
    if Gg.FE5_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE5_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x10000000, 1)
        if check:
            Gg.FE5_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE5_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE5_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x10000000, 1)
        if check:
            Gg.FE5_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE5_ALDO_En2_onoff_button4.configure(bg="red")

def FE1_ALDO_Enable2_onoff4():
    if Gg.FE1_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE1_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x20000000, 1)
        if check:
            Gg.FE1_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE1_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE1_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x20000000, 1)
        if check:
            Gg.FE1_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE1_ALDO_En2_onoff_button4.configure(bg="red")

def FE8_ALDO_Enable1_onoff4():
    if Gg.FE8_ALDO_En1_onoff_button4.cget('bg') == "white" or Gg.FE8_ALDO_En1_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x40000000, 1)
        if check:
            Gg.FE8_ALDO_En1_onoff_button4.configure(bg="green")
        else:
            Gg.FE8_ALDO_En1_onoff_button4.configure(bg="red")                          
    elif Gg.FE8_ALDO_En1_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x40000000, 1)
        if check:
            Gg.FE8_ALDO_En1_onoff_button4.configure(bg="white")
        else:
            Gg.FE8_ALDO_En1_onoff_button4.configure(bg="red")

def FE8_ALDO_Enable2_onoff4():
    if Gg.FE8_ALDO_En2_onoff_button4.cget('bg') == "white" or Gg.FE8_ALDO_En2_onoff_button4.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x80000000, 1)
        if check:
            Gg.FE8_ALDO_En2_onoff_button4.configure(bg="green")
        else:
            Gg.FE8_ALDO_En2_onoff_button4.configure(bg="red")                          
    elif Gg.FE8_ALDO_En2_onoff_button4.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x80000000, 1)
        if check:
            Gg.FE8_ALDO_En2_onoff_button4.configure(bg="white")
        else:
            Gg.FE8_ALDO_En2_onoff_button4.configure(bg="red")

def FE9_ALDO_Enable2_setclr4():
    if Gg.FE9_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE9_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000001, 1)
        if check:
            Gg.FE9_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE9_ALDO_En2_setclr_button4.configure(bg="red")
    elif Gg.FE9_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000001, 1)
        if check:
            Gg.FE9_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE9_ALDO_En2_setclr_button4.configure(bg="red")

def FE9_ALDO_Enable1_setclr4():
    if Gg.FE9_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE9_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000002, 1)
        if check:
            Gg.FE9_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE9_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE9_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000002, 1)
        if check:
            Gg.FE9_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE9_ALDO_En1_setclr_button4.configure(bg="red")

def PCC_B_EN_IV8_1_setclr4():
    if Gg.PCC_B_EN_IV8_1_setclr_button4.cget('bg') == "white" or Gg.PCC_B_EN_IV8_1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000004, 1)
        if check:
            Gg.PCC_B_EN_IV8_1_setclr_button4.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_1_setclr_button4.configure(bg="red")                          
    elif Gg.PCC_B_EN_IV8_1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000004, 1)
        if check:
            Gg.PCC_B_EN_IV8_1_setclr_button4.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_1_setclr_button4.configure(bg="red")

def PCC_B_EN_IV8_2_setclr4():
    if Gg.PCC_B_EN_IV8_2_setclr_button4.cget('bg') == "white" or Gg.PCC_B_EN_IV8_2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000008, 1)
        if check:
            Gg.PCC_B_EN_IV8_2_setclr_button4.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_2_setclr_button4.configure(bg="red")                          
    elif Gg.PCC_B_EN_IV8_2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000008, 1)
        if check:
            Gg.PCC_B_EN_IV8_2_setclr_button4.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_2_setclr_button4.configure(bg="red")

def cSS_B_setclr4():
    if Gg.cSS_B_setclr_button4.cget('bg') == "white" or Gg.cSS_B_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000010, 1)
        if check:
            Gg.cSS_B_setclr_button4.configure(bg="green")
        else:
            Gg.cSS_B_setclr_button4.configure(bg="red")                          
    elif Gg.cSS_B_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000010, 1)
        if check:
            Gg.cSS_B_setclr_button4.configure(bg="white")
        else:
            Gg.cSS_B_setclr_button4.configure(bg="red")

def FE10_ALDO_Enable1_setclr4():
    if Gg.FE10_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE10_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000020, 1)
        if check:
            Gg.FE10_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE10_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE10_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000020, 1)
        if check:
            Gg.FE10_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE10_ALDO_En1_setclr_button4.configure(bg="red")

def FE10_ALDO_Enable2_setclr4():
    if Gg.FE10_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE10_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000040, 1)
        if check:
            Gg.FE10_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE10_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE10_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000040, 1)
        if check:
            Gg.FE10_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE10_ALDO_En2_setclr_button4.configure(bg="red")

def cEN_B_setclr4():
    if Gg.cEN_B_setclr_button4.cget('bg') == "white" or Gg.cEN_B_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000080, 1)
        if check:
            Gg.cEN_B_setclr_button4.configure(bg="green")
        else:
            Gg.cEN_B_setclr_button4.configure(bg="red")                          
    elif Gg.cEN_B_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000080, 1)
        if check:
            Gg.cEN_B_setclr_button4.configure(bg="white")
        else:
            Gg.cEN_B_setclr_button4.configure(bg="red")

def FE7_ALDO_Enable1_setclr4():
    if Gg.FE7_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE7_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000100, 1)
        if check:
            Gg.FE7_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE7_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE7_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000100, 1)
        if check:
            Gg.FE7_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE7_ALDO_En1_setclr_button4.configure(bg="red")

def FE7_ALDO_Enable2_setclr4():
    if Gg.FE7_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE7_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000200, 1)
        if check:
            Gg.FE7_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE7_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE7_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000200, 1)
        if check:
            Gg.FE7_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE7_ALDO_En2_setclr_button4.configure(bg="red")

def eSS_B_setclr4():
    if Gg.eSS_B_setclr_button4.cget('bg') == "white" or Gg.eSS_B_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000400, 1)
        if check:
            Gg.eSS_B_setclr_button4.configure(bg="green")
        else:
            Gg.eSS_B_setclr_button4.configure(bg="red")                          
    elif Gg.eSS_B_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000400, 1)
        if check:
            Gg.eSS_B_setclr_button4.configure(bg="white")
        else:
            Gg.eSS_B_setclr_button4.configure(bg="red")

def FE3_ALDO_Enable1_setclr4():
    if Gg.FE3_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE3_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000800, 1)
        if check:
            Gg.FE3_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE3_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE3_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000800, 1)
        if check:
            Gg.FE3_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE3_ALDO_En1_setclr_button4.configure(bg="red")

def FE5_ALDO_Enable1_setclr4():
    if Gg.FE5_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE5_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00001000, 1)
        if check:
            Gg.FE5_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE5_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE5_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00001000, 1)
        if check:
            Gg.FE5_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE5_ALDO_En1_setclr_button4.configure(bg="red")

def oEN_B_setclr4():
    if Gg.oEN_B_setclr_button4.cget('bg') == "white" or Gg.oEN_B_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00002000, 1)
        if check:
            Gg.oEN_B_setclr_button4.configure(bg="green")
        else:
            Gg.oEN_B_setclr_button4.configure(bg="red")                          
    elif Gg.oEN_B_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00002000, 1)
        if check:
            Gg.oEN_B_setclr_button4.configure(bg="white")
        else:
            Gg.oEN_B_setclr_button4.configure(bg="red")

def FE6_ALDO_Enable1_setclr4():
    if Gg.FE6_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE6_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00004000, 1)
        if check:
            Gg.FE6_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE6_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE6_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00004000, 1)
        if check:
            Gg.FE6_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE6_ALDO_En1_setclr_button4.configure(bg="red")

def FE6_ALDO_Enable2_setclr4():
    if Gg.FE6_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE6_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00008000, 1)
        if check:
            Gg.FE6_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE6_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE6_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00008000, 1)
        if check:
            Gg.FE6_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE6_ALDO_En2_setclr_button4.configure(bg="red")

def FE12_ALDO_Enable2_setclr4():
    if Gg.FE12_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE12_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00010000, 1)
        if check:
            Gg.FE12_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE12_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE12_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00010000, 1)
        if check:
            Gg.FE12_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE12_ALDO_En2_setclr_button4.configure(bg="red")

def FE3_ALDO_Enable2_setclr4():
    if Gg.FE3_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE3_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00020000, 1)
        if check:
            Gg.FE3_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE3_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE3_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00020000, 1)
        if check:
            Gg.FE3_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE3_ALDO_En2_setclr_button4.configure(bg="red")

def FE4_ALDO_Enable2_setclr4():
    if Gg.FE4_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE4_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00040000, 1)
        if check:
            Gg.FE4_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE4_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE4_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00040000, 1)
        if check:
            Gg.FE4_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE4_ALDO_En2_setclr_button4.configure(bg="red")

def FE12_ALDO_Enable1_setclr4():
    if Gg.FE12_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE12_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00080000, 1)
        if check:
            Gg.FE12_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE12_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE12_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00080000, 1)
        if check:
            Gg.FE12_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE12_ALDO_En1_setclr_button4.configure(bg="red")

def PCC_A_EN_IV8_2_setclr4():
    if Gg.PCC_A_EN_IV8_2_setclr_button4.cget('bg') == "white" or Gg.PCC_A_EN_IV8_2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00100000, 1)
        if check:
            Gg.PCC_A_EN_IV8_2_setclr_button4.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_2_setclr_button4.configure(bg="red")                          
    elif Gg.PCC_A_EN_IV8_2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00100000, 1)
        if check:
            Gg.PCC_A_EN_IV8_2_setclr_button4.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_2_setclr_button4.configure(bg="red")

def PCC_A_EN_IV8_1_setclr4():
    if Gg.PCC_A_EN_IV8_1_setclr_button4.cget('bg') == "white" or Gg.PCC_A_EN_IV8_1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00200000, 1)
        if check:
            Gg.PCC_A_EN_IV8_1_setclr_button4.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_1_setclr_button4.configure(bg="red")                          
    elif Gg.PCC_A_EN_IV8_1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00200000, 1)
        if check:
            Gg.PCC_A_EN_IV8_1_setclr_button4.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_1_setclr_button4.configure(bg="red")

def FE11_ALDO_Enable1_setclr4():
    if Gg.FE11_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE11_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00400000, 1)
        if check:
            Gg.FE11_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE11_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE11_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00400000, 1)
        if check:
            Gg.FE11_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE11_ALDO_En1_setclr_button4.configure(bg="red")

def FE2_ALDO_Enable1_setclr4():
    if Gg.FE2_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE2_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00800000, 1)
        if check:
            Gg.FE2_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE2_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE2_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00800000, 1)
        if check:
            Gg.FE2_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE2_ALDO_En1_setclr_button4.configure(bg="red")

def FE4_ALDO_Enable1_setclr4():
    if Gg.FE4_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE4_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x01000000, 1)
        if check:
            Gg.FE4_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE4_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE4_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x01000000, 1)
        if check:
            Gg.FE4_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE4_ALDO_En1_setclr_button4.configure(bg="red")

def FE11_ALDO_Enable2_setclr4():
    if Gg.FE11_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE11_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x02000000, 1)
        if check:
            Gg.FE11_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE11_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE11_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x02000000, 1)
        if check:
            Gg.FE11_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE11_ALDO_En2_setclr_button4.configure(bg="red")

def FE2_ALDO_Enable2_setclr4():
    if Gg.FE2_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE2_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x04000000, 1)
        if check:
            Gg.FE2_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE2_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE2_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x04000000, 1)
        if check:
            Gg.FE2_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE2_ALDO_En2_setclr_button4.configure(bg="red")

def FE1_ALDO_Enable1_setclr4():
    if Gg.FE1_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE1_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x08000000, 1)
        if check:
            Gg.FE1_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE1_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE1_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x08000000, 1)
        if check:
            Gg.FE1_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE1_ALDO_En1_setclr_button4.configure(bg="red")

def FE5_ALDO_Enable2_setclr4():
    if Gg.FE5_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE5_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x10000000, 1)
        if check:
            Gg.FE5_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE5_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE5_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x10000000, 1)
        if check:
            Gg.FE5_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE5_ALDO_En2_setclr_button4.configure(bg="red")

def FE1_ALDO_Enable2_setclr4():
    if Gg.FE1_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE1_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x20000000, 1)
        if check:
            Gg.FE1_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE1_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE1_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x20000000, 1)
        if check:
            Gg.FE1_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE1_ALDO_En2_setclr_button4.configure(bg="red")

def FE8_ALDO_Enable1_setclr4():
    if Gg.FE8_ALDO_En1_setclr_button4.cget('bg') == "white" or Gg.FE8_ALDO_En1_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x40000000, 1)
        if check:
            Gg.FE8_ALDO_En1_setclr_button4.configure(bg="green")
        else:
            Gg.FE8_ALDO_En1_setclr_button4.configure(bg="red")                          
    elif Gg.FE8_ALDO_En1_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x40000000, 1)
        if check:
            Gg.FE8_ALDO_En1_setclr_button4.configure(bg="white")
        else:
            Gg.FE8_ALDO_En1_setclr_button4.configure(bg="red")

def FE8_ALDO_Enable2_setclr4():
    if Gg.FE8_ALDO_En2_setclr_button4.cget('bg') == "white" or Gg.FE8_ALDO_En2_setclr_button4.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x80000000, 1)
        if check:
            Gg.FE8_ALDO_En2_setclr_button4.configure(bg="green")
        else:
            Gg.FE8_ALDO_En2_setclr_button4.configure(bg="red")                          
    elif Gg.FE8_ALDO_En2_setclr_button4.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x80000000, 1)
        if check:
            Gg.FE8_ALDO_En2_setclr_button4.configure(bg="white")
        else:
            Gg.FE8_ALDO_En2_setclr_button4.configure(bg="red")










def FE2_ALDO_Enable2_onoff1():
    if Gg.FE2_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE2_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000001, 2)
        if check:
            Gg.FE2_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE2_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE2_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000001, 2)
        if check:
            Gg.FE2_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE2_ALDO_En2_onoff_button1.configure(bg="red")

def FE5_ALDO_Enable2_onoff1():
    if Gg.FE5_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE5_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000002, 2)
        if check:
            Gg.FE5_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE5_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE5_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000002, 2)
        if check:
            Gg.FE5_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE5_ALDO_En2_onoff_button1.configure(bg="red")

def FE8_ALDO_Enable2_onoff1():
    if Gg.FE8_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE8_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000004, 2)
        if check:
            Gg.FE8_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE8_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE8_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000004, 2)
        if check:
            Gg.FE8_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE8_ALDO_En2_onoff_button1.configure(bg="red")

def FE8_ALDO_Enable1_onoff1():
    if Gg.FE8_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE8_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000008, 2)
        if check:
            Gg.FE8_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE8_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE8_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000008, 2)
        if check:
            Gg.FE8_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE8_ALDO_En1_onoff_button1.configure(bg="red")

def FE11_ALDO_Enable2_onoff1():
    if Gg.FE11_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE11_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000010, 2)
        if check:
            Gg.FE11_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE11_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE11_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000010, 2)
        if check:
            Gg.FE11_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE11_ALDO_En2_onoff_button1.configure(bg="red")

def FE1_ALDO_Enable2_onoff1():
    if Gg.FE1_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE1_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000020, 2)
        if check:
            Gg.FE1_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE1_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE1_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000020, 2)
        if check:
            Gg.FE1_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE1_ALDO_En2_onoff_button1.configure(bg="red")

def FE1_ALDO_Enable1_onoff1():
    if Gg.FE1_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE1_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000040, 2)
        if check:
            Gg.FE1_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE1_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE1_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000040, 2)
        if check:
            Gg.FE1_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE1_ALDO_En1_onoff_button1.configure(bg="red")

def FE11_ALDO_Enable1_onoff1():
    if Gg.FE11_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE11_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000080, 2)
        if check:
            Gg.FE11_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE11_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE11_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000080, 2)
        if check:
            Gg.FE11_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE11_ALDO_En1_onoff_button1.configure(bg="red")

def FE2_ALDO_Enable1_onoff1():
    if Gg.FE2_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE2_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000100, 2)
        if check:
            Gg.FE2_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE2_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE2_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000100, 2)
        if check:
            Gg.FE2_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE2_ALDO_En1_onoff_button1.configure(bg="red")

def FE4_ALDO_Enable1_onoff1():
    if Gg.FE4_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE4_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000200, 2)
        if check:
            Gg.FE4_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE4_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE4_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000200, 2)
        if check:
            Gg.FE4_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE4_ALDO_En1_onoff_button1.configure(bg="red")

def FE12_ALDO_Enable1_onoff1():
    if Gg.FE12_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE12_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000400, 2)
        if check:
            Gg.FE12_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE12_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE12_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000400, 2)
        if check:
            Gg.FE12_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE12_ALDO_En1_onoff_button1.configure(bg="red")

def PCC_A_EN_IV8_2_onoff1():
    if Gg.PCC_A_EN_IV8_2_onoff_button1.cget('bg') == "white" or Gg.PCC_A_EN_IV8_2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00000800, 2)
        if check:
            Gg.PCC_A_EN_IV8_2_onoff_button1.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_2_onoff_button1.configure(bg="red")
    elif Gg.PCC_A_EN_IV8_2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00000800,2)
        if check:
            Gg.PCC_A_EN_IV8_2_onoff_button1.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_2_onoff_button1.configure(bg="red")

def PCC_A_EN_IV8_1_onoff1():
    if Gg.PCC_A_EN_IV8_1_onoff_button1.cget('bg') == "white" or Gg.PCC_A_EN_IV8_1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00001000, 2)
        if check:
            Gg.PCC_A_EN_IV8_1_onoff_button1.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_1_onoff_button1.configure(bg="red")
    elif Gg.PCC_A_EN_IV8_1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00001000,2)
        if check:
            Gg.PCC_A_EN_IV8_1_onoff_button1.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_1_onoff_button1.configure(bg="red")

def FE12_ALDO_Enable2_onoff1():
    if Gg.FE12_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE12_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00002000, 2)
        if check:
            Gg.FE12_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE12_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE12_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00002000, 2)
        if check:
            Gg.FE12_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE12_ALDO_En2_onoff_button1.configure(bg="red")

def FE3_ALDO_Enable2_onoff1():
    if Gg.FE3_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE3_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00004000, 2)
        if check:
            Gg.FE3_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE3_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE3_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00004000, 2)
        if check:
            Gg.FE3_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE3_ALDO_En2_onoff_button1.configure(bg="red")

def FE4_ALDO_Enable2_onoff1():
    if Gg.FE4_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE4_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00008000, 2)
        if check:
            Gg.FE4_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE4_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE4_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00008000, 2)
        if check:
            Gg.FE4_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE4_ALDO_En2_onoff_button1.configure(bg="red")

def oEN_A_onoff1():
    if Gg.oEN_A_onoff_button1.cget('bg') == "white" or Gg.oEN_A_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00010000, 2)
        if check:
            Gg.oEN_A_onoff_button1.configure(bg="green")
        else:
            Gg.oEN_A_onoff_button1.configure(bg="red")
    elif Gg.oEN_A_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00010000, 2)
        if check:
            Gg.oEN_A_onoff_button1.configure(bg="white")
        else:
            Gg.oEN_A_onoff_button1.configure(bg="red")

def FE6_ALDO_Enable1_onoff1():
    if Gg.FE6_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE6_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00020000, 2)
        if check:
            Gg.FE6_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE6_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE6_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00020000, 2)
        if check:
            Gg.FE6_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE6_ALDO_En1_onoff_button1.configure(bg="red")

def FE6_ALDO_Enable2_onoff1():
    if Gg.FE6_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE6_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00040000, 2)
        if check:
            Gg.FE6_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE6_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE6_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00040000, 2)
        if check:
            Gg.FE6_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE6_ALDO_En2_onoff_button1.configure(bg="red")

def eSS_A_onoff1():
    if Gg.eSS_A_onoff_button1.cget('bg') == "white" or Gg.eSS_A_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00080000, 2)
        if check:
            Gg.eSS_A_onoff_button1.configure(bg="green")
        else:
            Gg.eSS_A_onoff_button1.configure(bg="red")
    elif Gg.eSS_A_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00080000, 2)
        if check:
            Gg.eSS_A_onoff_button1.configure(bg="white")
        else:
            Gg.eSS_A_onoff_button1.configure(bg="red")

def FE3_ALDO_Enable1_onoff1():
    if Gg.FE3_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE3_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00100000, 2)
        if check:
            Gg.FE3_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE3_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE3_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00100000, 2)
        if check:
            Gg.FE3_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE3_ALDO_En1_onoff_button1.configure(bg="red")

def FE5_ALDO_Enable1_onoff1():
    if Gg.FE5_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE5_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00200000, 2)
        if check:
            Gg.FE5_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE5_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE5_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00200000, 2)
        if check:
            Gg.FE5_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE5_ALDO_En1_onoff_button1.configure(bg="red")

def cEN_A_onoff1():
    if Gg.cEN_A_onoff_button1.cget('bg') == "white" or Gg.cEN_A_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00400000, 2)
        if check:
            Gg.cEN_A_onoff_button1.configure(bg="green")
        else:
            Gg.cEN_A_onoff_button1.configure(bg="red")
    elif Gg.cEN_A_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00400000, 2)
        if check:
            Gg.cEN_A_onoff_button1.configure(bg="white")
        else:
            Gg.cEN_A_onoff_button1.configure(bg="red")

def FE7_ALDO_Enable1_onoff1():
    if Gg.FE7_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE7_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x00800000, 2)
        if check:
            Gg.FE7_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE7_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE7_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x00800000, 2)
        if check:
            Gg.FE7_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE7_ALDO_En1_onoff_button1.configure(bg="red")

def FE7_ALDO_Enable2_onoff1():
    if Gg.FE7_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE7_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x01000000, 2)
        if check:
            Gg.FE7_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE7_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE7_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x01000000, 2)
        if check:
            Gg.FE7_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE7_ALDO_En2_onoff_button1.configure(bg="red")

def cSS_A_onoff1():
    if Gg.cSS_A_onoff_button1.cget('bg') == "white" or Gg.cSS_A_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x02000000, 2)
        if check:
            Gg.cSS_A_onoff_button1.configure(bg="green")
        else:
            Gg.cSS_A_onoff_button1.configure(bg="red")
    elif Gg.cSS_A_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x02000000, 2)
        if check:
            Gg.cSS_A_onoff_button1.configure(bg="white")
        else:
            Gg.cSS_A_onoff_button1.configure(bg="red")

def FE9_ALDO_Enable2_onoff1():
    if Gg.FE9_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE9_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x04000000, 2)
        if check:
            Gg.FE9_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE9_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE9_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x04000000, 2)
        if check:
            Gg.FE9_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE9_ALDO_En2_onoff_button1.configure(bg="red")

def FE9_ALDO_Enable1_onoff1():
    if Gg.FE9_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE9_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x08000000, 2)
        if check:
            Gg.FE9_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE9_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE9_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x08000000, 2)
        if check:
            Gg.FE9_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE9_ALDO_En1_onoff_button1.configure(bg="red")

def PCC_B_EN_IV8_2_onoff1():
    if Gg.PCC_B_EN_IV8_2_onoff_button1.cget('bg') == "white" or Gg.PCC_B_EN_IV8_2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x10000000, 2)
        if check:
            Gg.PCC_B_EN_IV8_2_onoff_button1.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_2_onoff_button1.configure(bg="red")
    elif Gg.PCC_B_EN_IV8_2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x10000000,2)
        if check:
            Gg.PCC_B_EN_IV8_2_onoff_button1.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_2_onoff_button1.configure(bg="red")

def FE10_ALDO_Enable1_onoff1():
    if Gg.FE10_ALDO_En1_onoff_button1.cget('bg') == "white" or Gg.FE10_ALDO_En1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x20000000, 2)
        if check:
            Gg.FE10_ALDO_En1_onoff_button1.configure(bg="green")
        else:
            Gg.FE10_ALDO_En1_onoff_button1.configure(bg="red")
    elif Gg.FE10_ALDO_En1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x20000000, 2)
        if check:
            Gg.FE10_ALDO_En1_onoff_button1.configure(bg="white")
        else:
            Gg.FE10_ALDO_En1_onoff_button1.configure(bg="red")

def FE10_ALDO_Enable2_onoff1():
    if Gg.FE10_ALDO_En2_onoff_button1.cget('bg') == "white" or Gg.FE10_ALDO_En2_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x40000000, 2)
        if check:
            Gg.FE10_ALDO_En2_onoff_button1.configure(bg="green")
        else:
            Gg.FE10_ALDO_En2_onoff_button1.configure(bg="red")
    elif Gg.FE10_ALDO_En2_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x40000000, 2)
        if check:
            Gg.FE10_ALDO_En2_onoff_button1.configure(bg="white")
        else:
            Gg.FE10_ALDO_En2_onoff_button1.configure(bg="red")

def PCC_B_EN_IV8_1_onoff1():
    if Gg.PCC_B_EN_IV8_1_onoff_button1.cget('bg') == "white" or Gg.PCC_B_EN_IV8_1_onoff_button1.cget('bg') == "red":
        check = SCA_functions.GPIOon(0x80000000, 2)
        if check:
            Gg.PCC_B_EN_IV8_1_onoff_button1.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_1_onoff_button1.configure(bg="red")
    elif Gg.PCC_B_EN_IV8_1_onoff_button1.cget('bg') == "green":
        check = SCA_functions.GPIOoff(0x80000000,2)
        if check:
            Gg.PCC_B_EN_IV8_1_onoff_button1.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_1_onoff_button1.configure(bg="red")

def FE2_ALDO_Enable2_setclr1():
    if Gg.FE2_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE2_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000001, 2)
        if check:
            Gg.FE2_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE2_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE2_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000001, 2)
        if check:
            Gg.FE2_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE2_ALDO_En2_setclr_button1.configure(bg="red")

def FE5_ALDO_Enable2_setclr1():
    if Gg.FE5_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE5_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000002, 2)
        if check:
            Gg.FE5_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE5_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE5_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000002, 2)
        if check:
            Gg.FE5_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE5_ALDO_En2_setclr_button1.configure(bg="red")

def FE8_ALDO_Enable2_setclr1():
    if Gg.FE8_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE8_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000004, 2)
        if check:
            Gg.FE8_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE8_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE8_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000004, 2)
        if check:
            Gg.FE8_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE8_ALDO_En2_setclr_button1.configure(bg="red")

def FE8_ALDO_Enable1_setclr1():
    if Gg.FE8_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE8_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000008, 2)
        if check:
            Gg.FE8_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE8_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE8_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000008, 2)
        if check:
            Gg.FE8_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE8_ALDO_En1_setclr_button1.configure(bg="red")

def FE11_ALDO_Enable2_setclr1():
    if Gg.FE11_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE11_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000010, 2)
        if check:
            Gg.FE11_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE11_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE11_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000010, 2)
        if check:
            Gg.FE11_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE11_ALDO_En2_setclr_button1.configure(bg="red")

def FE1_ALDO_Enable2_setclr1():
    if Gg.FE1_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE1_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000020, 2)
        if check:
            Gg.FE1_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE1_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE1_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000020, 2)
        if check:
            Gg.FE1_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE1_ALDO_En2_setclr_button1.configure(bg="red")

def FE1_ALDO_Enable1_setclr1():
    if Gg.FE1_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE1_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000040, 2)
        if check:
            Gg.FE1_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE1_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE1_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000040, 2)
        if check:
            Gg.FE1_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE1_ALDO_En1_setclr_button1.configure(bg="red")

def FE11_ALDO_Enable1_setclr1():
    if Gg.FE11_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE11_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000080, 2)
        if check:
            Gg.FE11_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE11_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE11_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000080, 2)
        if check:
            Gg.FE11_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE11_ALDO_En1_setclr_button1.configure(bg="red")

def FE2_ALDO_Enable1_setclr1():
    if Gg.FE2_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE2_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000100, 2)
        if check:
            Gg.FE2_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE2_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE2_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000100, 2)
        if check:
            Gg.FE2_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE2_ALDO_En1_setclr_button1.configure(bg="red")

def FE4_ALDO_Enable1_setclr1():
    if Gg.FE4_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE4_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000200, 2)
        if check:
            Gg.FE4_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE4_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE4_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000200, 2)
        if check:
            Gg.FE4_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE4_ALDO_En1_setclr_button1.configure(bg="red")

def FE12_ALDO_Enable1_setclr1():
    if Gg.FE12_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE12_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000400, 2)
        if check:
            Gg.FE12_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE12_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE12_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000400, 2)
        if check:
            Gg.FE12_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE12_ALDO_En1_setclr_button1.configure(bg="red")

def PCC_A_EN_IV8_2_setclr1():
    if Gg.PCC_A_EN_IV8_2_setclr_button1.cget('bg') == "white" or Gg.PCC_A_EN_IV8_2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00000800, 2)
        if check:
            Gg.PCC_A_EN_IV8_2_setclr_button1.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_2_setclr_button1.configure(bg="red")
    elif Gg.PCC_A_EN_IV8_2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00000800,2)
        if check:
            Gg.PCC_A_EN_IV8_2_setclr_button1.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_2_setclr_button1.configure(bg="red")

def PCC_A_EN_IV8_1_setclr1():
    if Gg.PCC_A_EN_IV8_1_setclr_button1.cget('bg') == "white" or Gg.PCC_A_EN_IV8_1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00001000, 2)
        if check:
            Gg.PCC_A_EN_IV8_1_setclr_button1.configure(bg="green")
        else:
            Gg.PCC_A_EN_IV8_1_setclr_button1.configure(bg="red")
    elif Gg.PCC_A_EN_IV8_1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00001000,2)
        if check:
            Gg.PCC_A_EN_IV8_1_setclr_button1.configure(bg="white")
        else:
            Gg.PCC_A_EN_IV8_1_setclr_button1.configure(bg="red")

def FE12_ALDO_Enable2_setclr1():
    if Gg.FE12_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE12_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00002000, 2)
        if check:
            Gg.FE12_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE12_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE12_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00002000, 2)
        if check:
            Gg.FE12_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE12_ALDO_En2_setclr_button1.configure(bg="red")

def FE3_ALDO_Enable2_setclr1():
    if Gg.FE3_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE3_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00004000, 2)
        if check:
            Gg.FE3_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE3_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE3_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00004000, 2)
        if check:
            Gg.FE3_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE3_ALDO_En2_setclr_button1.configure(bg="red")

def FE4_ALDO_Enable2_setclr1():
    if Gg.FE4_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE4_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00008000, 2)
        if check:
            Gg.FE4_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE4_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE4_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00008000, 2)
        if check:
            Gg.FE4_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE4_ALDO_En2_setclr_button1.configure(bg="red")

def oEN_A_setclr1():
    if Gg.oEN_A_setclr_button1.cget('bg') == "white" or Gg.oEN_A_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00010000, 2)
        if check:
            Gg.oEN_A_setclr_button1.configure(bg="green")
        else:
            Gg.oEN_A_setclr_button1.configure(bg="red")
    elif Gg.oEN_A_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00010000, 2)
        if check:
            Gg.oEN_A_setclr_button1.configure(bg="white")
        else:
            Gg.oEN_A_setclr_button1.configure(bg="red")

def FE6_ALDO_Enable1_setclr1():
    if Gg.FE6_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE6_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00020000, 2)
        if check:
            Gg.FE6_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE6_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE6_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00020000, 2)
        if check:
            Gg.FE6_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE6_ALDO_En1_setclr_button1.configure(bg="red")

def FE6_ALDO_Enable2_setclr1():
    if Gg.FE6_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE6_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00040000, 2)
        if check:
            Gg.FE6_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE6_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE6_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00040000, 2)
        if check:
            Gg.FE6_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE6_ALDO_En2_setclr_button1.configure(bg="red")

def eSS_A_setclr1():
    if Gg.eSS_A_setclr_button1.cget('bg') == "white" or Gg.eSS_A_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00080000, 2)
        if check:
            Gg.eSS_A_setclr_button1.configure(bg="green")
        else:
            Gg.eSS_A_setclr_button1.configure(bg="red")
    elif Gg.eSS_A_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00080000, 2)
        if check:
            Gg.eSS_A_setclr_button1.configure(bg="white")
        else:
            Gg.eSS_A_setclr_button1.configure(bg="red")

def FE3_ALDO_Enable1_setclr1():
    if Gg.FE3_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE3_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00100000, 2)
        if check:
            Gg.FE3_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE3_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE3_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00100000, 2)
        if check:
            Gg.FE3_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE3_ALDO_En1_setclr_button1.configure(bg="red")

def FE5_ALDO_Enable1_setclr1():
    if Gg.FE5_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE5_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00200000, 2)
        if check:
            Gg.FE5_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE5_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE5_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00200000, 2)
        if check:
            Gg.FE5_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE5_ALDO_En1_setclr_button1.configure(bg="red")

def cEN_A_setclr1():
    if Gg.cEN_A_setclr_button1.cget('bg') == "white" or Gg.cEN_A_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00400000, 2)
        if check:
            Gg.cEN_A_setclr_button1.configure(bg="green")
        else:
            Gg.cEN_A_setclr_button1.configure(bg="red")
    elif Gg.cEN_A_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00400000, 2)
        if check:
            Gg.cEN_A_setclr_button1.configure(bg="white")
        else:
            Gg.cEN_A_setclr_button1.configure(bg="red")

def FE7_ALDO_Enable1_setclr1():
    if Gg.FE7_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE7_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x00800000, 2)
        if check:
            Gg.FE7_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE7_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE7_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x00800000, 2)
        if check:
            Gg.FE7_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE7_ALDO_En1_setclr_button1.configure(bg="red")

def FE7_ALDO_Enable2_setclr1():
    if Gg.FE7_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE7_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x01000000, 2)
        if check:
            Gg.FE7_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE7_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE7_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x01000000, 2)
        if check:
            Gg.FE7_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE7_ALDO_En2_setclr_button1.configure(bg="red")

def cSS_A_setclr1():
    if Gg.cSS_A_setclr_button1.cget('bg') == "white" or Gg.cSS_A_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x02000000, 2)
        if check:
            Gg.cSS_A_setclr_button1.configure(bg="green")
        else:
            Gg.cSS_A_setclr_button1.configure(bg="red")
    elif Gg.cSS_A_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x02000000, 2)
        if check:
            Gg.cSS_A_setclr_button1.configure(bg="white")
        else:
            Gg.cSS_A_setclr_button1.configure(bg="red")

def FE9_ALDO_Enable2_setclr1():
    if Gg.FE9_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE9_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x04000000, 2)
        if check:
            Gg.FE9_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE9_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE9_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x04000000, 2)
        if check:
            Gg.FE9_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE9_ALDO_En2_setclr_button1.configure(bg="red")

def FE9_ALDO_Enable1_setclr1():
    if Gg.FE9_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE9_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x08000000, 2)
        if check:
            Gg.FE9_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE9_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE9_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x08000000, 2)
        if check:
            Gg.FE9_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE9_ALDO_En1_setclr_button1.configure(bg="red")

def PCC_B_EN_IV8_2_setclr1():
    if Gg.PCC_B_EN_IV8_2_setclr_button1.cget('bg') == "white" or Gg.PCC_B_EN_IV8_2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x10000000, 2)
        if check:
            Gg.PCC_B_EN_IV8_2_setclr_button1.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_2_setclr_button1.configure(bg="red")
    elif Gg.PCC_B_EN_IV8_2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x10000000,2)
        if check:
            Gg.PCC_B_EN_IV8_2_setclr_button1.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_2_setclr_button1.configure(bg="red")

def FE10_ALDO_Enable1_setclr1():
    if Gg.FE10_ALDO_En1_setclr_button1.cget('bg') == "white" or Gg.FE10_ALDO_En1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x20000000, 2)
        if check:
            Gg.FE10_ALDO_En1_setclr_button1.configure(bg="green")
        else:
            Gg.FE10_ALDO_En1_setclr_button1.configure(bg="red")
    elif Gg.FE10_ALDO_En1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x20000000, 2)
        if check:
            Gg.FE10_ALDO_En1_setclr_button1.configure(bg="white")
        else:
            Gg.FE10_ALDO_En1_setclr_button1.configure(bg="red")

def FE10_ALDO_Enable2_setclr1():
    if Gg.FE10_ALDO_En2_setclr_button1.cget('bg') == "white" or Gg.FE10_ALDO_En2_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x40000000, 2)
        if check:
            Gg.FE10_ALDO_En2_setclr_button1.configure(bg="green")
        else:
            Gg.FE10_ALDO_En2_setclr_button1.configure(bg="red")
    elif Gg.FE10_ALDO_En2_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x40000000, 2)
        if check:
            Gg.FE10_ALDO_En2_setclr_button1.configure(bg="white")
        else:
            Gg.FE10_ALDO_En2_setclr_button1.configure(bg="red")

def PCC_B_EN_IV8_1_setclr1():
    if Gg.PCC_B_EN_IV8_1_setclr_button1.cget('bg') == "white" or Gg.PCC_B_EN_IV8_1_setclr_button1.cget('bg') == "red":
        check = SCA_functions.GPIOset(0x80000000, 2)
        if check:
            Gg.PCC_B_EN_IV8_1_setclr_button1.configure(bg="green")
        else:
            Gg.PCC_B_EN_IV8_1_setclr_button1.configure(bg="red")
    elif Gg.PCC_B_EN_IV8_1_setclr_button1.cget('bg') == "green":
        check = SCA_functions.GPIOclr(0x80000000,2)
        if check:
            Gg.PCC_B_EN_IV8_1_setclr_button1.configure(bg="white")
        else:
            Gg.PCC_B_EN_IV8_1_setclr_button1.configure(bg="red")




def LpGBTon_off_button(Button, output_textbox, LpGBT_num, bit_num):
    if Button.cget('bg') == "white" or Button.cget('bg') == "red":    #Off state or bad to on
	    proc = subprocess.Popen(['python3', 'LpGBT_functions.py', 'on', str(LpGBT_num), str(bit_num)], stdout=subprocess.PIPE)
            out_value = str(proc.communicate()[0])
            print out_value
	    out_value = out_value.partition('\n')[0]
	    if out_value == "worked":
	        Button.configure(bg="green")
	    else:
	        Button.configure(bg="red")
    elif Button.cget('bg') == "green":
	    proc = subprocess.Popen(['python3', 'LpGBT_functions.py', 'off', str(LpGBT_num), str(bit_num)], stdout=subprocess.PIPE)
            out_value = str(proc.communicate()[0])
            out_value = out_value.partition('\n')[0]
	    if out_value == "worked":
	        Button.configure(bg="white")
	    else:
	        Button.configure(bg="red")

def LpGBTset_clr_button(Button, output_textbox, LpGBT_num, bit_num):
    if Button.cget('bg') == "white" or Button.cget('bg') == "red":    #Off state or bad to on
	    proc = subprocess.Popen(['python3', 'LpGBT_functions.py', 'set', str(LpGBT_num), str(bit_num)], stdout=subprocess.PIPE)
            out_value = str(proc.communicate()[0])
            out_value = out_value.partition('\n')[0]
	    if out_value == "worked":
	        Button.configure(bg="green")
	    else:
	        Button.configure(bg="red")
    elif Button.cget('bg') == "green":
	    proc = subprocess.Popen(['python3', 'LpGBT_functions.py', 'clr', str(LpGBT_num), str(bit_num)], stdout=subprocess.PIPE)
            out_value = str(proc.communicate()[0])
            out_value = out_value.partition('\n')[0]
	    if out_value == "worked":
	        Button.configure(bg="white")
	    else:
	        Button.configure(bg="red")

#################################################################################
### Analog IO tab specific functions ############################################
#################################################################################
def AnIO_refresh(IC4B_label_array2, IC4B_label_array3, IC1B_label_array2, IC1B_label_array3, output_textbox):
    #IC4B GBT_SCA
    res_array = temps_array()
    
    for i in range(len(IC4B_label_array2)):                         
        value = SCA_functions.SCAADCread(output_textbox, 1, i)
        if i == 24:                                                 #V Bias B mon
	    value1 = str(hex(value))
            IC4B_label_array2[i].configure(text=value1)
	    calc_value = int(value) / float(4096)
            calc_value = calc_value * (80600 + 2000) / 80600
	    calc_value = "{:.3f}".format(calc_value)
            calc_value_output = str(calc_value) + "V"
            IC4B_label_array3[i].configure(text=calc_value_output)
        elif i == 19 or i == 22 or i > 26.5:                        #SIPM Temp
	    value1 = str(hex(value))
            IC4B_label_array2[i].configure(text=value1)
            calc_value0 = int(value) / float(4096)
            calc_value1 = calc_value0 / .0001
            low_res = 602.56
	    high_res = 1385.05
	    low_temp = -100
	    high_temp = 100
            calc_value = (calc_value1 - low_res) / (high_res - low_res) * (high_temp - low_temp) + low_temp 
            for j in range(len(res_array)):
		if j-100 > calc_value:		#array starts at -100 degrees Celsius
			high_temp = j-100
		    	low_temp = j-101
                    	high_res = res_array[j]
		    	low_res = res_array[j-1]
		    	break
            calc_value = (calc_value1 - low_res) / (high_res - low_res) * (high_temp - low_temp) + low_temp
            for k in range(len(res_array)):
                if k-100 > calc_value:
                    high_temp = k-100
		    low_temp = k-101
                    high_res = res_array[k]
		    low_res = res_array[k-1]
		    break
            calc_value = (calc_value1 - low_res) / (high_res - low_res) * (high_temp - low_temp) + low_temp
	    calc_value = "{:.3f}".format(calc_value)
            degree_sign = u'\N{DEGREE SIGN}'
            calc_value_output = str(calc_value) + degree_sign + "C"
            IC4B_label_array3[i].configure(text=calc_value_output)
        else:                                                       # FE Bias
	    value1 = str(hex(value))
            IC4B_label_array2[i].configure(text=value1)
            calc_value = int(value) / float(4096)
            calc_value = calc_value * (59000 + 39200) / 59000
	    calc_value = "{:.3f}".format(calc_value)
            calc_value_output = str(calc_value) + "A"
            IC4B_label_array3[i].configure(text=calc_value_output)

    #IC1B GBT_SCA
    for i in range(len(IC1B_label_array2)):                         
        value = SCA_functions.SCAADCread(output_textbox, 1, i)
        if i == 24:                                                 #V Bias A mon
	    value1 = str(hex(value))
            IC1B_label_array2[i].configure(text=value1)
            calc_value = int(value) / float(4096)
            calc_value = calc_value * (80600 + 2000) / 80600
	    calc_value = "{:.3f}".format(calc_value)
            calc_value_output = str(calc_value) + "V"
            IC1B_label_array3[i].configure(text=calc_value_output)
        elif i == 19 or i == 22 or i > 26.5:                        #SIPM Temp
	    value1 = str(hex(value))
            IC1B_label_array2[i].configure(text=value1)
            calc_value0 = int(value) / float(4096)
            calc_value1 = calc_value0 / .0001
	    low_res = 602.56
	    high_res = 1385.05
	    low_temp = -100
	    high_temp = 100
            calc_value = (calc_value1 - low_res) / (high_res - low_res) * (high_temp - low_temp) + low_temp
            for j in range(len(res_array)):
                if j-100 > calc_value:
                    high_temp = j-100
	            low_temp = j-101
                    high_res = res_array[j]
		    low_res = res_array[j-1]
		    break
            calc_value = (calc_value1 - low_res) / (high_res - low_res) * (high_temp - low_temp) + low_temp
            for k in range(len(res_array)):
                if k-100 > calc_value:
                    high_temp = k-100
		    low_temp = k-101
                    high_res = res_array[k]
		    low_res = res_array[k-1]
		    break
            calc_value = (calc_value1 - low_res) / (high_res - low_res) * (high_temp - low_temp) + low_temp
	    calc_value = "{:.3f}".format(calc_value)
            degree_sign = u'\N{DEGREE SIGN}'
            calc_value_output = str(calc_value) + degree_sign + "C"
            IC1B_label_array3[i].configure(text=calc_value_output)
        else:                                                       # FE Bias
	    value1 = str(hex(value))
            IC1B_label_array2[i].configure(text=value1)
            calc_value = int(value) / float(4096)
            calc_value = calc_value * (59000 + 39200) / 59000
	    calc_value = "{:.3f}".format(calc_value)
            calc_value_output = str(calc_value) + "A"
            IC1B_label_array3[i].configure(text=calc_value_output)

#################################################################################
### Temp Calculations Array #####################################################
#################################################################################
def temps_array():
    # array of resistances at each temperature from -100 to 100 C
    temps_array = [
    602.56, 606.61,	610.66,	614.71,	618.76,	622.80,	626.84,	630.88,	634.92,	638.96,
    643.00, 647.03,	651.06,	655.09,	659.12,	663.15,	667.17,	671.20,	675.22,	679.24,
    683.25, 687.27,	691.29,	695.30,	699.31,	703.32,	707.33,	711.34,	715.34,	719.34,
    723.35, 727.35,	731.34,	735.34,	739.34,	743.33,	747.32,	751.32,	755.30,	759.29,
    763.28, 767.26,	771.25,	775.23,	779.21,	783.19,	787.17,	791.14,	795.12,	799.09,
    803.06, 807.03,	811.00,	814.97,	818.94,	822.90,	826.87,	830.83,	834.79,	838.75,
    842.71, 846.66,	850.62,	854.57,	858.53,	862.48,	866.43,	870.38,	874.33,	878.27,
    882.22, 886.16,	890.10,	894.04,	897.99,	901.92,	905.86,	909.80,	913.73,	917.67,
    921.60, 925.53,	929.46,	933.39,	937.32,	941.24,	945.17,	949.09,	953.02,	956.94,
    960.86, 964.78,	968.70,	972.61,	976.53,	980.44,	984.36,	988.27,	992.18,	996.09,
    1000.00, 1003.91, 1007.81, 1011.72, 1015.62, 1019.53, 1023.43, 1027.33,	1031.23, 1035.13,
    1039.03, 1042.92, 1046.82, 1050.71, 1054.60, 1058.49, 1062.38, 1066.27,	1070.16, 1074.05,
    1077.94, 1081.82, 1085.70, 1089.59, 1093.47, 1097.35, 1101.23, 1105.10,	1108.98, 1112.86,
    1116.73, 1120.60, 1124.47, 1128.35, 1132.21, 1136.08, 1139.95, 1143.82,	1147.68, 1151.55,
    1155.41, 1159.27, 1163.13, 1166.99, 1170.85, 1174.70, 1178.56, 1182.41,	1186.27, 1190.12,
    1193.97, 1197.82, 1201.67, 1205.52, 1209.36, 1213.21, 1217.05, 1220.90,	1224.74, 1228.58,
    1232.42, 1236.26, 1240.09, 1243.93, 1247.77, 1251.60, 1255.43, 1259.26,	1263.09, 1266.92,
    1270.75, 1274.58, 1278.40, 1282.23, 1286.05, 1289.87, 1293.70, 1297.52,	1301.33, 1305.15,
    1308.97, 1312.78, 1316.60, 1320.41, 1324.22, 1328.03, 1331.84, 1335.65,	1339.46, 1343.26,
    1347.07, 1350.87, 1354.68, 1358.48, 1362.28, 1366.08, 1369.87, 1373.67,	1377.47, 1381.26,
    1385.05, 1388.85, 1392.64, 1396.43,	1400.22, 1404.00, 1407.79, 1411.58,	1415.36, 1419.14,
    1422.93, 1426.71, 1430.49, 1434.26,	1438.04, 1441.82, 1445.59, 1449.37,	1453.14, 1456.91,
    1460.68, 1464.45, 1468.22, 1471.98,	1475.75, 1479.51, 1483.28, 1487.04,	1490.80, 1494.56,
    1498.32, 1502.08, 1505.83, 1509.59,	1513.34, 1517.10, 1520.85, 1524.60,	1528.35, 1532.10,
    1535.84, 1539.59, 1543.33, 1547.08,	1550.82, 1554.56, 1558.30, 1562.04,	1565.78, 1569.52,
    1573.25, 1576.99, 1580.72, 1584.45,	1588.18, 1591.91, 1595.64, 1599.37,	1603.09, 1606.82,
    1610.54, 1614.27, 1617.99, 1621.71,	1625.43, 1629.15, 1632.86, 1636.58,	1640.30, 1644.01,
    1647.72, 1651.43, 1655.14, 1658.85,	1662.56, 1666.27, 1669.97, 1673.68,	1677.38, 1681.08,
    1684.78, 1688.48, 1692.18, 1695.88,	1699.58, 1703.27, 1706.96, 1710.66,	1714.35, 1718.04,
    1721.73, 1725.42, 1729.10, 1732.79,	1736.48, 1740.16, 1743.84, 1747.52,	1751.20, 1754.88,
    1758.56, 1762.24, 1765.91, 1769.59,	1773.26, 1776.93, 1780.60, 1784.27,	1787.94, 1791.61,
    1795.28, 1798.94, 1802.60, 1806.27,	1809.93, 1813.59, 1817.25, 1820.91,	1824.56, 1828.22,
    1831.88, 1835.53, 1839.18, 1842.83,	1846.48, 1850.13, 1853.78, 1857.43,	1861.07, 1864.72,
    1868.36, 1872.00, 1875.64, 1879.28,	1882.92, 1886.56, 1890.19, 1893.83,	1897.46, 1901.10,
    1904.73, 1908.36, 1911.99, 1915.62,	1919.24, 1922.87, 1926.49, 1930.12,	1933.74, 1937.36,
    1940.98, 1944.60, 1948.22, 1951.83,	1955.45, 1959.06, 1962.68, 1966.29,	1969.90, 1973.51,
    1977.12, 1980.73, 1984.33, 1987.94,	1991.54, 1995.14, 1998.75, 2002.35,	2005.95, 2009.54,
    2013.14, 2016.74, 2020.33, 2023.93,	2027.52, 2031.11, 2034.70, 2038.29,	2041.88, 2045.46,
    2049.05, 2052.63, 2056.22, 2059.80,	2063.38, 2066.96, 2070.54, 2074.11,	2077.69, 2081.27,
    2084.84, 2088.41, 2091.98, 2095.55,	2099.12, 2102.69, 2106.26, 2109.82,	2113.39, 2116.95,
    2120.52]
    return temps_array
