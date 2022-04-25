from decimal import InvalidOperation
from os import system 
from time import sleep
from Library import Library
from utils import InvalidSelection
from colorama import Fore as fg, Back as bg, Style as st

sinp = lambda x: str(input(str(x)))
rtxt = lambda x: st.BRIGHT + fg.RED + str(x) + st.RESET_ALL
ytxt = lambda x: st.BRIGHT + fg.YELLOW + str(x) + st.RESET_ALL
ctxt = lambda x: st.BRIGHT + fg.CYAN + str(x) + st.RESET_ALL
gtxt = lambda x: st.BRIGHT + fg.GREEN + str(x) + st.RESET_ALL
mtxt = lambda x: st.BRIGHT + fg.MAGENTA + str(x) + st.RESET_ALL
cPrint = lambda x: print(ctxt(str(x)))
rPrint = lambda x: print(rtxt(str(x)))
gPrint = lambda x: print(gtxt(str(x)))
yPrint = lambda x: print(ytxt(str(x)))
mPrint = lambda x: print(mtxt(str(x)))
csinp = lambda x: str(input(ctxt(str(x))))
rsinp = lambda x: str(input(rtxt(str(x))))
ysinp = lambda x: str(input(ytxt(str(x))))
gsinp = lambda x: str(input(gtxt(str(x))))
msinp = lambda x: str(input(mtxt(str(x))))

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    system('cls||clear')
    
def safeExit():
    clear()
    print(gtxt("Saving"), end="")
    for i in range(3):
        print(gtxt("."), end="")
        sleep(1)
    gPrint("\nGoodbye!")
    sleep(2)
    clear()
    exit()
    
# Prints invalid selection error to user, returns to main screen
def invalidSel(n ,e):
    clear()
    print(rtxt(f"\n[ERROR-0{str(n)}]: {str(e)} IS AN INVALID SELECTION\n") + ytxt("Please make a selection between 1 & 8"))
    sleep(6)
    clear()
     
# Prints unknown exception
def unknownExcept(n, e):
    clear()
    rPrint(f"\n[ERROR-0{str(n)}]: UNEXPECTED EXCEPTION RAISED IN GameLib.py\n{e}")
    sleep(6)
    clear()
    return

# Formats name (First, Middle, & Last) to have capital first letter, lowercase remaining
def formName(name):
    form = ""
    for n in name.split(" "):
        if not n.isalpha(): raise Exception
        form += n[0].upper() + n[1:].lower() + " " 
    return form[:-1]

######### Main ##########
lib = Library(10)
sel = 0

if __name__ == "__main__":
    clear()
    user = csinp("Howdy! What is your name?\n")
    try:
        cPrint(f"Welcome to The Game Library, {formName(user)}!")
    except:
        cPrint(f"Welcome to The Game Library, {user}!")
        sleep(1)
        print(mtxt("You have an interesting name"), end="")
        sleep(1)
        for i in range(3):
            print(mtxt("."), end="")
            sleep(1)
    finally:
        sleep(3)
        clear()
    
    while T:
        try: sel = Library.promptMainMenu()
        except InvalidSelection as e: invalidSel(0,e)
        except Exception as e: unknownExcept(1,e)
        else:
            try:
                match (sel):
                    case 0: raise InvalidOperation(rtxt("case 0 matched"))
                    case 1: lib.search()
                    case 2: lib.addGame()
                    case 3: lib.delGame()
                    case 4: lib.instructions()
                    case 5: lib.printLib()
                    case 6: lib.resetLib()
                    case 7: lib.importGames()
                    case 8: lib.saveAndExit()
            except SystemExit: safeExit()
            except Exception as e: unknownExcept(2,e)
            finally: clear()
            
                
    
    
