import tkinter as tk
from data_connect import database
from tkinter import messagebox
from sqlite3 import Error
import hashlib
from frames.login import Login


class Register(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Register")
        self.master.resizable(False, False)
        self.center_window(320, 360)

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')

         
        tk.Label(self, text="First Name:").grid(row=0, column=0, sticky="w")
        self.first_name = tk.Entry(self, width=26)
        self.first_name.grid(row=0, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Last Name:").grid(row=1, column=0, sticky="w")
        self.last_name = tk.Entry(self, width=26)
        self.last_name.grid(row=1, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Password:").grid(row=2, column=0, sticky="w")
        self.password = tk.Entry(self, show="*", width=26)
        self.password.grid(row=2, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Email:").grid(row=3, column=0, sticky="w")
        self.email = tk.Entry(self, width=26)
        self.email.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        
        global gender
        gender= tk.StringVar()
        tk.Label(self, text="Gender:").grid(row=4, column=0, sticky="w")
        self.genderm = tk.Radiobutton(self, text='F',width=10, variable=gender, value='Female')
        self.genderm.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.genderf = tk.Radiobutton(self, text='M', width=10, variable=gender, value='Male')
        self.genderf.grid(row=4, column=1, padx=10, pady=10, sticky="w")
         
        tk.Label(self, text="Age:").grid(row=5, column=0, sticky="w")
        self.age = tk.Entry(self, width=10)
        self.age.grid(row=5, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Address:").grid(row=6, column=0, sticky="w")
        self.address = tk.Text(self, width=20, height=3)
        self.address.grid(row=6, column=1, padx=10, pady=10, sticky="e")
         
        submit_button = tk.Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=7, column=1, sticky="e",padx=10, pady=10)
 
        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.grid(row=7, column=0, sticky="w", padx=10, pady=10)
        self.pack()
    

    def submit(self):

        def hash_password(password):
            hashed_pass=hashlib.sha256(password.encode()).hexdigest()
            return hashed_pass
        
        def get_selected_gender():
            return gender.get()
        
        data = {}
        data["firstName"] = self.first_name.get()
        data["lastName"] = self.last_name.get()
        data["password"] = hash_password(self.password.get())
        data["email"] = self.email.get()
        data["gender"] = get_selected_gender()
        data["age"] = self.age.get()
        data["address"] = self.address.get(1.0, tk.END)
    
        if self.first_name.get()=="" or self.last_name.get()=="" or self.password.get()=="" or self.email.get()=="" or get_selected_gender()=="" or self.age.get()=="" or self.address.get(1.0, tk.END)=="":
            messagebox.showinfo(title="ERROR", message="Incomplete data. Fill in all spaces.")
            return
        try:
            database.register(data)
            tk.messagebox.showinfo(title="Success", message="Your account has been created.")    
        except Error as ex:
            print(ex)
        self.destroy_widgets()
        self.destroy()
        Login(self.master)

    def destroy_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        from frames.welcome import Welcome
        Welcome(self.master)