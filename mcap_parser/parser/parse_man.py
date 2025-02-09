import os
import subprocess
from pathlib import Path
from .utils.mcap_utils import parse_mcap
from .utils.csv_utils import write_csv_TVN, write_csv_OMNI
from .utils.ld_utils import write_ld


def parse(input, output, style, recursive, multithreaded):
    # Get all the files and roots of folders
    if recursive:
        if os.path.isdir(input):
            for root, dirs, all_files in os.walk(input):
                for file in all_files:
                    if multithreaded == 0:
                        process_file(file, output, style, root)
                    if multithreaded == 1:
                        thread_file(file, output, style, root)
                    if multithreaded == "x":
                        print("Not done yet lil bro")

    else:
        process_file(input, output, style)

    print("Done loading data")


def thread_file(input, output, style, root):
    if input.endswith(".mcap"):
        # Get the full directory by combing the active root with the file name
        file_dir = os.path.join(root, input)

        # Make a task (fancy thread), append it to the list, and then start it
        subprocess.Popen(
            args=(
                "python",
                "mcap_parser.py",
                "cli",
                "-s",
                file_dir,
                "-d",
                output,
                "--style",
                style,
            )
        )


def process_file(input, output, style, root=None):
    if input.endswith(".mcap"):
        if root is not None:
            # Get the full directory by combing the active root with the file name
            file_dir = os.path.join(root, input)
        else:
            # This catch is for if its not recursive
            file_dir = input

        with open(file_dir, mode="rb") as file:
            data, topics = parse_mcap(file)

            if style == "TVN":
                write_csv_TVN(Path(file.name).stem, data, output)

            if style == "OMNI":
                write_csv_OMNI(Path(file.name).stem, data, topics, output)

            if style == "i2":
                write_ld()
