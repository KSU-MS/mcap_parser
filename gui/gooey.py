import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from utils.file_utils import drop, select_files


def start_gui():

    app = TkinterDnD.Tk()
    app.title("MCAP Parser")
    # app.iconbitmap -> put scrappy!
    app.geometry("1000x550")

    parser = ConfigParser() # no work
    parser.read("saved_paths.txt") 
    grab_dir = parser.get('user_paths', 'grab')
    upload_dir = parser.get('user_paths', 'upload')

    app.drop_target_register(DND_FILES)
    app.dnd_bind("<<Drop>>", drop(app))

    select_button = tk.Button(app, text="Select", command=select_files)
    select_button.pack(pady=20)

    #  progress_bar = ttk.Progressbar(root, mode="indeterminate")
    # progress_bar.pack(pady=20)

    app.mainloop()
