from tkinter import filedialog
from configparser import ConfigParser
from parser.parse_man import parse_folder, process_file
import os

# class userinfo(): # need to fix CONFIG parser

# parser = ConfigParser()
# parser.read("saved_paths.txt")

# grab_dir = parser.get('user_paths', 'grab')
# initial_origin = grab_dir
# upload_dir = parser.get('user_paths', 'upload')
# initial_dest = upload_dir


def select():
    global files
    wawa = filedialog.askopenfilenames(title="Select")  # mk include inital dir
    files = str(wawa[0])
    print(files)
    # "('C:/Users/rexro/Documents/06_14_2024_16_42_58-fixed.mcap',)"


def drop(root, event):
    global files
    files = str(root.tk.splitlist(event.data))


def upload():
    global dir
    dir = str(filedialog.askdirectory(title="Upload Dir"))  # mk include initial dir


# def style_select(): # need to find solution within this scope
#     global style
#     style =


def handle_files():
    fileExtension = os.path.splitext(files)[1]
    print(fileExtension)

    if fileExtension == ".mcap',)":  # better ways to do this ?
        process_file(files, dir, style)
    else:
        parse_folder(files, dir, style)

    print(f"Parsing {files} into {dir} formatted in {style}")


files = " "
dir = " "
style = " "
