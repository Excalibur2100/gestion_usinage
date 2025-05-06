import tkinter as tk

class ProductionView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestion de la Production")
        self.geometry("600x400")

        tk.Label(self, text="Gestion de la Production", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self, text="Ici, vous pourrez gérer la production.").pack(pady=10)

        tk.Button(self, text="Fermer", command=self.destroy).pack(pady=10)
