#
# OpenCorpus/interactive.py
# Joseph Bergman
#
# An interactive script for downloading the data
import os
from collections import OrderedDict


OPTIONS = OrderedDict({
    1: change_directory,
    2: create_directory,
    3: select_directory,
})


#
# Functions from the OPTIONS variable
#
def change_directory():
    """Change directory"""
    pass


def create_directory():
    """Create a new directory"""
    dir_name = get_new_directory_name()
    try:
        os.mkdir(dir_name)
        clear_screen("Success! Create the directory: {}".format(dir_name))
    except:
        clear_screen("An error occurred. Please try again.")


def select_directory():
    """Select a directory for downloads"""
    pass


def display_options():
    """Display the user options from OPTIONS."""
    print("Select a command from the following: ")
    for k,v in OPTIONS.items():
        print("{}) {}".format(k, v.__doc__))


def get_option():
    """Get an option from the user.

    Returns:
        (int) The option selected if it was valid
        (None) If the option was invalid for any reason
    """
    try:
        option = int(input("Select an option: "))
        if option in OPTIONS: return option
    except:
        return None
    return None


#
# Helper functions for the current directory
#
def get_new_directory_name():
    """Prompt the user to enter a new directory name and return it."""
    valid_name = False
    dir_name = None
    while not valid_name:
        dir_name = str(input("Enter a directory name: ")).strip()
        valid_name = re.match(r'^[a-zA-Z0-9](\w|-)*$', dir_name)
        if not valid_name:
            print("Must begin with a letter or number.")
            print("Only letters, numbers, and underscores permitted.", end="\n\n")
        elif os.path.isdir(dir_name):
            valid_name = False
            print("Directory already exists.")
            print("Please enter a new directory name.", end="\n\n")
    return dir_name


def get_directories():
    """Returns a list of all the directories in the current directory."""
    return [item for item in os.listdir() if os.path.isdir(item)]

def list_directories():
    """Create human readable output of all directories in current directory."""
    dirs = get_directories()
    dirs.sort()
    for d in dirs:
        print(d)


#
# Helper functions for displaying terminal output
#

def clear_screen(display=None):
    """Clear the terminal screen. (optional) display the 'display' message."""
    os.system('cls' if os.name == 'nt' else 'clear')
    if display: print(display)
