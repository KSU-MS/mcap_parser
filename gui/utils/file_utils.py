from tkinter import filedialog
from parser.parse_man import parse_folder, process_file
from configparser import ConfigParser


def handle_files(folders): # handle them accordingly (in mysterious voice)
    dest = filedialog.askdirectory(title="Upload Dir")
    
    for folder in folders: 
        if 'dir': 
            parse_folder(folder, dest, "OMNI") 
        if 'file':
            process_file()
        else: 
            continue 


def drop(root, event): # dnd functionality (MEOW!)
    files = root.tk.splitlist(event.data)
    
    if files:
        handle_files(files)


def select_files():  
    files = filedialog.askopenfilenames(title="Select")
    
    if files:
        handle_files(files)

