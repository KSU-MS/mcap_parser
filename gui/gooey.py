import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from gui.utils.file_utils import select, drop, upload, handle_files


def start_gui():
    app = TkinterDnD.Tk()
    app.title("MCAP Parser")
    app.geometry("320x250")

    app.drop_target_register(DND_FILES)  # include drag box
    app.dnd_bind("<<Drop>>", drop)  # missing argument error (?)
    file_button = tk.Button(app, text=" Select ", command=select)
    file_button.grid(row=0, column=0, padx=20, pady=20)

    dest_button = tk.Button(app, text=" Destination ", command=upload)  # mk update text
    dest_button.grid(row=0, column=4, pady=20)

    selected = tk.StringVar(value="OMNI")  # save in userinfo
    omni = tk.Radiobutton(app, text=" OMNI ", variable=selected, value="OMNI")
    omni.grid(row=1, column=2, padx=10, pady=10)
    tvn = tk.Radiobutton(app, text=" TVN ", variable=selected, value="TVN")
    tvn.grid(row=1, column=3, pady=20)
    global style
    style = selected.get()

    process = tk.Button(app, text="   Parse   ", command=handle_files)
    process.grid(row=3, column=0, columnspan=5, pady=20)

    # progress bar

    app.mainloop()
