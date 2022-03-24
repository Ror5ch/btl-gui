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
from GUI_global import *

############################################################
### Sending GPIO argument ###
############################################################
def GPIOenter():
    sendarg = GPIO_entry.get()
    output_textbox.insert(tk.END, "\n " + sendarg)
    sendarg = int(sendarg, 0)

############################################################
### SCA Functions and Checks ###
############################################################
### Scripts tab specific functions ###
def Connect(Connect_button, EnableGPIO_button, EnableAtoD_button, Bread_button, DIRread_button,
    DATAOUTread_button, IDread_button, GPIOon_button, GPIOset_button, GPIOclr_button, GPIOoff_button,
    output_textbox, GBT_SCA_num, GBT_SCA_button_array, GBT_SCA_button_array2):
    check = SCA_functions.Connect(output_textbox, GBT_SCA_num)
    if check:
        Connect_button.configure(bg="green")
        EnableGPIO_button.configure(bg="white")
        EnableAtoD_button.configure(bg="white")
        Bread_button.configure(bg="white")
        DIRread_button.configure(bg="white")
        DATAOUTread_button.configure(bg="white")
        IDread_button.configure(bg="white")
        GPIOon_button.configure(bg="white")
        GPIOset_button.configure(bg="white")
        GPIOclr_button.configure(bg="white")
        GPIOoff_button.configure(bg="white")
	for i in range(len(GBT_SCA_button_array)):
		GBT_SCA_button_array[i].configure(bg="white")
	for i in range(len(GBT_SCA_button_array2)):
		GBT_SCA_button_array2[i].configure(bg="white")
    else:
        Connect_button.configure(bg="red")

def EnableGPIO(EnableGPIO_button, output_textbox, GBT_SCA_num):
    check = SCA_functions.EnableGPIO(output_textbox, GBT_SCA_num)
    if check:
        EnableGPIO_button.configure(bg="green")
    else:
        EnableGPIO_button.configure(bg="red")

def EnableAtoD(EnableAtoD_button, output_textbox, GBT_SCA_num):
    check = SCA_functions.EnableAtoD(output_textbox, GBT_SCA_num)
    if check:
        EnableAtoD_button.configure(bg="green")
    else:
        EnableAtoD_button.configure(bg="red")

def IDread(IDread_button, IDread_label, output_textbox, GBT_SCA_num):
    check = SCA_functions.IDread(IDread_label, output_textbox, GBT_SCA_num)
    if check:
        IDread_button.configure(bg="green")
    else:
        IDread_button.configure(bg="red")

def Bread(Bread_button, Bread_label, output_textbox, GBT_SCA_num):
    check = SCA_functions.Bread(Bread_label, output_textbox, GBT_SCA_num)
    if check:
        Bread_button.configure(bg="green")
    else:
        Bread_button.configure(bg="red")

def DIRread(DIRread_button, DIRread_label, output_textbox, GBT_SCA_num):
    check = SCA_functions.DIRread(DIRread_label, output_textbox, GBT_SCA_num)
    if check:
        DIRread_button.configure(bg="green")
    else:
        DIRread_button.configure(bg="red")

def DATAOUTread(DATAOUTread_button, DATAOUTread_label, output_textbox, GBT_SCA_num):
    check = SCA_functions.DATAOUTread(DATAOUTread_label, output_textbox, GBT_SCA_num)
    if check:
        DATAOUTread_button.configure(bg="green")
    else:
        DATAOUTread_button.configure(bg="red")

def GPIOon(value, GPIOon_button, output_textbox, GBT_SCA_num):
    output_textbox.insert(tk.END, "\n " + value)
    value = int(value, 0)
    check = SCA_functions.GPIOon(value, output_textbox, GBT_SCA_num)
    if check:
        GPIOon_button.configure(bg="green")
    else:
        GPIOon_button.configure(bg="red")

def GPIOset(value, GPIOset_button, output_textbox, GBT_SCA_num):
    output_textbox.insert(tk.END, "\n " + value)
    value = int(value, 0)    
    check = SCA_functions.GPIOset(value, output_textbox, GBT_SCA_num)
    if check:
        GPIOset_button.configure(bg="green")
    else:
        GPIOset_button.configure(bg="red")

def GPIOclr(value, GPIOclr_button, output_textbox, GBT_SCA_num):
    output_textbox.insert(tk.END, "\n " + value)
    value = int(value, 0)
    check = SCA_functions.GPIOclr(value, output_textbox, GBT_SCA_num)
    if check:
        GPIOclr_button.configure(bg="green")
    else:
        GPIOclr_button.configure(bg="red")

def GPIOoff(value, GPIOoff_button, output_textbox, GBT_SCA_num):
    output_textbox.insert(tk.END, "\n " + value)
    value = int(value, 0)
    check = SCA_functions.GPIOoff(value, output_textbox, GBT_SCA_num)
    if check:
        GPIOoff_button.configure(bg="green")
    else:
        GPIOoff_button.configure(bg="red")

### GPIO tab specific functions ###
def GPIOon_off_button(NewValue, i, output_textbox, GBT_SCA_num):
    Button = GBT_SCA4_button_array[i]
    if GBT_SCA_num == 2:
        Button = GBT_SCA1_button_array[i]
    
    if Button.cget('bg') == "white" or Button.cget('bg') == "red":    #Off state to on or bad to on
        check = SCA_functions.GPIOon(NewValue,output_textbox, GBT_SCA_num)
        if check:
            Button.configure(bg="green")
        else:
            Button.configure(bg="red")                          
    elif Button.cget('bg') == "green":  #On state to turn off
        check = SCA_functions.GPIOoff(NewValue, output_textbox, GBT_SCA_num)
        if check:
            Button.configure(bg="white")
        else:
            Button.configure(bg="red")                         

def GPIOset_clr_button(NewValue, i, output_textbox, GBT_SCA_num):
    Button = GBT_SCA4_button_array2[i]
    if GBT_SCA_num == 2:
        Button = GBT_SCA1_button_array2[i]
    if Button.cget('bg') == "white" or Button.cget('bg') == "red":    #Clr state to Set
        check = SCA_functions.GPIOset(NewValue, output_textbox, GBT_SCA_num)
        if check:
            Button.configure(bg="green")
        else:
            Button.configure(bg="red")                        
    elif Button.cget('bg') == "green":  #Set state to Clr
        check = SCA_functions.GPIOclr(NewValue, output_textbox, GBT_SCA_num)
        if check:
            Button.configure(bg="white")
        else:
            Button.configure(bg="red")

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
    elif Button.cget('bg') == "green":  #On state to turn off
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

### Analog IO tab specific functions ###
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
            calc_value_output = str(calc_value) + "A"
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
            calc_value_output = str(calc_value) + "A"
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

### Temp Calculations Array ###
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
