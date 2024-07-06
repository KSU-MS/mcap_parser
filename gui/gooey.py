import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from utils.file_utils import drop, select, upload, handle_files


def start_gui(): # use grid(column,pady) to make prettier
    app = TkinterDnD.Tk()
    app.title("MCAP Parser")
    app.geometry("1000x550")

    app.drop_target_register(DND_FILES)
    app.dnd_bind("<<Drop>>", drop(app))
    choosefiles = tk.Button(app, text="Select", command=select)
    choosefiles.pack(pady=20) 

    filedestination = tk.Button(app, text="Destination", command=upload)
    filedestination.pack(pady=20)

    selected = tk.StringVar(value="OMNI") # include saved selection in userinfo
    omni = tk.Radiobutton(app, text="OMNI", variable=selected, value="OMNI")
    omni.pack(pady=20)
    tvn = tk.Radiobutton(app, text="TVN", variable=selected, value="TVN")
    tvn.pack(pady=20)
    selectedstyle = selected.get()

    process = tk.Button(app, text="Parse", command=handle_files)
    process.pack(pady=20)

    # progress_bar = ttk.Progressbar(root, mode="indeterminate")
    # progress_bar.pack(pady=20)

    app.mainloop()
