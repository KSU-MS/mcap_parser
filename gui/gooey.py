import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import shutil
from tkinterdnd2 import DND_FILES, TkinterDnD
from parser.parse_man import parse_folder
from parser.parse_man import process_file


def process_folder(folders, dest):
    for folder in folders:
        parse_folder(folder, dest, "OMNI")  # flag


# function for handling file processing and uploading
def handle_files(folder_path):
    destination = filedialog.askdirectory(title="Select Upload Directory")
    process_folder(folder_path, destination)


# function for file selection
def select_files():
    files = filedialog.askopenfilenames(title="Select Files")
    if files:
        handle_files(files)


def start_gui():
    root = TkinterDnD.Tk()
    root.title("File Processor")
    root.geometry("800x400")

    # DND functionality (MEOW)
    def drop(event):
        files = root.tk.splitlist(
            event.data
        )  # flag, gotta find a better way to do this
        if files:
            handle_files(files)

    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drop)

    # select files
    select_button = tk.Button(root, text="Select Files", command=select_files)
    select_button.pack(pady=20)

    # progress_bar = ttk.Progressbar(root, mode="indeterminate")
    # progress_bar.pack(pady=20)

    root.mainloop()
