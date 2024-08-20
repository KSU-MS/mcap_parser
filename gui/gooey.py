from tkinter import ttk
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import gui.utils.file_utils as utilities

file_handler = utilities.handle_files()
persistence = utilities.persistence()
utils = utilities.front_end()

class Application(tk.Tk):
    def __init__(self, parse):
        global upload_path
        global deload_path
        global parse_form

        super.__init__()
        self.title("MCAP Parser")
        self.geometry("800x500")

        self.left_frame_init = left_frame(self)
        self.right_frame_init = right_frame(self)
        self.middle_frame_init = middle_frame(self, parse)

        upload_path.set("Upload dir")
        deload_path.set("Deload dir")

        persistence.load_files(
            self.left_frame_init.llistbox, 
            self.right_frame_init.rlistbox
        )

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
        llistbox.dnd_bind("<<Drop>>", command=lambda: util.drop(upload_path, llistbox))
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
    def __init__(self, parent, parse):
        self.__init__(parent)
        self.grid(row=0, column=1, sticky="nsew")

        parse_form = tk.StringVar(value="OMNI")  # default style set here
        omni = tk.Radiobutton(self, text="OMNI", variable=parse_form, value="OMNI")
        omni.pack(pady=10, anchor="s", fill="x")
        tvn = tk.Radiobutton(self, text="TVN", variable=parse_form, value="TVN")
        tvn.pack(pady=10, anchor="s", fill="x")

        process = tk.Button(self, text="Parse", command=lambda: utils.handle_files(parse))
        process.pack(pady=10, anchor="s", fill="x")

def open_gui(parse):
    global progress_bar

    app = Application(parse)
    progress_bar = ttk.Progressbar(app, mode="indeterminate")
    app.protocol("WM_DELETE_WINDOW", command=lambda: persistence.save_files())
    app.mainloop()