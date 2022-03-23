# Command for running GUI:
<details><summary>How to download</summary>

- To use this repo, you must first login to a computer connected to the teststand (remotely via openVPN or in person)
- Go to the directory in which you would like to run from
- Download/update files with the following command sequence:

</details>
Once you are in the directory run:

- python2 GUI_board_test.py

This will bring up the interface for communicating with the teststand

# Global variables
GUI_global.py
- Creates all the variables that are called in multiple scripts/functions but does not define them

# For editing structure of interface:
GUI_board_test.py

- Has the structure of the tabs in the notebook. Also, defines and structures the buttons, labels, etc. on each tab
- When a button is pressed, this script calls GUI_button_functions to perform the necessary function(s)

# Functions for color changes to buttons as well as current and temperature calculations and displays
GUI_button_functions.py
- For GPIO tab, this script is notified which function to run from GUI_board_test and sends through info to SCA_functions
- For Analog IO tab, this script is notified to get calculations from GUI_board_test, sends this through to SCA_functions, then calculates temperature or current from SCA_functions result(s)
- After receiving results from SCA_functions, this tab changes the color or text for a button or label, respectively

# Functions for sending commands to the board
SCA_functions.py
- Actually communicates with the teststand
- Rewritten from Russell's SCA scripts (one for each of the functions)
- Sends through which GBT_SCA is needed to GUI_getNode_functions to get the needed nodes
- Sends results/errors back to GUI_button_functions

# Gets the node for the matching GBT_SCA
GUI_getNode_functions.py

- Receives a GBT-SCA number from SCA_functions then gets the nodes for the corresponding GBT-SCA, the system is as follows:
- GBT_SCA4 uses 1
- GBT_SCA1 uses 2

# Communicating with the LpGBTs on the board
LpGBT_functions.py
- This script is in ***** python 3 ******
- This is script is still in editing and not provided in the repo yet
