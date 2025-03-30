import os
import subprocess
import sys
from dotenv import load_dotenv
import os

# Charger le fichier config.env
load_dotenv()

# Vérification
print("🔹 Database User:", os.getenv("DATABASE_USER"))
print("🔹 Database Name:", os.getenv("DATABASE_NAME"))

def check_python():
    """ Vérifie la version de Python """
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ est requis !")
        sys.exit(1)

def check_postgres():
    """ Vérifie si PostgreSQL est en cours d’exécution """
    try:
        result = subprocess.run(["pg_isready"], capture_output=True, text=True)
        if "accepting connections" not in result.stdout:
            print("❌ PostgreSQL n’est pas lancé ! Démarre le serveur avant de continuer.")
            sys.exit(1)
    except FileNotFoundError:
        print("❌ `pg_isready` non trouvé. Vérifie que PostgreSQL est installé.")
        sys.exit(1)

def install_requirements():
    """ Installe les dépendances dans l’environnement virtuel """
    try:
        print("📦 Activation de l’environnement virtuel...")
        print("📦 Installation des dépendances...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation des dépendances : {e}")
        sys.exit(1)

def setup_database():
    """ Initialise la base de données PostgreSQL """
    try:
        print("🛠️ Initialisation de la base de données...")
        subprocess.run([sys.executable, "scripts/init_db.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'initialisation de la base de données : {e}")
        sys.exit(1)

def run_tests():
    """ Vérifie si les tests passent avant le lancement """
    print("✅ Exécution des tests unitaires...")
    result = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("❌ Des tests ont échoué, vérifie les erreurs avant de continuer.")
        sys.exit(1)

def launch_application():
    """ Lance l’application """
    print("🚀 Lancement de l’application...")
    subprocess.run([sys.executable, "main.py"])  # Remplace `main.py` par ton fichier de lancement principal

if __name__ == "__main__":
    check_python()
    check_postgres()  # 🔥 Vérification PostgreSQL
    install_requirements()
    setup_database()
    run_tests()
    launch_application()
