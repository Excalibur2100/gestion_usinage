from pathlib import Path
import re

# Fonction pour nettoyer les noms de section
def sanitize(name):
    return re.sub(r'\W+', '_', name.strip().lower())

# Base dynamique
BASE_DIR = Path(__file__).resolve().parent
source_file = BASE_DIR / "schemas.py"
target_dir = BASE_DIR

# Assurez-vous que le dossier cible existe
target_dir.mkdir(parents=True, exist_ok=True)

# Lire le contenu
lines = source_file.read_text(encoding="utf-8").splitlines(keepends=True)

current_section = None
current_content = []

for line in lines:
    if line.strip().startswith("# ========================="):
        if current_section and current_content:
            filename = f"{sanitize(current_section)}_schemas.py"
            (target_dir / filename).write_text("".join(current_content), encoding="utf-8")
            print(f"Fichier créé : {filename}")

        current_section = line.strip().strip("# =").strip()
        current_content = [f"# Fichier généré automatiquement pour {current_section}\n\n"]
    else:
        if current_section:
            current_content.append(line)

# Dernier fichier
if current_section and current_content:
    filename = f"{sanitize(current_section)}_schemas.py"
    (target_dir / filename).write_text("".join(current_content), encoding="utf-8")
    print(f"Fichier créé : {filename}")

# Ajouter __init__.py
(target_dir / "__init__.py").touch()
