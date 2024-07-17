import sys
from parser.parse_man import parse_folder
from gui.gooey2 import setupGUI


def main():
    # parse_folder(sys.argv[1], sys.argv[2], "OMNI")
    setupGUI()


if __name__ == "__main__":
    main()
