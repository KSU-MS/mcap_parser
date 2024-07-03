import sys
from parser.parse_man import parse_folder
from gui.gooey import start_gui

def main():
    # parse_folder(sys.argv[1])
    start_gui(parse_folder)


if __name__ == "__main__":
    main()
