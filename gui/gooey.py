import tkinter as tk
from tkinter import ttk, filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
import json
import os
# import gui.utils.file_utils as utl


def open_gui(passed_function):
    SAVE_FILE = "saved_files.json"

    def drop_upload(event):
        event_list = event.data
        values = [str(x) for x in event_list[event]]
        path = " ".join(values)

        upload_path.set(path)
        llistbox.insert("end", path)

    def drop_deload(event):
        event_list = event.data
        values = [str(x) for x in event_list[event]]
        path = " ".join(values)

        deload_path.set(path)
        rlistbox.insert("end", path)

    def select_upload():
        files = filedialog.askopenfilenames(title="File Select")
        if files:
            files = str(files[0])
            upload_path.set(files)
            llistbox.insert("end", files)

    def select_deload():
        files = filedialog.askdirectory(title="File Select")
        files = str(files)
        if files:
            deload_path.set(files)
            rlistbox.insert("end", files)

    def handle_files():
        upload = upload_path.get()
        deload = deload_path.get() + "/"
        style = parse_form.get()
        if upload and deload:
            progress_bar.grid(
                row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew"
            )  # doesn't show actual progess
            app.update_idletasks()
            passed_function(upload, deload, style)
            progress_bar.grid_forget()

    def select_up():
        try:
            selected_file = llistbox.get(llistbox.curselection())
            upload_path.set(selected_file)
        except tk.TclError:
            print("No file selected in the left listbox.")  # add pop up box

    def select_down():
        try:
            selected_file = rlistbox.get(rlistbox.curselection())
            deload_path.set(selected_file)
        except tk.TclError:
            print("No file selected in the right listbox.")  # add pop up box

    def save_files():  # need to make functionality for json file creation on first use
        data = {
            "upload_files": list(llistbox.get(0, tk.END)),
            "deload_files": list(rlistbox.get(0, tk.END)),
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    def load_files():
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                for file in data.get("upload_files", []):
                    llistbox.insert(tk.END, file)
                for file in data.get("deload_files", []):
                    rlistbox.insert(tk.END, file)

    app = TkinterDnD.Tk()
    app.title("MCAP Parser")
    app.geometry("800x500")
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=0)
    app.grid_columnconfigure(2, weight=1)
    app.grid_rowconfigure(0, weight=1)
    left_frame = tk.Frame(app)
    right_frame = tk.Frame(app)
    middle_frame = tk.Frame(app)
    left_frame.grid(row=0, column=0, sticky="nsew")
    right_frame.grid(row=0, column=2, sticky="nsew")
    middle_frame.grid(row=0, column=1, sticky="nsew")

    upload_path = tk.StringVar()
    deload_path = tk.StringVar()

    # left frame
    label_left = tk.Label(
        left_frame, textvariable=upload_path, width=20, height=2, anchor="w"
    )
    label_left.pack(pady=10, padx=10, anchor="w", fill="x")

    llistbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, background="#ffe0d6")
    llistbox.pack(pady=10, padx=10, anchor="w", fill="x")
    llistbox.drop_target_register(DND_FILES)
    llistbox.dnd_bind("<<Drop>>", drop_upload)
    # llistbox.bind("<<ListboxSelect>>", select_up) # was supposed to be how we select files, for now button works instead
    llistbox_but = tk.Button(left_frame, text="Select", command=select_up)
    llistbox_but.pack(pady=10, padx=10)

    lbutton = tk.Button(left_frame, text="Open Files", command=select_upload)
    lbutton.pack(pady=10, padx=10, anchor="w", fill="x")

    # right frame
    label_right = tk.Label(
        right_frame, textvariable=deload_path, width=20, height=2, anchor="w"
    )
    label_right.pack(pady=10, padx=10, anchor="w", fill="x")

    rlistbox = tk.Listbox(right_frame, selectmode=tk.SINGLE, background="#ffe0d6")
    rlistbox.pack(pady=10, padx=10, anchor="w", fill="x")
    rlistbox.drop_target_register(DND_FILES)
    rlistbox.dnd_bind("<<Drop>>", drop_deload)
    # rlistbox.bind("<<ListboxSelect>>", select_down)
    rlistbox_but = tk.Button(right_frame, text="Select", command=select_down)
    rlistbox_but.pack(pady=10, padx=10)

    rbutton = tk.Button(right_frame, text="Open Folder", command=select_deload)
    rbutton.pack(pady=10, padx=10, anchor="w", fill="x")

    # middle column
    testlabel = tk.Label(middle_frame, width="15", height="9")
    testlabel.pack(pady=10)

    parse_form = tk.StringVar(value="OMNI")  # default
    omni = tk.Radiobutton(middle_frame, text="OMNI", variable=parse_form, value="OMNI")
    omni.pack(pady=10, anchor="s", fill="x")
    tvn = tk.Radiobutton(middle_frame, text="TVN", variable=parse_form, value="TVN")
    tvn.pack(pady=10, anchor="s", fill="x")

    process = tk.Button(middle_frame, text="Parse", command=handle_files)
    process.pack(pady=10, anchor="s", fill="x")

    # finish - set to most recent file/dir/style
    upload_path.set("Upload dir")
    deload_path.set("Deload dir")

    progress_bar = ttk.Progressbar(app, mode="indeterminate")

    load_files()
    app.protocol("WM_DELETE_WINDOW", save_files)
    app.mainloop()


def headless(passed_function):
    def get_input(prompt):
        user_input = input(prompt)
        if user_input.lower() == "exit":
            exit()

    print("\nEnter the details for file handling or type 'exit' to quit:")

    upload_path = get_input("Enter the upload path: ")
    deload_path = get_input("Enter the deload path: ")
    parse_type = get_input("Enter the parse type (OMNI/TVN):")

    try:
        passed_function(upload_path, deload_path, parse_type)
    except ValueError as e:
        print(f"Error: {e}")
