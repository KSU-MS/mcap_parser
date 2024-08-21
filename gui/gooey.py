from tkinter import ttk
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import gui.utils.file_utils as utilities

persistence = utilities.persistence()
utils = utilities.front_end()

class Application(tk.Tk):
    def __init__(self, parse):
        super().__init__()

        upload_path = tk.StringVar()
        deload_path = tk.StringVar()
        parse_form = tk.StringVar(value='OMNI')

        upload_path.set("Upload dir")
        deload_path.set("Deload dir")

        self.title("MCAP Parser")
        self.geometry("800x500")

        self.left_frame_init = left_frame(self)
        self.right_frame_init = right_frame(self)
        self.middle_frame_init = middle_frame(self, parse)
        self.progress_bar = ttk.Progressbar(self, mode="indeterminate")

        persistence.load_files(
            self.left_frame_init.llistbox, 
            self.right_frame_init.rlistbox
        )

        self.protocol("WM_DELETE_WINDOW", command=lambda: persistence.save_files())

class left_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="nsew")

        upload_path = tk.StringVar()
        label_left = tk.Label(self, textvariable=upload_path, width=20, height=2, anchor="w")
        label_left.pack(pady=10, padx=10, anchor="w", fill="x")

        llistbox = tk.Listbox(self, selectmode=tk.SINGLE, background="#ffe0d6")
        llistbox.pack(pady=10, padx=10, anchor="w", fill="x")
        llistbox.drop_target_register(DND_FILES)
        llistbox.dnd_bind("<<Drop>>", command=lambda: utils.drop(upload_path, llistbox))
        llistbox_but = tk.Button(self, text="Select", command=lambda: utils.select_button())
        llistbox_but.pack(pady=10, padx=10)

        lbutton = tk.Button(self, text="Open Files", command=lambda: utils.select(upload_path, llistbox))
        lbutton.pack(pady=10, padx=10, anchor="w", fill="x")

class right_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=2, sticky="nsew")

        deload_path = tk.StringVar()
        label_right = tk.Label(self, textvariable=deload_path, width=20, height=2, anchor="w")
        label_right.pack(pady=10, padx=10, anchor="w", fill="x")

        rlistbox = tk.Listbox(self, selectmode=tk.SINGLE, background="#ffe0d6")
        rlistbox.pack(pady=10, padx=10, anchor="w", fill="x")
        rlistbox.drop_target_register(DND_FILES)
        rlistbox.dnd_bind("<<Drop>>", utils.drop(deload_path, rlistbox))
        # rlistbox.bind("<<ListboxSelect>>", select_down) # add so we can get rid of select button
        rlistbox_but = tk.Button(self, text="Select", command=lambda: utils.select_button())
        rlistbox_but.pack(pady=10, padx=10)

        rbutton = tk.Button(self, text="Open Folder", command=lambda: utils.select(deload_path, rlistbox))
        rbutton.pack(pady=10, padx=10, anchor="w", fill="x")

class middle_frame(tk.Frame):
    def __init__(self, parent, parse, upload_path, deload_path, parse_form):
        super().__init__(parent)

        self.grid(row=0, column=1, sticky="nsew")

        omni = tk.Radiobutton(self, text="OMNI", variable=parse_form, value="OMNI")
        omni.pack(pady=10, anchor="s", fill="x")
        tvn = tk.Radiobutton(self, text="TVN", variable=parse_form, value="TVN")
        tvn.pack(pady=10, anchor="s", fill="x")

        process = tk.Button(self, text="Parse", command=lambda: utilities.handle_files(
                upload_path, deload_path, parse_form, parse
                )
        )
        process.pack(pady=10, anchor="s", fill="x")

def open_gui(parse):
    app = Application(parse)
    app.mainloop()