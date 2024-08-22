import tkinter as tk
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import gui.utils.file_utils as Utilities

class Application(ctk.CTk):
    def __init__(self, parse):
        super().__init__()
        self.layout = Utilities.UIManager(self)
        persistence = Utilities.Persistence()
        self.utils = Utilities.InputManager()
        
        self.upload_path = ctk.StringVar(value="Upload dir")
        self.deload_path = ctk.StringVar(value="Deload dir")
        self.parse_form = ctk.StringVar(value='OMNI')

        ctk.set_appearance_mode("Dark")
        self.title("MCAP Parser")
        self.geometry("800x500")

        self.fg_color = '#1f1f1f'
        self.left_frame_init = LeftFrame(self)
        self.middle_frame_init = MiddleFrame(self, parse)
        self.right_frame_init = RightFrame(self)
        self.progress_bar = ctk.CTkProgressBar(self, mode="indeterminate")
        
        self.layout.configure_grid()
        self.layout.place_frames(
            left_frame = self.left_frame_init,
            right_frame = self.right_frame_init,
            middle_frame = self.middle_frame_init,
        )
        persistence.load_files(
            left = self.left_frame_init.llistbox, 
            right = self.right_frame_init.rlistbox
        )

        self.protocol("WM_DELETE_WINDOW", persistence.save_files(
            left = self.left_frame_init.llistbox,
            right = self.right_frame_init.rlistbox
            )
        )

class LeftFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="nsew")

        self.label_left = ctk.CTkLabel(self, textvariable=parent.upload_path, width=20, height=2, anchor="w")
        self.label_left.pack(pady=10, padx=10, anchor="w", fill="x")

        self.llistbox = tk.Listbox(self, selectmode=tk.SINGLE, background="#C0C0C0")
        self.llistbox.pack(pady=10, padx=10, anchor="w", fill="x")
        # llistbox.drop_target_register(DND_FILES)
        # llistbox.dnd_bind("<<Drop>>", command=lambda: utils.drop(upload_path, llistbox))

        self.llistbox_but = ctk.CTkButton(self, text="Select", command=lambda: parent.utils.select_button())
        self.llistbox_but.pack(pady=10, padx=10)

        self.lbutton = ctk.CTkButton(self, text="Open Files", command=lambda: parent.utils.select(parent.upload_path, self.llistbox))
        self.lbutton.pack(pady=10, padx=10, anchor="w", fill="x")

class RightFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=2, sticky="nsew")

        self.label_right = ctk.CTkLabel(self, textvariable=parent.deload_path, width=20, height=2, anchor="w")
        self.label_right.pack(pady=10, padx=10, anchor="w", fill="x")

        self.rlistbox = tk.Listbox(self, selectmode=tk.SINGLE, background="#C0C0C0")
        self.rlistbox.pack(pady=10, padx=10, anchor="w", fill="x")
        # rlistbox.drop_target_register(DND_FILES)
        # rlistbox.dnd_bind("<<Drop>>", utils.drop(deload_path, rlistbox))

        # rlistbox.bind("<<ListboxSelect>>", select_down) # add so we can get rid of select button
        self.rlistbox_but = ctk.CTkButton(self, text="Select", command=lambda: parent.utils.select_button())
        self.rlistbox_but.pack(pady=10, padx=10)

        self.rbutton = ctk.CTkButton(self, text="Open Folder", command=lambda: parent.utils.select(parent.deload_path, self.rlistbox))
        self.rbutton.pack(pady=10, padx=10, anchor="w", fill="x")

class MiddleFrame(ctk.CTkFrame):
    def __init__(self, parent, parse):
        super().__init__(parent)

        self.grid(row=0, column=1, sticky="nsew")

        omni = ctk.CTkRadioButton(self, text="OMNI", variable=parent.parse_form, value="OMNI")
        omni.pack(pady=10, anchor="s", fill="x")
        tvn = ctk.CTkRadioButton(self, text="TVN", variable=parent.parse_form, value="TVN")
        tvn.pack(pady=10, anchor="s", fill="x")

        process = ctk.CTkButton(self, text="Parse", command=lambda:[
            Utilities.handle_files(
                    parent.upload_path, 
                    parent.deload_path, 
                    parent.parse_form, 
                    parse
                ),
            parent.layout.show_progress(
                progress_bar = parent.progress_bar
            )
            ]
        )
        process.pack(pady=10, anchor="s", fill="x")

def open_gui(parse):
    app = Application(parse)
    app.mainloop()
