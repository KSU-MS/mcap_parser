import sys
import argparse
from parser.parse_man import parse
from gui.gooey import gui


def main():
    # TODO: Make the sys arg system not fucking aids and hardcodded to shit
    if sys.argv[1].__contains__("-"):
        if sys.argv[1] == "--help":
            print("Basic tool to parse mcaps with a GUI for the casuals")
            print("-h   --headless run parser with no GUI")
            # print("-x   --experimental wacky multithreading better for larger files")
            # print("-n   --no-preserve does not try to preserve file structure")
            print("")
            print("headless example:    python -h ./main.py ~/mcaps/ ~/parsed_mcaps/")

        else:
            if sys.argv[1].__contains__("h" or "headless"):
                parse(sys.argv[2], sys.argv[3], "OMNI")

    else:
        gui(parse)


if __name__ == "__main__":
    main()
