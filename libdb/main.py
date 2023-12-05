import tkinter as tk

from data_connect import database
from frames.welcome import Welcome


if __name__ == "__main__":

    con = database.connect_database()

    root = tk.Tk()
    Welcome(root)
    root.mainloop()
