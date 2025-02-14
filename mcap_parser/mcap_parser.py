import sys
from argparse import ArgumentParser
from parser.parse_man import parse
from gui.gui_man import run_gui


def main():
    # Setup the parser
    apar = ArgumentParser(
        description="A basic MCAP parser into CSV",
        epilog="You can get a unique help output for each mode btw",
    )

    # Add subparsers for gui and headless
    spar = apar.add_subparsers(dest="mode", help="Choose how to use the parser")
    gui = spar.add_parser("gui", help="Run the parser with the tkinter GUI frontend")
    cli = spar.add_parser("cli", help="Run the parser in headless mode")

    # Add args for headless parser
    cli.add_argument("-s", type=str, required=True, help="Source of files")
    cli.add_argument("-d", type=str, required=True, help="Destination of files")
    cli.add_argument("--style", choices=["TVN", "OMNI", "LD"], help="Style of parse")
    cli.add_argument("-r", type=bool, help="Enables recursion through nested folders")
    cli.add_argument("-m", choices=["none", "legacy", "x"], help="Multithreading")

    # TODO: Make these real
    # cli.add_argument("-n", help="Does not try to preserve file structure")

    # Run GUI if no args get passed
    if len(sys.argv) == 1:
        run_gui(parse)

    # Collect flags
    args = apar.parse_args()

    if args.mode == "gui":
        run_gui(parse)

    elif args.mode == "cli":
        parse(args.s, args.d, args.style, args.r, args.m)


if __name__ == "__main__":
    main()
