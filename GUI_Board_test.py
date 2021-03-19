import tkinter as tk
import random # For randint
import sys # For sys.argv and sys.exit
import time
from datetime import date
from random import randrange


def gettext():
    today = date.today()                #Get the Date
    d3 = today.strftime("%m/%d/%y")

    text = entry.get()                  #Get what's entered in box to use

    value = randrange(10)               #Do task on Board

    f = open("Board_test.txt","w+")     #Open and write to text file
    f.write("Date: " + d3)
    f.write("\nBoard number: " + text)
    f.write("\nValue: %i" % (value))
    f.close()

def SCAConnect():                       
    TxValue = address.get()             #Get User input address
    print int(TxValue, 16)              #Convert hex into int
    print "write address =", TxValue

def SCAEnableGPIO():                    
    TxValue = address2.get()            #Get User input address
    print int(TxValue, 16)              #Convert hex into int
    print "write address =", TxValue

def SCABread():
    TxValue = address6.get()            #Get User input address
    print int(TxValue, 16)              #Convert hex into int
    print "write address =", TxValue

#######################################################################
window = tk.Tk()

#Create Frame for quit button
frame1 = tk.Frame(window)               
frame1.pack(side=tk.BOTTOM)             

quit = tk.Button(
    master=frame1,
    text="Quit",
    command=quit
)
quit.pack()

#Create Frame for Board ID Entry
frame2 = tk.Frame(window)               
frame2.pack(side=tk.LEFT)

label = tk.Label(master=frame2, text="Board ID Number")
label.pack(side=tk.TOP)

entry = tk.Entry(master=frame2, width = 20)
entry.pack(side=tk.TOP)

enter = tk.Button(
    master=frame2,
    text="Enter Board ID #",
    command=gettext
)
enter.pack(side=tk.TOP)

# Create Frame for SCAConnect
frame3 = tk.Frame(window)
frame3.pack(side=tk.LEFT)

label2 = tk.Label(master=frame3, text="SCAConnect")
label2.pack(side=tk.TOP)

address = tk.Entry(master=frame3, width = 20)
address.pack(side=tk.TOP)

enter1 = tk.Button(                     
    master=frame3,
    text="Run SCAConnect",
    command=SCAConnect
)
enter1.pack(side=tk.TOP)

#Create Frame for SCAEnableGPIO
frame4 = tk.Frame(window)
frame4.pack(side=tk.LEFT)

label3 = tk.Label(master=frame4, text="SCAEnableGPIO")
label3.pack(side=tk.TOP)
label4 = tk.Label(master=frame4, text="Write Control Register B")
label4.pack(side=tk.TOP)

address2 = tk.Entry(master=frame4, width = 20)
address2.pack(side=tk.TOP)

label5 = tk.Label(master=frame4, text="Write Data Field")
label5.pack(side=tk.TOP)

address3 = tk.Entry(master=frame4, width = 20)
address3.pack(side=tk.TOP)

label6 = tk.Label(master=frame4, text="Read Control Register B")
label6.pack(side=tk.TOP)

address4 = tk.Entry(master=frame4, width = 20)
address4.pack(side=tk.TOP)

label7 = tk.Label(master=frame4, text="Read Data Field")
label7.pack(side=tk.TOP)

address5 = tk.Entry(master=frame4, width = 20)
address5.pack(side=tk.TOP)

enter2 = tk.Button(                     
    master=frame4,
    text="Run SCAEnableGPIO",
    command=SCAEnableGPIO
)
enter2.pack(side=tk.TOP)

#Create Frame for SCABread
frame5=tk.Frame(window)
frame5.pack(side=tk.LEFT)

label8 = tk.Label(master=frame5, text="SCABread")
label8.pack(side=tk.TOP)
label9 = tk.Label(master=frame5, text="Read Control Register D")
label9.pack(side=tk.TOP)

address6 = tk.Entry(master=frame5, width = 20)
address6.pack(side=tk.TOP)

label10 = tk.Label(master=frame5, text="Read Data Field")
label10.pack(side=tk.TOP)

address7 = tk.Entry(master=frame5, width = 20)
address7.pack(side=tk.TOP)

enter3 = tk.Button(
    master=frame5,
    text="Run SCABread",
    command=SCABread
)
enter3.pack(side=tk.TOP)

window.mainloop()