import os
from pathlib import Path
from .utils.csv_utils import write_csv_TVN
from .utils.mcap_utils import parse_mcap


def parse_folder(folder):
    for file_name in os.listdir(folder):
        if file_name.endswith(".mcap"):
            with open(os.path.join(folder, file_name), mode="rb") as file:
                data = parse_mcap(file)

                write_csv_TVN(Path(file_name).stem, data)
