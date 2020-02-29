import tkinter as tk
from tkinter import ttk
import pandas as pd

from back import DataF

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack(side='top', fill='both', expand=True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(window, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, win):
        frame = self.frames[win]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.dataframe = DataF('1460_amazon_reviews.csv')

        label = tk.Label(self, text=self.dataframe.get_row(0), font=("Verdana", 12))
        label.pack(pady=10, padx=10)


app = Application()
app.mainloop()

    


