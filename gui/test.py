import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Complex Tkinter Program")
        self.geometry("400x300")

        # Initialize the frames
        self.frames = {}
        for F in (StartPage, LoginPage, DashboardPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame

            # Stack all the pages on top of each other
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the Application", font=("Helvetica", 16))
        label.pack(side="top", fill="x", pady=10)

        login_button = tk.Button(self, text="Login",
                                 command=lambda: controller.show_frame("LoginPage"))
        login_button.pack()

        exit_button = tk.Button(self, text="Exit", command=self.quit)
        exit_button.pack()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Please enter your credentials", font=("Helvetica", 16))
        label.pack(side="top", fill="x", pady=10)

        username_label = tk.Label(self, text="Username:")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self, text="Login",
                                 command=self.login)
        login_button.pack(pady=10)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"))
        back_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.controller.show_frame("DashboardPage")
        else:
            messagebox.showerror("Login Error", "Incorrect username or password")


class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the Dashboard", font=("Helvetica", 16))
        label.pack(side="top", fill="x", pady=10)

        logout_button = tk.Button(self, text="Logout",
                                  command=lambda: controller.show_frame("StartPage"))
        logout_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", command=self.quit)
        quit_button.pack()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
