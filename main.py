import sys
from parser.parse_man import parse_folder


def main():
    parse_folder(sys.argv[1])


if __name__ == "__main__":
    main()
