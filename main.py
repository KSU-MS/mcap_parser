import sys
from parser.parse_man import parse_folder
from gui.gooey import start_gui


def main():
    # parse_folder(sys.argv[1], sys.argv[2], "OMNI")
    start_gui()


if __name__ == "__main__":
    main()
