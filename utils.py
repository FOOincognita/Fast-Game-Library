import sys
import subprocess
import pkg_resources
from platform import python_version
from pkg_resources import DistributionNotFound, VersionConflict
from colorama import init, Fore as fg, Back as bg, Style as st

# Used as custom exception when a non-existent item is accessed by dev
class DuplicateEntry(Exception): pass

# Used as a custom exception when an empty or N/A title is passed (INVALID ENTRY)
class EmptyEntry(Exception): pass

# Used as a custom exception when anything other than ints 1-8 are entered in main menu
class InvalidSelection(Exception): pass

def should_install_requirement(requirement):
    should_install = False
    try:
        pkg_resources.require(requirement)
    except (DistributionNotFound, VersionConflict):
        should_install = True
    return should_install

def install_packages(requirement_list):
    try:
        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        if len(requirements) > 0:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
        else:
            pass # print("Requirements already satisfied")

    except Exception as e:
        print(e)
        print(st.BRIGHT + fg.RED + "[ERROR] PLEASE INSTALL PIP\n" + st.RESET_ALL)
        
# Add required packages here
install_packages(['colorama'])

########## PYTHON VER VALIDATION ##########
if python_version().split('.')[1] != "10":
    print(st.BRIGHT + fg.RED + "\n[ERROR] PLEASE INSTALL PYTHON 3.10 OR ABOVE" + st.RESET_ALL)
    print(st.BRIGHT + fg.YELLOW + "Your current version: " + str(python_version()) + "\n" + st.RESET_ALL)
    print(st.BRIGHT + fg.MAGENTA + "Alternate Fix:\nChange the match-case statements in GameLib.py to if-elif statements\nThen, in utils.py, comment out anything below \"PYTHON VER VALIDATION\" " + "\n" + st.RESET_ALL)
