from tkinter import filedialog
from configparser import ConfigParser

# abstract class 
def drop(path, list, event):
    path.set(event.data)
    list.insert("end", event.data)



