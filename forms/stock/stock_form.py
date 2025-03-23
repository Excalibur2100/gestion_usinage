import tkinter as tk
from tkinter import ttk, messagebox
from db.models.database import Database

class StockForm(tk.Toplevel):
    def __init__(self, parent, refresh_callback, materiau_data=None):
        super().__init__(parent)
        self.title("Ajouter / Modifier un Matériau")
        self.geometry("400x600")
        self.refresh_callback = refresh_callback
        self.materiau_data = materiau_data
        self.db = Database()

        # Titre
        tk.Label(self, text="Formulaire Matériaux", font=("Arial", 14, "bold")).pack(pady=10)

        # Champs du formulaire
        fields = [
            ("Nom", "nom"),
            ("AFNOR", "afnor"),
            ("Diamètre Rond (mm)", "rond_diametre"),
            ("Côté Carré (mm)", "carre"),
            ("Largeur Plat (mm)", "plat_largeur"),
            ("Epaisseur (mm)", "epaisseur"),
            ("Stock (mètres)", "stock"),
            ("Type", "type"),
            ("Dureté", "durete")
        ]

        self.entries = {}
        for label, field in fields:
            row = tk.Frame(self)
            row.pack(fill="x", padx=10, pady=5)
            tk.Label(row, text=label).pack(side="left")
            entry = tk.Entry(row)
            entry.pack(side="right", fill="x", expand=True)
            self.entries[field] = entry

        # Liste déroulante pour le fournisseur
        tk.Label(self, text="Fournisseur").pack(pady=5)
        self.fournisseur_var = tk.StringVar()
        self.fournisseur_dropdown = ttk.Combobox(self, textvariable=self.fournisseur_var)
        self.fournisseur_dropdown.pack(fill="x", padx=10)
        self.load_fournisseurs()

        # Boutons
        self.submit_button = tk.Button(self, text="Enregistrer", command=self.save_data, bg="green", fg="white")
        self.submit_button.pack(pady=10)

        if self.materiau_data:
            self.populate_fields()

    def load_fournisseurs(self):
        """Charge la liste des fournisseurs depuis la base de données."""
        fournisseurs = self.db.lister_fournisseurs()
        fournisseur_names = [f[1] for f in fournisseurs]  # On récupère uniquement les noms
        self.fournisseur_dropdown["values"] = fournisseur_names

    def populate_fields(self):
        """Remplit les champs si modification d'un matériau existant."""
        for field, entry in self.entries.items():
            entry.insert(0, str(self.materiau_data.get(field, "")))

        fournisseur_id = self.materiau_data.get("fournisseur_id")
        fournisseur_nom = self.db.get_fournisseur_nom(fournisseur_id) if fournisseur_id else ""
        self.fournisseur_var.set(fournisseur_nom)

    def save_data(self):
        """Enregistre les données dans la base de données."""
        materiau = {field: self.entries[field].get() for field in self.entries}
        fournisseur_nom = self.fournisseur_var.get()
        materiau["fournisseur_id"] = self.db.get_fournisseur_id(fournisseur_nom) if fournisseur_nom else None

        if self.materiau_data:
            self.db.modifier_materiau(self.materiau_data['id'], **materiau)
            messagebox.showinfo("Succès", "Matériau modifié avec succès !")
        else:
            self.db.ajouter_materiau(**materiau)
            messagebox.showinfo("Succès", "Matériau ajouté avec succès !")

        self.refresh_callback()
        self.destroy()
