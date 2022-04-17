import tkinter as tk
from tkinter import E, ttk
from views.edit_status_description import EditStatusDescription
from models.status import StatusModel

class Top(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        status_model = StatusModel.find_by_id(1)
        print(status_model)
        print(status_model.description)
        frame = EditStatusDescription(status_model)
        frame.grid()