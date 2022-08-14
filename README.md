# ENGR102 Final Project: The Fast Game Library
This repository holds all versions of my final project in ENGR-102 (intro Python course).

### Purpose:
**This is a database style library I wrote from scratch which stores 'games' which have 4 string attributes, & stores them within a custom written hashtable, which uses linked lists for collisions. All but 75 lines within the whole project were written by me.**

Library.py:
  - Contains all data structures necessary for our program to store & retreieve data fast. 
  - Contains the Library class, which will be used to control every operation within the program.
  - You can reference this file when writing your code to see which methods are available to you.

test_*.py:
  - Any file that starts with "test_" is a unittest file, which is a unit tester for our program to ensure everything works properly with a click of the button.

utils.py:
  - Contains a package manager, which will automatically install any missing libraries from your computer. 
    - You must have PIP installed for this to work.
  - Contains custom exceptions to be thrown within try:except:finally branches.

LibMem.txt:
  - This file will contain all game entries & will server as persistent memory for our program (e.i. after shutting the program off, we will be able to reboot it with all the exact same data from before, mimicing a harddrive). Our program will read that file on boot, & write to it on shutdown. The file will be in lexicographical order by title.

GameLib.py:
  - Servers as "main"; user will start program from this file. This file is the "front-end."
