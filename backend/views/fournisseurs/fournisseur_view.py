import tkinter as tk
from tkinter import ttk

class FournisseurView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        ttk.Label(self, text="Gestion des fournisseur").pack(pady=20)
