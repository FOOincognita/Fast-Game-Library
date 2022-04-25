from decimal import InvalidOperation
from os import _exit, system 
from time import sleep
from Library import Library
from utils import EmptyEntry, InvalidSelection
from colorama import init, Fore as fg, Back as bg, Style as st

sinp = lambda x: str(input(x))
redtxt = lambda x: st.BRIGHT + fg.RED + str(x) + st.RESET_ALL
ylwtxt = lambda x: st.BRIGHT + fg.YELLOW + str(x) + st.RESET_ALL
cyntxt = lambda x: st.BRIGHT + fg.CYAN + str(x) + st.RESET_ALL
grntxt = lambda x: st.BRIGHT + fg.GREEN + str(x) + st.RESET_ALL

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    system('cls||clear')
    
def safeExit():
    clear()
    print(grntxt("Saving"), end="")
    for i in range(3):
        print(grntxt("."), end="")
        sleep(1)
    sleep(1)
    print(grntxt("\nGoodbye!"))
    sleep(2)
    clear()
    exit()
    
def invalidSel(n ,e):
    clear()
    print(redtxt(f"\n[ERROR-0{str(n)}]: {str(e)} IS AN INVALID SELECTION\n") + ylwtxt("Please make a selection between 1 & 8"))
    sleep(6)
    clear()
    
def unknownExcept(n, e):
    clear()
    print(redtxt(f"\n[ERROR-0{str(n)}]: UNEXPECTED EXCEPTION RAISED IN GameLib.py\n{e}"))
    sleep(6)
    clear()
    return

######### Main ##########
lib = Library(10)
sel = 0

if __name__ == "__main__":
    clear()
    user = sinp(cyntxt("Howdy! What is your name?\n"))
    print(cyntxt(f"Welcome to The Game Library, {user}!"))
    sleep(2)
    clear()
    
    while T:
        try: sel = Library.promptMainMenu()
        except InvalidSelection as e: invalidSel(1,e)
        except Exception as e: unknownExcept(2,e)
        else:
            try:
                match (sel):
                    case 0: raise InvalidOperation(redtxt("case 0 matched"))
                    case 1: lib.search()
                    case 2: lib.addGame()
                    case 3: lib.delGame()
                    case 4: lib.instructions()
                    case 5: lib.printLib()
                    case 6: lib.resetLib()
                    case 7: lib.importGames()
                    case 8: lib.saveAndExit()
            except SystemExit: safeExit()
            except Exception as e: unknownExcept(3,e)
            finally: clear()
            
                
    
    
