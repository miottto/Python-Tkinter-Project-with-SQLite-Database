import tkinter as tk
from tkinter import *


class Welcome(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome")
        self.master.resizable(False, False)
        self.center_window(240, 120)

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')
         
        login_button = tk.Button(self, text="Login", width=10, command=self.open_login)
        login_button.pack(padx=20, pady=(20, 10))
         
        register_button = tk.Button(self, text="Register", width=10, command=self.open_register)
        register_button.pack(pady=10)
        self.pack()
         
    def open_login(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        from frames.login import Login
        Login(self.master)
         
    def open_register(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        from frames.register import Register
        Register(self.master)