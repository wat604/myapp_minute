import tkinter as tk
from tkinter import ttk
from models.members import MemberModel

class EditStatusDescription(ttk.Frame):
    def __init__(self, status_model, **kwargs):
        super().__init__(**kwargs)

        description = tk.StringVar()
        description.set(status_model.description)

        project_label = ttk.Label(self, text=status_model.project)

        member_models = MemberModel.find_by_status_id(status_model.id)
        member_labels = []
        for member in member_models:
            member_labels.append(
                ttk.Label(self, text=member.name)
            )
        
        description_entry = tk.Entry(self, textvariable=description, width=40)

        project_label.pack(side='top')
        
        for member_label in member_labels:
            member_label.pack(side='left')
        
        description_entry.pack(side='top')