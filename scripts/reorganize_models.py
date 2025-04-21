import os
import re

# Chemins des dossiers
BASE_DIR = "/home/excalibur/gestion_usinage/db/models"
MODELS_FILE = os.path.join(BASE_DIR, "models.py")
TABLES_DIR = os.path.join(BASE_DIR, "tables")
INIT_FILE = os.path.join(TABLES_DIR, "__init__.py")

# Dictionnaire pour mapper les classes à leurs fichiers
DOMAIN_MAPPING = {
    "Utilisateur": "utilisateur.py",
    "Droit": "utilisateur.py",
    "DroitAcces": "utilisateur.py",
    "GestionAcces": "utilisateur.py",
    "HistoriqueAction": "utilisateur.py",
    "RH": "rh.py",
    "Absence": "rh.py",
    "Formation": "rh.py",
    "Sanction": "rh.py",
    "Entretien": "rh.py",
    "NotationRH": "rh.py",
    "DocumentRH": "rh.py",
    "Client": "clients.py",
    "Fournisseur": "clients.py",
    "EvaluationFournisseur": "clients.py",
    "Devis": "devis.py",
    "Commande": "devis.py",
    "CommandePiece": "devis.py",
    "Facture": "devis.py",
    "LigneFacture": "devis.py",
    "Piece": "production.py",
    "ProgrammePiece": "production.py",
    "PostProcesseur": "production.py",
    "Machine": "production.py",
    "Maintenance": "production.py",
    "Outil": "stock.py",
    "Materiau": "stock.py",
    "GammeProduction": "production.py",
    "Tracabilite": "production.py",
    "PlanningEmploye": "planning.py",
    "PlanningMachine": "planning.py",
    "AffectationMachine": "planning.py",
    "Pointage": "planning.py",
    "InstrumentControle": "qhse.py",
    "ControlePiece": "qhse.py",
    "EPI": "qhse.py",
    "EPIUtilisateur": "qhse.py",
    "AuditQualite": "qhse.py",
    "NonConformite": "qhse.py",
    "DocumentQualite": "qhse.py",
    "DocumentReglementaire": "qhse.py",
    "Finance": "finance.py",
    "StatFinance": "finance.py",
    "GestionFiltrage": "systeme.py",
    "QrCodeObjet": "systeme.py",
    "SurveillanceCamera": "systeme.py",
    "Robotique": "systeme.py",
    "ControleRobot": "systeme.py",
}


# Fonction pour créer les fichiers nécessaires
def create_files():
    if not os.path.exists(TABLES_DIR):
        os.makedirs(TABLES_DIR)
    for filename in set(DOMAIN_MAPPING.values()):
        filepath = os.path.join(TABLES_DIR, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(
                    "# Auto-generated file for models\n\nfrom db.models.base import Base\n\n"
                )


# Fonction pour extraire les classes du fichier models.py
def extract_classes():
    with open(MODELS_FILE, "r") as f:
        content = f.read()

    # Regex pour extraire les classes
    class_pattern = re.compile(r"class (\w+)\(Base\):\n(.*?)(?=\nclass|\Z)", re.S)
    classes = class_pattern.findall(content)

    return classes


# Fonction pour répartir les classes dans les fichiers correspondants
def distribute_classes(classes):
    for class_name, class_body in classes:
        if class_name in DOMAIN_MAPPING:
            filename = DOMAIN_MAPPING[class_name]
            filepath = os.path.join(TABLES_DIR, filename)
            with open(filepath, "a") as f:
                f.write(f"class {class_name}(Base):\n{class_body.strip()}\n\n")


# Fonction pour générer le fichier __init__.py
def generate_init_file():
    imports = []
    for class_name, filename in DOMAIN_MAPPING.items():
        module_name = filename.replace(".py", "")
        imports.append(f"from .{module_name} import {class_name}")
    with open(INIT_FILE, "w") as f:
        f.write("# Auto-generated __init__.py for models\n\n")
        f.write("\n".join(imports))
        f.write("\n\n__all__ = [\n")
        f.write(
            ",\n".join(f'    "{class_name}"' for class_name in DOMAIN_MAPPING.keys())
        )
        f.write("\n]\n")


# Fonction principale
def main():
    print("Réorganisation des modèles...")
    create_files()
    classes = extract_classes()
    distribute_classes(classes)
    generate_init_file()
    print("Réorganisation terminée avec succès !")


if __name__ == "__main__":
    main()
