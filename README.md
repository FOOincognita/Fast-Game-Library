# ENGR102 Final Project: The Fast Game Library (Python 3.10+ Required)
This repository holds all versions of my final project in ENGR-102 (intro Python course). **Check out the manual for more info.**

### Purpose:
**This is a database style library I wrote from scratch which stores 'games' which have 4 string attributes, & stores them within a custom written hashtable, which uses linked lists for collisions. All but 75 lines within the whole project were written by me.**

Library.py:
  - Contains all data structures necessary for program to store & retreieve data fast. 
  - Contains the Library class, which will be used to control every operation within the program.

test_*.py:
  - Any file that starts with "test_" is a unittest file, which is a unit tester for the program to ensure everything works properly with a click of the button.

utils.py:
  - Contains a package manager, which will automatically install any missing libraries from any computer. 
    - You must have PIP installed for this to work.
  - Contains custom exceptions to be thrown within try:except:finally branches.

LibMem.txt:
  - This file contains all game entries & serves as persistent memory for the program. Any persistent memory code or files are **only for testing**, & have not been developed with any standard in mind. All entries are sorted in lexicographical order

GameLib.py:
  - Servers as "main"; user will start program from this file. This file is the "front-end."
