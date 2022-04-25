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
lib = Library(10)

if __name__ == "__main__":
    user = sinp("Howdy! What is your name?\n")
    print(f"Welcome to The Game Library, {user}!")
    sleep(2)
    
    while T:
        clear()
        sel = Library.promptMainMenu()
    
        match (sel):
            case 1: lib.search()
            case 2: lib.addGame()
            case 3: lib.delGame()
            case 4: lib.instructions()
            case 5: lib.printLib()
            case 6: lib.resetLib()
            case 7: lib.importGames()
            case 8: lib.saveAndExit()
    
    
