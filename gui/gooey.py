import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import gui.utils.file_utils as utilities

persistence = utilities.persistence()
utils = utilities.front_end()

class Application(ctk.CTk):
    def __init__(self, parse):
        super().__init__()

        self.upload_path = tk.StringVar()
        self.deload_path = tk.StringVar()
        self.parse_form = tk.StringVar(value='OMNI')

        ctk.set_appearance_mode("Dark")
        self.upload_path.set("Upload dir")
        self.deload_path.set("Deload dir")

        self.title("MCAP Parser")
        self.geometry("800x500")

        self.left_frame_init = left_frame(self)
        self.right_frame_init = right_frame(self)
        self.middle_frame_init = middle_frame(self, parse)
        self.progress_bar = ttk.Progressbar(self, mode="indeterminate")

        persistence.load_files(
            left = self.left_frame_init.llistbox, 
            right = self.right_frame_init.rlistbox
        )

        self.protocol("WM_DELETE_WINDOW", persistence.save_files(
            left = self.left_frame_init.llistbox,
            right = self.right_frame_init.rlistbox
            )
        )

class left_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="nsew")

        self.label_left = tk.Label(self, textvariable=parent.upload_path, width=20, height=2, anchor="w")
        self.label_left.pack(pady=10, padx=10, anchor="w", fill="x")

        self.llistbox = tk.Listbox(self, selectmode=tk.SINGLE, background="#ffe0d6")
        self.llistbox.pack(pady=10, padx=10, anchor="w", fill="x")
        # llistbox.drop_target_register(DND_FILES)
        # llistbox.dnd_bind("<<Drop>>", command=lambda: utils.drop(upload_path, llistbox))

        self.llistbox_but = tk.Button(self, text="Select", command=lambda: utils.select_button())
        self.llistbox_but.pack(pady=10, padx=10)

        self.lbutton = tk.Button(self, text="Open Files", command=lambda: utils.select(parent.upload_path, self.llistbox))
        self.lbutton.pack(pady=10, padx=10, anchor="w", fill="x")

class right_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=2, sticky="nsew")

        self.label_right = tk.Label(self, textvariable=parent.deload_path, width=20, height=2, anchor="w")
        self.label_right.pack(pady=10, padx=10, anchor="w", fill="x")

        self.rlistbox = tk.Listbox(self, selectmode=tk.SINGLE, background="#ffe0d6")
        self.rlistbox.pack(pady=10, padx=10, anchor="w", fill="x")
        # rlistbox.drop_target_register(DND_FILES)
        # rlistbox.dnd_bind("<<Drop>>", utils.drop(deload_path, rlistbox))

        # rlistbox.bind("<<ListboxSelect>>", select_down) # add so we can get rid of select button
        self.rlistbox_but = tk.Button(self, text="Select", command=lambda: utils.select_button())
        self.rlistbox_but.pack(pady=10, padx=10)

        self.rbutton = tk.Button(self, text="Open Folder", command=lambda: utils.select(parent.deload_path, self.rlistbox))
        self.rbutton.pack(pady=10, padx=10, anchor="w", fill="x")

class middle_frame(tk.Frame):
    def __init__(self, parent, parse):
        super().__init__(parent)

        self.grid(row=0, column=1, sticky="nsew")

        omni = tk.Radiobutton(self, text="OMNI", variable=parent.parse_form, value="OMNI")
        omni.pack(pady=10, anchor="s", fill="x")
        tvn = tk.Radiobutton(self, text="TVN", variable=parent.parse_form, value="TVN")
        tvn.pack(pady=10, anchor="s", fill="x")

        process = tk.Button(self, text="Parse", command=lambda: utilities.handle_files(
                parent.upload_path, parent.deload_path, parent.parse_form, parse
                )
        )
        process.pack(pady=10, anchor="s", fill="x")

def open_gui(parse):
    app = Application(parse)
    app.mainloop()
