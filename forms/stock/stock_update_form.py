import tkinter as tk
from tkinter import ttk, messagebox
from db.models.database import Database

class StockUpdateForm(tk.Toplevel):
    def __init__(self, parent, refresh_callback):
        super().__init__(parent)
        self.title("Mise à jour du stock")
        self.geometry("400x300")
        self.db = Database()
        self.refresh_callback = refresh_callback

        tk.Label(self, text="Rechercher un matériau", font=("Arial", 12, "bold")).pack(pady=10)

        # Recherche par Nom ou AFNOR
        tk.Label(self, text="Nom du Matériau:").pack()
        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack(fill="x", padx=10)

        tk.Label(self, text="Norme AFNOR:").pack()
        self.afnor_entry = tk.Entry(self)
        self.afnor_entry.pack(fill="x", padx=10)

        self.search_button = tk.Button(self, text="Rechercher", command=self.search_material)
        self.search_button.pack(pady=10)

        # Champ pour le stock actuel et l'ajout de stock
        self.stock_var = tk.StringVar()
        tk.Label(self, text="Stock actuel (mètres):").pack()
        self.stock_label = tk.Label(self, textvariable=self.stock_var, font=("Arial", 10, "bold"))
        self.stock_label.pack()

        tk.Label(self, text="Ajouter au stock (mètres):").pack()
        self.stock_entry = tk.Entry(self)
        self.stock_entry.pack(fill="x", padx=10)

        # Bouton de validation
        self.submit_button = tk.Button(self, text="Mettre à jour", command=self.update_stock, bg="green", fg="white")
        self.submit_button.pack(pady=10)

        self.selected_material = None  # Stocke l'ID du matériau sélectionné

    def search_material(self):
        """Rechercher un matériau en fonction du nom ou de la norme AFNOR"""
        nom = self.nom_entry.get().strip()
        afnor = self.afnor_entry.get().strip()

        if not nom and not afnor:
            messagebox.showerror("Erreur", "Veuillez entrer un nom ou une norme AFNOR.")
            return

        materials = self.db.search_material(nom, afnor)
        if not materials:
            messagebox.showerror("Erreur", "Aucun matériau trouvé.")
            return

        if len(materials) == 1:
            self.selected_material = materials[0][0]  # ID du matériau
            self.stock_var.set(f"{materials[0][1]} mm")  # Stock actuel
            messagebox.showinfo("Succès", f"Matériau trouvé : {materials[0][2]} ({materials[0][3]})")
        else:
            self.show_selection_list(materials)  # Afficher la liste de sélection

    def show_selection_list(self, materials):
        """Affiche une liste déroulante pour choisir le bon matériau."""
        selection_window = tk.Toplevel(self)
        selection_window.title("Sélectionnez un matériau")
        selection_window.geometry("300x200")

        tk.Label(selection_window, text="Choisissez un matériau :").pack(pady=5)

        self.material_var = tk.StringVar()
        material_names = [
            f"{mat[2]} ({mat[3]}) - {mat[1]} mm" if mat[3] is not None else f"{mat[2]} - {mat[1]} mm"
            for mat in materials
        ]

        self.material_combobox = ttk.Combobox(
            selection_window, values=material_names, textvariable=self.material_var
        )
        self.material_combobox.pack(pady=5)
        self.material_combobox.current(0)  # Sélectionne le premier par défaut

        def confirm_selection():
            selected_index = self.material_combobox.current()
            if selected_index == -1:
                messagebox.showerror("Erreur", "Veuillez sélectionner un matériau.")
                return
            
            self.selected_material = materials[selected_index][0]  # Récupère l'ID du matériau sélectionné
            self.stock_var.set(f"{materials[selected_index][1]} mm")
            selection_window.destroy()

        tk.Button(selection_window, text="Valider", command=confirm_selection, bg="green", fg="white").pack(pady=10)

    def update_stock(self):
        """Mettre à jour la quantité de stock du matériau"""
        if not self.selected_material:
            messagebox.showerror("Erreur", "Aucun matériau sélectionné.")
            return

        try:
            new_stock = float(self.stock_entry.get().strip())
            if new_stock <= 0:
                raise ValueError("Quantité invalide.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une quantité valide en mm.")
            return

        self.db.update_material_stock(self.selected_material, new_stock)
        messagebox.showinfo("Succès", "Stock mis à jour avec succès !")
        self.refresh_callback()
        self.destroy()
