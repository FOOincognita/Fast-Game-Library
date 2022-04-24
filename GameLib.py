# This file will act as main()
import os
from time import sleep
from Library import Library

sinp = lambda x: str(input(x))

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')

######### Main ##########

gameLibrary = Library(10)

if __name__ == "__main__":
    user = sinp("Howdy! What is your name?\n")
    print(f"Welcome to the Game Library, {user}!")
    sleep(2)
    
    while T:
        clear()
        Library.promptMainMenu()
        sel = Library.userMenuSel()
        print(sel)
    
        match (sel):
            case 1: gameLibrary.search()
            case 2: gameLibrary.addGame()
            case 3: gameLibrary.delGame()
            case 4: gameLibrary.printLib()
            case 5: gameLibrary.reset()
            case 6: gameLibrary.importGames()
            case 7: gameLibrary.saveAndExit()
    
    
