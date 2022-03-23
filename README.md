# Command for running GUI:
<details><summary>How to download</summary>


- To use this repo, you must first login to a computer connected to the teststand (remotely via openVPN or in person)
- Go to the directory in which you would like to run this repo from
- Download/update files with the following command sequence:

</details>
Once you are in the directory run:

- python2 GUI_board_test.py

This will bring up the interface

# For editing structure of interface:
GUI_board_test.py
- sends information to GUI_button_functions

# Functions for color changes to buttons as well as current and temperature calculations and displays
GUI_button_functions.py
- For GPIO tab, this takes some information from GUI_board_test and sends through to SCA_functions
- For Analog IO tab, this takes some information from GUI_board_test, sends through to SCA_functions, then calculates temperature or current from result

# Functions for sending commands to the board
SCA_functions.py
- Actually communicates with the teststand
- Rewritten from Russell's SCA scripts (one for each of the functions)
- Sends through which GBT_SCA is needed to GUI_getNode_functions to get the needed nodes

# Gets the node for the matching GBT_SCA
GUI_getNode_functions.py
- GBT_SCA4 uses 1
- GBT_SCA1 uses 2

# Communicating with the LpGBTs on the board
LpGBT_functions.py
- This script is in ***** python 3 ******
- 
