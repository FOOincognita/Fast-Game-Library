from decimal import InvalidOperation
from os import system 
from time import sleep
from Library import Library
from utils import InvalidSelection
from colorama import Fore as fg, Back as bg, Style as st

sinp = lambda x: str(input(str(x)))
fgtxt = lambda x,y: st.BRIGHT + x + str(y) + st.RESET_ALL
rtxt = lambda x: fgtxt(fg.RED, x)
ytxt = lambda x: fgtxt(fg.YELLOW, x)
ctxt = lambda x: fgtxt(fg.CYAN, x)
gtxt = lambda x: fgtxt(fg.GREEN, x)
mtxt = lambda x: fgtxt(fg.MAGENTA, x)

cPrint = lambda x: print(ctxt(x))
rPrint = lambda x: print(rtxt(x))
gPrint = lambda x: print(gtxt(x))
yPrint = lambda x: print(ytxt(x))
mPrint = lambda x: print(mtxt(x))

rsinp = lambda x: sinp(rtxt(x))
ysinp = lambda x: sinp(ytxt(x))
csinp = lambda x: sinp(ctxt(x))
gsinp = lambda x: sinp(gtxt(x))
msinp = lambda x: sinp(mtxt(x))

########## Global Constants ##########
T = True
F = False
########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear(): system('cls||clear')
    
def safeExit():
    clear()
    print(gtxt("Saving"), end="")
    for i in range(3):
        print(gtxt("."), end="")
        sleep(1)
    gPrint("\nGoodbye!")
    sleep(1)
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
                    case 0: raise InvalidOperation(rtxt("case 0 matched")) # -rm
                    case 1: lib.search()
                    case 2: lib.addGame()
                    case 3: lib.delGame()
                    case 4: Library.instructions()
                    case 5: lib.printLib()
                    case 6: lib.resetLib()
                    case 7: lib.importGames()
                    case 8: lib.saveAndExit()
            except SystemExit: safeExit()
            except Exception as e: unknownExcept(2,e)
            finally: clear()
            
                
    
    
