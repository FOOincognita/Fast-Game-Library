import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# Used as custom exception when a non-existent item is accessed by dev
class DuplicateEntry(Exception): pass

# Used as a custom exception when an empty or N/A title is passed (INVALID ENTRY)
class EmptyEntry(Exception): pass

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
        
# Add required packages here
install_packages(['colorama'])