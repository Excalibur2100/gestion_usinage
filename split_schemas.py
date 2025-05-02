import os

# Chemin du fichier source
source_file = "/home/excalibur/gestion_usinage/db/schemas/schemas.py"

# Dossier cible pour les fichiers divisés
target_dir = "/home/excalibur/gestion_usinage/db/schemas/"

# Assurez-vous que le dossier cible existe
os.makedirs(target_dir, exist_ok=True)

# Lire le contenu du fichier source
with open(source_file, "r") as f:
    lines = f.readlines()

# Variables pour suivre les sections
current_section = None
current_content = []

# Parcourir les lignes du fichier
for line in lines:
    # Identifier les sections basées sur les commentaires
    if line.strip().startswith("# ========================="):
        # Sauvegarder la section précédente dans un fichier
        if current_section and current_content:
            filename = f"{current_section.lower()}_schemas.py"
            with open(os.path.join(target_dir, filename), "w") as section_file:
                section_file.writelines(current_content)
            print(f"Fichier créé : {filename}")
        
        # Démarrer une nouvelle section
        current_section = line.strip().strip("# =").strip().replace(" ", "_").lower()
        current_content = [f"# Fichier généré automatiquement pour {current_section}\n\n"]
    else:
        # Ajouter les lignes à la section actuelle
        if current_section:
            current_content.append(line)

# Sauvegarder la dernière section
if current_section and current_content:
    filename = f"{current_section.lower()}_schemas.py"
    with open(os.path.join(target_dir, filename), "w") as section_file:
        section_file.writelines(current_content)
    print(f"Fichier créé : {filename}")