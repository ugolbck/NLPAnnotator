import tkinter as tk
from tkinter import ttk
import pandas as pd

from back import DataF

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Part Manager')
        # Width height
        master.geometry("700x350")

    def load_frame(self, frame):
        frame_field = tk.Label(self, text=frame.__str__())
        frame_field.grid(row=0, column=0)

app = Application(master=tk.Tk())

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

app.load_frame(DataF(df))



app.mainloop()