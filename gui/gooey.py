import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import shutil
from tkinterdnd2 import DND_FILES, TkinterDnD


def process_folder(folder_path):

    parsed_files = parse_dude(folder_path) # flag
    return parsed_files


# function for uploading processed files to a chosen location
def upload_file(processed_files, destination):

    try:
        shutil.copy(processed_files, destination)
        messagebox.showinfo("Success", f"File uploaded to {destination}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload file: {e}")


# function for handling file processing and uploading
def handle_files(folder_path):

    processed_files = process_folder(folder_path)
    destination = filedialog.askdirectory(title="Select Upload Directory")
    if destination:
        upload_file(processed_files, destination)


# function for file selection
def select_files():

    files = filedialog.askopenfilenames(title="Select Files")
    if files:
        handle_files(files)


def start_gui():
   
    root = TkinterDnD.Tk()
    root.title("File Processor")
    root.geometry("800x400")

    # DND functionality (drag&drop)
    def drop(event):
        files = root.tk.splitlist(event.data) # flag, gotta find a better way to do this
        if files:
            handle_files(files)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)

    # select files
    select_button = tk.Button(root, text="Select Files", command=select_files)
    select_button.pack(pady=20)

    # progress_bar = ttk.Progressbar(root, mode='indeterminate')
    # progress_bar.pack(pady=20)

    root.mainloop()