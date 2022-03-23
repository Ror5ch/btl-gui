# Command for running GUI:
<details><summary>How to download</summary>

- To use this repo, you must first login to a computer connected to the teststand (remotely via openVPN or in person)
- Go to the directory in which you would like to run this repo from
- Download/update files with the following command sequence:

</details>
Once you are in the directory run:

- python2 GUI_board_test.py

This will bring up the interface for communicating with the teststand

# For editing structure of interface:
GUI_board_test.py

- Has the structure of the tabs in the notebook and the buttons, labels, etc. on each tab
- When a button is pressed, this script calls GUI_button_functions to perform the necessary function(s)

# Functions for color changes to buttons as well as current and temperature calculations and displays
GUI_button_functions.py
- For GPIO tab, this script is notified which function to run from GUI_board_test and sends through info to SCA_functions
- For Analog IO tab, this script is notified to get calculations from GUI_board_test, sends this through to SCA_functions, then calculates temperature or current from SCA_functions result(s)

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
