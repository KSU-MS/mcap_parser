import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
# from gui.utils.file_utils import select, drop, upload, handle_files


def setupGUI(headless, passed_function):


    if (headless != True):

        def dir_drop_up(event):
            upload_path.set(event.data)
            llistbox.insert("end", event.data)

        def dir_drop_down(event):
            deload_path.set(event.data)
            rlistbox.insert("end", event.data)

        def select_up():
            files = filedialog.askopenfilenames(title="File Select")
            files = str(files[0])
            upload_path.set(files)
            llistbox.insert("end", files)

        def select_down():
            files = filedialog.askdirectory(title="File Select")
            files = str(files)
            deload_path.set(files)
            rlistbox.insert("end", files)

        def handle_files(passed_function):
            upload = upload_path.get()
            deload = deload_path.get()
            style = parse_form.get()
            passed_function(upload, deload, style)

        # init
        app = TkinterDnD.Tk()
        app.title("MCAP Parser")
        app.geometry("800x300")
        app.grid_columnconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=0)
        app.grid_columnconfigure(2, weight=1)
        app.grid_rowconfigure(0, weight=1)
        left_frame = tk.Frame(app)
        right_frame = tk.Frame(app)
        middle_frame = tk.Frame(app)
        left_frame.grid(row=0, column=0, sticky='nsew')
        right_frame.grid(row=0, column=2, sticky='nsew')
        middle_frame.grid(row=0, column=1, sticky='nsew')

        upload_path = tk.StringVar()
        deload_path = tk.StringVar()

        # left frame
        label_left = tk.Label(left_frame, textvariable=upload_path, width=20, height=2, anchor='w')
        label_left.pack(pady=10, padx=10, anchor='w', fill='x')

        llistbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, background="#ffe0d6") # add select functionality
        llistbox.pack(pady=10, padx=10, anchor='w', fill = 'x')
        llistbox.drop_target_register(DND_FILES)
        llistbox.dnd_bind("<<Drop>>", dir_drop_up)

        lbutton = tk.Button(left_frame, text="Select here", command=select_up)
        lbutton.pack(pady=10, padx=10, anchor='w', fill='x')

        # right frame
        label_right = tk.Label(right_frame, textvariable=deload_path, width=20, height=2, anchor='w')
        label_right.pack(pady=10, padx=10, anchor='w', fill='x')

        rlistbox = tk.Listbox(right_frame, selectmode=tk.SINGLE, background="#ffe0d6")
        rlistbox.pack(pady=10, padx=10, anchor='w', fill = 'x')
        rlistbox.drop_target_register(DND_FILES)
        rlistbox.dnd_bind("<<Drop>>", dir_drop_down)

        rbutton = tk.Button(right_frame, text="Select here", command=select_down)
        rbutton.pack(pady=10, padx=10, anchor='w', fill='x')

        # middle column
        testlabel = tk.Label(middle_frame, width="15", height="9")
        testlabel.pack(pady=10)

        parse_form = tk.StringVar(value="OMNI") # default
        omni = tk.Radiobutton(middle_frame, text="OMNI", variable=parse_form, value="OMNI")
        omni.pack(pady=10, anchor='s', fill='x')
        tvn = tk.Radiobutton(middle_frame, text="TVN", variable=parse_form, value="TVN")
        tvn.pack(pady=10, anchor='s', fill='x')

        process = tk.Button(middle_frame, text="Parse", command=handle_files)
        process.pack(pady=10, anchor='s', fill='x')

        # finish
        upload_path.set("Upload dir")
        deload_path.set("Deload dir")

        app.mainloop()
    
    else:
        print("\nEnter the details for file handling or type 'exit' to quit:")

        upload_path = input("Enter the upload path: ")
        if upload_path.lower() == 'exit':
            print("Exiting.")

        deload_path = input("Enter the deload path: ")
        if deload_path.lower() == 'exit':
            print("Exiting.")

        parse_type = input("Enter the parse type (OMNI/TVN): ")
        if parse_type.lower() == 'exit':
            print("Exiting.")

        if parse_type not in ['OMNI', 'TVN']:
            print("Invalid parse type. Please enter 'OMNI' or 'TVN'.")

        handle_files(upload_path, deload_path, parse_type)
        



