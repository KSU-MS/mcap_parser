import os
import multiprocessing
from pathlib import Path
from .utils.csv_utils import write_csv_TVN, write_csv_OMNI
from .utils.mcap_utils import parse_mcap


def parse(input, output, style):
    # Make a list to hold active threads
    tasks = []

    # Get all the files and roots of folders
    # if recursive:
    if os.path.isdir(input):
        for root, dirs, all_files in os.walk(input):
            for file in all_files:
                thread_file(tasks, root, file, output, style)

        global progress_length
        progress_length = len(tasks)

        global progress_position
        progress_position = 0

    # else:
    process_file(input, output, style)

    print("Done")


def thread_file(list, root, input, output, style):
    if input.endswith(".mcap"):
        # Get the full directory by combing the active root with the file name
        file_dir = os.path.join(root, input)

        # Make a task (fancy thread), append it to the list, and then start it
        multiprocessing.set_start_method("spawn")
        new_task = multiprocessing.Process(
            target=process_file, args=(file_dir, output, style)
        )

        list.append(new_task)
        new_task.start()


def process_file(input, output, style):
    if input.endswith(".mcap"):
        with open(input, mode="rb") as file:
            data, topics = parse_mcap(file)

            if style == "TVN":
                write_csv_TVN(Path(file.name).stem, data, output)

            if style == "OMNI":
                write_csv_OMNI(Path(file.name).stem, data, topics, output)
