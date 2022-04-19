import tkinter as tk
from tkinter import ttk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x400')
        self.resizable(0, 0)

        label = ttk.Label(self, text="Project name")
        label.grid(row=0, column=0, sticky="W")

        member_frame = Members(self)
        member_frame.grid(row=1, column=0, sticky='W')

        text = ttk.Entry(self)
        text.grid(row=2, column=0, sticky="W")

        button = ttk.Button(self, text="Save")
        button.grid(row=3, column=0, sticky="E")


class Members(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        members = ['Mario', 'Luigi', 'Yoshi']
        member_labels = [ttk.Label(self, text=member) for member in members]
        for i, l in enumerate(member_labels):
            l.grid(row=0, column=i, sticky="W")




if __name__ == '__main__':
    root = Top()
    root.mainloop()