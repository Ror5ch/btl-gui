import sys # For sys.argv and sys.exit
import random # For randint
import uhal
import time
#import Tkinter as tk    #Not needed here

def Init_EC_IC_moduls(sentarg):
    if sentarg == 1:
        Init_EC_IC_moduls = hw.getNode("A2")
        return Init_EC_IC_moduls
    elif sentarg == 2:
        Init_EC_IC_moduls = hw.getNode("A2_2")
        return Init_EC_IC_moduls

#####################################################################
def EC_Tx_Elink_Header(sentarg):
    if sentarg == 1:
        EC_Tx_Elink_Header = hw.getNode("EC_Tx_Elink_Header")
        return EC_Tx_Elink_Header
    elif sentarg == 2:
        EC_Tx_Elink_Header = hw.getNode("EC_Tx_Elink_Header_2")
        return EC_Tx_Elink_Header

#####################################################################
def EC_Tx_SCA_Header(sentarg):
    if sentarg == 1:
        EC_Tx_SCA_Header = hw.getNode("EC_Tx_SCA_Header")
        return EC_Tx_SCA_Header
    elif sentarg == 2:
        EC_Tx_SCA_Header = hw.getNode("EC_Tx_SCA_Header_2")
        return EC_Tx_SCA_Header

#####################################################################
def EC_Tx_SCA_Data(sentarg):
    if sentarg == 1:
        EC_Tx_SCA_Data = hw.getNode("EC_Tx_SCA_Data")
        return EC_Tx_SCA_Data
    elif sentarg == 2:
        EC_Tx_SCA_Data = hw.getNode("EC_Tx_SCA_Data_2")
        return EC_Tx_SCA_Data

#####################################################################
def SCA_Rst_CMD(sentarg):
    if sentarg == 1:
        SCA_Rst_CMD = hw.getNode("SCA_Rst_CMD")
        return SCA_Rst_CMD
    elif sentarg == 2:
        SCA_Rst_CMD = hw.getNode("SCA_Rst_CMD_2")
        return SCA_Rst_CMD

#####################################################################
def SCA_Connect_CMD(sentarg):
    if sentarg == 1:
        SCA_Connect_CMD = hw.getNode("SCA_Connect_CMD")
        return SCA_Connect_CMD
    elif sentarg == 2:
        SCA_Connect_CMD = hw.getNode("SCA_Connect_CMD_2")
        return SCA_Connect_CMD

#####################################################################
def SCA_Test_CMD(sentarg):
    if sentarg == 1:
        SCA_Test_CMD = hw.getNode("SCA_Test_CMD")
        return SCA_Test_CMD
    elif sentarg == 2:
        SCA_Test_CMD = hw.getNode("SCA_Test_CMD_2")
        return SCA_Test_CMD

#####################################################################
def SCA_Start_CMD(sentarg):
    if sentarg == 1:
        SCA_Start_CMD = hw.getNode("SCA_Start_CMD")
        return SCA_Start_CMD
    elif sentarg == 2:
        SCA_Start_CMD = hw.getNode("SCA_Start_CMD_2")
        return SCA_Start_CMD

#####################################################################
def nFRAME(sentarg):
    if sentarg == 1:
        nFRAME = hw.getNode("nFRAME")
        return nFRAME
    elif sentarg == 2:
        nFRAME = hw.getNode("nFRAME_2")
        return nFRAME

#####################################################################
def EC_Rx_SCA_Header(sentarg):
    if sentarg == 1:
        EC_Rx_SCA_Header = hw.getNode("EC_Rx_SCA_Header")
        return EC_Rx_SCA_Header
    elif sentarg == 2:
        EC_Rx_SCA_Header = hw.getNode("EC_Rx_SCA_Header_2")
        return EC_Rx_SCA_Header

#####################################################################
def EC_Rx_SCA_Data(sentarg):
    if sentarg == 1:
        EC_Rx_SCA_Data = hw.getNode("EC_Rx_SCA_Data")
        return EC_Rx_SCA_Data
    elif sentarg == 2:
        EC_Rx_SCA_Data = hw.getNode("EC_Rx_SCA_Data_2")
        return EC_Rx_SCA_Data

#####################################################################