import sys
from parser.parse_man import process_file
from gui.gooey import setupGUI


def main():
    # parse_folder(sys.argv[1], sys.argv[2], "OMNI")
    setupGUI(headless=False, passed_function=process_file) # difficulty accessing parseman from gooey on my computer


if __name__ == "__main__":
    main()
