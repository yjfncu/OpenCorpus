#
# OpenCorpus/interactive.py
# Joseph Bergman
#
# An interactive script for downloading the data
import os
import re
from collections import OrderedDict


ERROR = "An error occurred. Please try again."


#
# Functions for the OPTIONS variable
#
def change_directory():
    """Change current directory"""
    try:
        find_desired_directory()
        return True
    except:
        clear_screen(display=ERROR)
        return False


def create_directory():
    """Create a new directory"""
    dir_name = get_new_directory_name()
    try:
        os.mkdir(dir_name)
        return dir_name
    except:
        clear_screen(display=ERROR)
        return False


def display_current_directory():
    """Display the current directory"""
    print("Currently at {}".format(os.getcwd()), end='\n\n')
    display_available_directories()
    print()


def cancel():
    """Exit the downloader"""
    clear_screen("Interactive downloader canceled.")
    return


OPTIONS = OrderedDict({
    1: change_directory,
    2: create_directory,
    3: display_current_directory,
    4: cancel,
})



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
            error = ("Must begin with a letter or number.\n"
                    "Only letters, numbers, and underscores permitted.\n\n")
            clear_screen(display=error)
        elif os.path.isdir(dir_name):
            valid_name = False
            error = ("Directory already exists.\n",
                    "Please enter a new directory name.\n\n")
    return dir_name


def find_desired_directory():
    """Help the user navigate to a desire directory."""
    directory_selected = False
    while not directory_selected:
        display_current_directory()
        dir_name = str(input("Enter a directory name: ")).strip()
        if os.path.isdir(dir_name) and dir_name != ".":
            clear_screen()
            os.chdir(dir_name)
        if dir_name == ".":
            directory_selected = True



#
# Helper functions for displaying terminal output
#
def clear_screen(display=None):
    """Clear the terminal screen. (optional) display the 'display' message."""
    os.system('cls' if os.name == 'nt' else 'clear')
    if display: print(display)


def display_options():
    """Display the user options from OPTIONS."""
    print("Select a command from the following: ")
    for k,v in OPTIONS.items():
        print("{}) {}".format(k, v.__doc__))


def display_available_directories():
    """Create human readable output of all directories in current directory."""
    dirs = [item for item in os.listdir()
                    if os.path.isdir(item) and not item.startswith('.')]
    dirs.sort()
    dirs.append("..")
    dirs.append(".  (select current)")
    for d in dirs:
        print(d)



#
# Driver: Main functions for running the downloader
#

def get_option():
    """Get an option from the user.

    Returns:
        (int) The option selected if it was valid
        (None) If the option was invalid for any reason
    """
    while True:
        display_options(); print();
        try:
            option = int(input("Select an option: "))
            if option in OPTIONS:
                return option
            else:
                clear_screen(display="Invalid Option \n")
        except:
            clear_screen(display="Invalid Option \n")


def run():
    """Runs the downloader."""
    desired_cwd_selected = None
    current_option = None

    # The user must ultimately create a directory
    while not desired_cwd_selected:
        clear_screen()
        print("This installer will help you create a folder for downloading files.\n")
        option = get_option()
        function = OPTIONS[option]

        if function == display_current_directory:
            # Just display the directory
            clear_screen()
            display_current_directory()
            input("\nPress enter to continue ")

        elif function == change_directory:
            # If the user changed the directory, have them create a folder
            clear_screen()
            if change_directory():
                desired_cwd_selected = True
            else:
                clear_screen(display=ERROR)

        elif function == cancel:
            # User wants to exit the installer
            cancel()
            return

        else:
            # User is ready to create a directory
            desired_cwd_selected = True

    # Create a directory
    dir_name = False
    clear_screen("Success! Now let's create a directory to store files\n")
    while not dir_name:
        display_current_directory();
        dir_name = create_directory()
        if dir_name:
            clear_screen("Success! Created the directory: {}".format(dir_name))
            os.chdir(dir_name)
            print("We are now in: {}".format(os.getcwd()))
        else:
            clear_screen(display=ERROR)
