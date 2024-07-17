import os
import multiprocessing
from pathlib import Path
from .utils.csv_utils import write_csv_TVN, write_csv_OMNI
from .utils.mcap_utils import parse_mcap


def parse(folder, output, style):
    # Make a list to hold active threads
    tasks = []

    # Get all the files and roots of folders
    for root, dirs, all_files in os.walk(folder):
        for file in all_files:
            if file.endswith(".mcap"):
                # print((root[len(folder) + 1 : len(root)]) + file)

                # Get the full directory by combing the active root with the file name
                file_dir = os.path.join(root, file)

                # Make a task (fancy thread), append it to the list, and then start it
                new_task = multiprocessing.Process(
                    target=process_file, args=(file_dir, output, style)
                )

                tasks.append(new_task)
                new_task.start()

    # This just makes us wait until all tasks have been executed
    for task in tasks:
        task.join()

    print("Done")


def process_file(file, output, style):
    with open(file, mode="rb") as file:
        data, topics = parse_mcap(file)

        if style == "TVN":
            write_csv_TVN(Path(file.name).stem, data, output)

        if style == "OMNI":
            write_csv_OMNI(Path(file.name).stem, data, topics, output)
