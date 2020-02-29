import tkinter as tk
from tkinter import ttk
import pandas as pd

from back import DataF

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "NLP Annotation tool")
        tk.Tk.geometry(self, '1400x500')

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
        tk.Frame.__init__(self, parent, relief='sunken', borderwidth=2)

        self.dataframe = DataF('1460_amazon_reviews.csv')

        cat = tk.StringVar()
        category = ttk.Entry(self, textvariable=cat)
        category.grid(column=0, row=1, sticky=tk.W)
        print(category.get())

        label = ttk.Label(self, text=self.dataframe.get_row(0), font=("Verdana", 12))
        label.grid(column=0, row=0, sticky=tk.N)

        button1 = ttk.Button(self, text='a', width=70)
        button1.grid(column=0, row=3)

        button2 = ttk.Button(self, text='b', width=70)
        button2.grid(column=2, row=3)

        button3 = ttk.Button(self, text='c', width=70, command="hello")
        button3.grid(column=0, row=6)

        button4 = ttk.Button(self, text='d', width=70)
        button4.grid(column=2, row=6)


app = Application()
app.mainloop()

    


