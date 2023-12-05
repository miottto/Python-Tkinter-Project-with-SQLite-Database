
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data_connect import database


class Collection(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Collection")
        self.master.resizable(True, True)
        self.create_menu()
        self.elements()
        self.center_window(900,720)
        
    def center_window(self, width, height):
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        options_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=options_menu)
        options_menu.add_command(label='Disconnect', command=self.disconnect)
        options_menu.add_command(label='Exit', command=self.master.quit)

    def disconnect(self):
        for widget in self.master.winfo_children():
            if widget != self:
                widget.destroy()
        self.destroy()
        from frames.welcome import Welcome
        Welcome(self.master)

    def elements(self):  
        lf_collection=tk.LabelFrame(self.master, text="BOOKS")
        lf_collection.pack(fill="both", expand= "yes", padx=10, pady=10)

        self.tv=ttk.Treeview(lf_collection, columns=('id', 'title', 'author', 'ISBN', 'available_quantity','user'), show='headings')
        self.tv.column('id', minwidth=0, width=30)
        self.tv.column('title', minwidth=0, width=270)
        self.tv.column('author', minwidth=0, width=100)
        self.tv.column('ISBN', minwidth=0, width=100)
        self.tv.column('available_quantity', minwidth=0, width=130)
        self.tv.column('user', minwidth=0, width=100)
        self.tv.heading('id', text='ID')
        self.tv.heading('title', text='TITLE')
        self.tv.heading('author', text='AUTHOR')
        self.tv.heading('ISBN', text='ISBN')
        self.tv.heading('available_quantity', text='AVAILABLE QUANTITY')
        self.tv.heading('user', text='USER' )
        self.tv.tk.call("ttk::setTheme", "clam")

        vsb = ttk.Scrollbar(lf_collection, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscrollcommand=vsb.set)
        self.tv.pack(side="left", fill="both", expand="yes", padx=(10,0), pady=10)
        vsb.pack(side="left", fill="y", padx=(0,10), pady=10)
       
        lf_newbook= tk.LabelFrame(self.master, text="ADD NEW BOOK")
        lf_newbook.pack(fill="both", expand="yes", padx=10, pady=10)

        lb_title=tk.Label(lf_newbook, text="Title")
        lb_title.pack(side="left")
        self.vtitle=tk.Entry(lf_newbook, width=40)
        self.vtitle.pack(side="left", padx=10)

        lb_author=tk.Label(lf_newbook, text="Author")
        lb_author.pack(side="left")
        self.vauthor=tk.Entry(lf_newbook, width=25)
        self.vauthor.pack(side="left", padx=10)

        lb_isbn=tk.Label(lf_newbook, text="ISBN")
        lb_isbn.pack(side="left")
        self.visbn=tk.Entry(lf_newbook, width=15)
        self.visbn.pack(side="left", padx=10)

        lb_quantity=tk.Label(lf_newbook, text="Available Quantity")
        lb_quantity.pack(side="left")
        self.vquantity=tk.Entry(lf_newbook, width=4)
        self.vquantity.pack(side="left", padx=10)

        btn_insert=tk.Button(lf_newbook, text="Insert", command=self.insert_book)
        btn_insert.pack(side="left")

        lb_search=tk.LabelFrame(self.master, text="SEARCH TITLE")
        lb_search.pack(fill="both", expand="yes", padx=10, pady=10)

        lb_title=tk.Label(lb_search, text="Title")
        lb_title.pack(side="left")

        self.search_title=tk.Entry(lb_search, width=40)
        self.search_title.pack(side="left", padx=10)

        btn_search=tk.Button(lb_search, text="Search", command=self.search_book)
        btn_search.pack(side="left", padx=10)

        btn_all=tk.Button(lb_search, text="Show All", command=self.populate)
        btn_all.pack(side="left", padx=10)

        btn_del=tk.Button(lb_search, text="Delete",command=self.delete_book)
        btn_del.pack(side="left",padx=10)
        
        self.populate()
        self.pack()

    def populate(self):
        self.tv.delete(*self.tv.get_children())
        vquery="SELECT * FROM all_books order by ID"
        self.tv.lines=database.dql(vquery)
        for i in self.tv.lines:
            self.tv.insert("", "end", values=i)

    def insert_book(self):
        if self.vtitle.get()=="" or self.vauthor.get()=="" or self.visbn.get()=="" or self.vquantity.get()=="":
            messagebox.showinfo(title="ERROR", message="Incomplete data. Fill in all spaces.")
            return
        try:
            from frames.login import rec_user
            vquery = "INSERT INTO all_books (Title, Author, ISBN, Available_Quantity, User) VALUES ('" + self.vtitle.get() + "', '" + self.vauthor.get() + "', '" + self.visbn.get() + "', '" + self.vquantity.get() + "', '" + rec_user + "')"
            database.dml(vquery)
        except:
            messagebox.showinfo(title="ERROR", message= "Cannot be inserted")
            return
        self.populate()
        self.vtitle.delete(0, tk.END)
        self.vauthor.delete(0, tk.END)
        self.visbn.delete(0, tk.END)
        self.vquantity.delete(0, tk.END)
        self.vtitle.focus()

    def delete_book(self):
        id_book=self.tv.selection()[0]
        val=self.tv.item(id_book, "values")
        vid=val[0]
        try:
            vquery="DELETE FROM all_books WHERE id="+vid
            database.dml(vquery)
        except:
            messagebox.showinfo(title="ERROR", message="Cannot be deleted")
            return
        self.tv.delete(id_book)

    def search_book(self):
        self.tv.delete(*self.tv.get_children())
        vquery="SELECT * FROM all_books WHERE Title LIKE '%"+self.search_title.get()+"%' order by ID"
        self.tv.lines=database.dql(vquery)
        for i in self.tv.lines:
            self.tv.insert("","end", values=i)

