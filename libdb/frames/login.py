import tkinter as tk
from tkinter import messagebox
from data_connect import database
import hashlib


class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.resizable(False, False)
        self.center_window(240, 140)

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')
         
        tk.Label(self, text="E-mail:").grid(row=0, column=0)
        self.username = tk.Entry(self)
        self.username.grid(row=0, column=1, padx=10, pady=10)
         
        tk.Label(self, text="Password:").grid(row=1, column=0)
        self.password = tk.Entry(self, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)
         
        submit_button = tk.Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=20)
 
        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.grid(row=2, column=0, sticky="w", padx=10, pady=20)
        self.pack()
             
    def submit(self):

        def hash_password(password):
            hashed_pass=hashlib.sha256(password.encode()).hexdigest()
            return hashed_pass
        
        if self.username.get()=="":
             messagebox.showinfo(title="Can't connect", message="Please enter an email.")
             return
            
        elif self.password.get()=="":
            messagebox.showinfo(title="Can't connect", message="Please enter a password.")
            return
       
        data = {}
        data["email"] = self.username.get()
        data["password"] = hash_password(self.password.get())
        print(f"Email: {data['email']}, Password: {data['password']}")
        
        try:   
            if  database.login(data) is True:
                global rec_user 
                rec_user = self.username.get()
                print("successful login")
                for widget in self.winfo_children(): 
                    widget.destroy()
                self.destroy()
                from frames.collection import Collection
                Collection(self.master)
                return
            else:
                tk.messagebox.showerror(title="Error", message="Incorrect email or password.")
                return
        except Exception as e:
            print(f"Error during login: {e}")
        tk.messagebox.showerror(title="Error", message="An error occurred during login.")
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        from frames.welcome import Welcome
        Welcome(self.master)