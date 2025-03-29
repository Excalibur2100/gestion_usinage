import os

# Chemin de base pour les contrôleurs
base_path = "/home/excalibur/gestion_usinage/controllers"

# Liste des contrôleurs à vérifier ou créer
controllers = [
    "utilisateur/utilisateur_controller.py",
    "rh/rh_controller.py",
    "client/client_controller.py",
    "fournisseur/fournisseur_controller.py",
    "commande/commande_controller.py",
    "devis/devis_controller.py",
    "piece/piece_controller.py",
    "machine/machine_controller.py",
    "outil/outil_controller.py",
    "materiau/materiau_controller.py",
    "commande_piece_controller.py",
    "programme_piece_controller.py",
    "gamme_production_controller.py",
    "gestion_acces_controllers.py",
    "planning_employe_controller.py",
    "planning_machine_controller.py",
    "gestion_filtrage_controller.py",
    "pointage/pointage_controller.py",
    "maintenance/maintenance_controller.py",
    "charge_machine_controller.py",
    "surveillance_camera_controller.py",
    "controle_robot_controller.py",
    "assistant_ia_controller.py",
    "codegen_controller.py",
    "ia/router_ia.py",
]

# Création ou correction des fichiers minimalistes
for controller in controllers:
    file_path = os.path.join(base_path, controller)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Crée les dossiers si nécessaires
    with open(file_path, "w") as f:
        # Écrit un contenu minimaliste pour chaque contrôleur
        f.write(f"""from fastapi import APIRouter

router = APIRouter(prefix="/{controller.split('/')[0]}", tags=["{controller.split('/')[0].capitalize()}"])

@router.get("/")
async def get_{controller.split('/')[0]}():
    return {{"message": "Endpoint {controller.split('/')[0]} opérationnel"}}
""")
    print(f"Corrigé ou créé : {file_path}")