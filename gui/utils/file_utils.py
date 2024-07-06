from tkinter import filedialog
from parser.parse_man import parse_folder, process_file
from configparser import ConfigParser


def userinfo():
    parser = ConfigParser()
    parser.read("saved_paths.txt") 

    def origin():
        grab_dir = parser.get('user_paths', 'grab')
        return grab_dir
    
    def destination():
        upload_dir = parser.get('user_paths', 'upload')
        return upload_dir


def select():
    ddir = userinfo.origin()
    if (userinfo):
        ddir = userinfo.o

    files = filedialog.askopenfilenames(title="Select", initialdir=ddir)
    return files


def drop(root, event): # dnd functionality (MEOW!)
    files = root.tk.splitlist(event.data)
    return files


def upload():
    dest = filedialog.askdirectory(title="Upload Dir", initialdir=userinfo.destination)
    return dest


def handle_files(select, dest, style): 
    parse_folder(select, dest, style="OMNI")
    process_file()
