import sys
import subprocess
import pkg_resources
from platform import python_version
from pkg_resources import DistributionNotFound, VersionConflict
from colorama import init, Fore as fg, Back as bg, Style as st

# Raised when a non-existent item is accessed 
class DuplicateEntry(Exception): pass

# Raised when an empty or N/A title is imported
class EmptyEntry(Exception): pass

# Raised when an invalid selection is made user
class InvalidSelection(Exception): pass

# Flag raised to indicate a save & exit request
class SaveExit(Exception): pass

# Flag raised to indicate an exit without save request
class ExitNoSave(Exception): pass

####################################################################################################
# install_packages() IS NOT MY WORK; IT'S FROM STACK OVERFLOW 
# & WAS ONLY USED TO ENSURE DEPENDANCIES WERE INSTALLED PROPERLY 
# FOR EACH GROUP MEMBER SO THEY COULD TEST THEIR CODE
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
####################################################################################################

########## PYTHON VER VALIDATION ##########
if python_version().split('.')[1] != "10":
    print(st.BRIGHT + fg.RED + "\n[ERROR] PLEASE INSTALL PYTHON 3.10 OR ABOVE" + st.RESET_ALL)
    print(st.BRIGHT + fg.YELLOW + "Your current version: " + str(python_version()) + "\n" + st.RESET_ALL)
    
    
