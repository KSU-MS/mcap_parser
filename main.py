import sys
from parser.parse_man import process_file
from gui.gooey import setupGUI


def main():
    # parse_folder(sys.argv[1], sys.argv[2], "OMNI")
    setupGUI(True, process_file) # difficulty accessing parseman from gooey
    

if __name__ == "__main__":
    main()
