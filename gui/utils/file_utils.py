from tkinter import filedialog
import tkinter as tk
import json, os
 
SAVE_FILE = "saved_files.json"

class LayoutManager:
    def __init__(self, parent):
        self.parent = parent

    def configure_grid(self):
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)  # Left Frame
        self.parent.grid_columnconfigure(1, weight=2)  # Middle Frame
        self.parent.grid_columnconfigure(2, weight=1)  # Right Frame

        self.parent.grid_rowconfigure(1, weight=0) # progress bar row

    def place_frames(self, left_frame, middle_frame, right_frame, progress_bar):
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        middle_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        right_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        
        progress_bar.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=10)

class InputMethods: # abstract GUI-dependent code

    def drop(self, event, location, box):
        event_list = event.data
        values = [str(x) for x in event_list[event]]
        path = " ".join(values)

        location.set(path) # upload_path/deload_path 
        box.insert("end", path) # llistbox/rlistbox

    def select(self, location, box):
        files = filedialog.askdirectory(title="File Select") # gui dependent
        files = str(files)
        if files:
            location.set(files) # upload_path/deload_path
            box.insert("end", files) # llistbox/rlistbox

    def select_button(self, location, box):
        try:
            selected_file = box.get(box.curselection())
            location.set(selected_file)
        except tk.TclError:
            tk.messagebox.showerror("No file selected in the left listbox.") # gui dependent

class Persistence: # needs error handling

    def save_files(self, left, right):
        data = {
            "upload_files": list(left.get(0, tk.END)),
            "deload_files": list(right.get(0, tk.END)),
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    def load_files(self, left, right):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                for file in data.get("upload_files", []):
                    left.insert(tk.END, file)
                for file in data.get("deload_files", []):
                    right.insert(tk.END, file)

def show_progress(position, length, bar): # not accessed
    step_value = position / length

    bar.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
    bar.step(step_value)
    # app.update_idletasks()
    bar.grid_forget()

def handle_files(upload_path, deload_path, parse_form, parse):
    upload = upload_path.get()
    deload = deload_path.get() + "/"
    style = parse_form.get()

    # have "default" rather than string, don't like hardcode here
    if (upload != "Upload dir") and (deload != "Deload dir/"): 
        parse(upload, deload, style)
        # show_progress()
    else:
        tk.messagebox.showerror("No path selected") # gui dependent (also doesn't show string)