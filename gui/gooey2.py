import customtkinter
from parser.parse_man import parse


def setupGUI():
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")

    def button_function():
        parse(
            "/home/ctrl/mcaps/KMS_data/test/",
            "./",
            "OMNI",
        )

    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="Parse", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()
