import customtkinter
import tkinter
from customtkinter import filedialog
# from tkinterdnd2 import TkinterDnD # He is fucked on my install rn

# Setup all our static elements
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("400x780")
app.title("MCAP Parser utility")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=0, padx=0, fill="both", expand=True)

header = customtkinter.CTkLabel(master=frame, text="MCAP Parser")
header.pack(anchor="w", pady=10, padx=10)

subheader = customtkinter.CTkLabel(master=frame, text="")
subheader.pack(anchor="w", pady=10, padx=10)

target = None
dest = None


def run_gui(parse):
    def source_callback():
        global target  # I love python scope

        if recurse_toggle.get():
            target = filedialog.askdirectory()
        else:
            target = filedialog.askopenfilename()

        header.configure(text=target)

    file_pick = customtkinter.CTkButton(
        master=frame,
        command=source_callback,
        text="Pick source file path",
    )
    file_pick.pack(anchor="w", pady=10, padx=10)

    def dest_callback():
        global dest
        dest = filedialog.askdirectory()
        subheader.configure(text=dest)

    file_pick = customtkinter.CTkButton(
        master=frame,
        command=dest_callback,
        text="Pick output file path",
    )
    file_pick.pack(anchor="w", pady=10, padx=10)

    parsemenu = customtkinter.CTkOptionMenu(frame, values=["TVN", "OMNI", "LD"])
    parsemenu.pack(anchor="w", pady=10, padx=10)
    parsemenu.set("Output type")

    recurse_toggle = customtkinter.CTkSwitch(master=frame, text="Enable recursion")
    recurse_toggle.pack(anchor="w", pady=10, padx=10)

    mutlithread_toggle = customtkinter.CTkSwitch(
        master=frame, text="Enable multithreading (experimental)"
    )
    mutlithread_toggle.pack(anchor="w", pady=10, padx=10)

    def parse_callback():
        if (target is None) or (dest is None):
            header.configure(text="Pick a source and output path first")
        else:
            if parsemenu.get() == "Output type":
                header.configure(text="Pick a output type first")
            else:
                parse(
                    target,
                    dest,
                    parsemenu.get(),
                    recurse_toggle.get(),
                    mutlithread_toggle.get(),
                )

    file_pick = customtkinter.CTkButton(
        master=frame,
        command=parse_callback,
        text="Parse selected",
    )
    file_pick.pack(anchor="w", pady=10, padx=10)

    # Fix this shit later
    # progress = customtkinter.CTkProgressBar(master=frame)
    # progress.pack(pady=10, padx=10)

    app.mainloop()
