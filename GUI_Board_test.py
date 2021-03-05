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

def assign_address():                   #Assigns address
    TxValue = address.get()             #Get User input address
    print int(TxValue, 0)               #Convert hex into int
    print "write address =", TxValue

def button_assign():                    #Assign address by pushing button
    TxValue = 0x10001001                #Address for specific button
    print int(TxValue)
    print "write address =", hex(TxValue)


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

# Create Frame for Address Entry
frame3 = tk.Frame(window)
frame3.pack(side=tk.LEFT)

label2 = tk.Label(master=frame3, text="Typer Address (hex)")
label2.pack(side=tk.TOP)

address = tk.Entry(master=frame3, width = 20)
address.pack(side=tk.TOP)

enter1 = tk.Button(                     
    master=frame3,
    text="Enter Address",
    command=assign_address
)
enter1.pack(side=tk.TOP)

#Create Frame for hard coded Address
frame4 = tk.Frame(window)
frame4.pack(side=tk.LEFT)

label3 = tk.Label(master=frame4, text="Push Button Address")
label3.pack(side=tk.TOP)

enter2 = tk.Button(                   
    master=frame4,
    text="Set Address",
    command=button_assign
)
enter2.pack(side=tk.TOP)

window.mainloop()