import os
import multiprocessing
from pathlib import Path
from .utils.csv_utils import write_csv_TVN, write_csv_OMNI
from .utils.mcap_utils import parse_mcap


def parse_folder(folder, output, style):
    # Make a list to hold active threads
    tasks = []

    for file_name in os.listdir(folder):
        if file_name.endswith(".mcap"):
            # Get the full directory
            file_dir = os.path.join(folder, file_name)

            # Make a task (fancy thread), append it to the list, and then start it
            task = multiprocessing.Process(
                target=process_file, args=(file_dir, output, style)
            )
            tasks.append(task)
            task.start()

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
