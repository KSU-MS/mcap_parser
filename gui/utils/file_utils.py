from tkinter import filedialog
import tkinter as tk
import json, os
 
global upload_path
global deload_path
global parse_form
SAVE_FILE = "saved_files.json"

class front_end:

    def drop(event, location, box):
        event_list = event.data
        values = [str(x) for x in event_list[event]]
        path = " ".join(values)

        location.set(path) # upload_path/deload_path 
        box.insert("end", path) # llistbox/rlistbox

    def select(location, box):
        files = filedialog.askdirectory(title="File Select")
        files = str(files)
        if files:
            location.set(files) # upload_path/deload_path
            box.insert("end", files) # llistbox/rlistbox

    def select_button(location, box):
        try:
            selected_file = box.get(box.curselection())
            location.set(selected_file)
        except tk.TclError:
            tk.messagebox.showerror("No file selected in the left listbox.")  

def show_progress(): # can't figure out how to make this inuitive (not pass app as arg)
    global progress_length
    global progress_position

    step_value = progress_position / progress_length

    progress_bar.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
    progress_bar.step(step_value)
    # app.update_idletasks()
    progress_bar.grid_forget()

def handle_files(parse):
    upload = upload_path.get()
    deload = deload_path.get() + "/"
    style = parse_form.get()
    if upload and deload:
        parse(upload, deload, style)
        # show_progress()

class persistence:

    def save_files(left, right):
        data = {
            "upload_files": list(left.get(0, tk.END)),
            "deload_files": list(right.get(0, tk.END)),
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    def load_files(left, right):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                for file in data.get("upload_files", []):
                    left.insert(tk.END, file)
                for file in data.get("deload_files", []):
                    right.insert(tk.END, file)
