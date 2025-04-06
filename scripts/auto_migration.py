import subprocess

def run_alembic_upgrade():
    """
    Automatisation de la commande Alembic pour appliquer les migrations.
    """
    try:
        print("Application des migrations Alembic...")
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Migrations appliquées avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'application des migrations : {e}")
    except FileNotFoundError:
        print("Erreur : Alembic n'est pas installé ou introuvable.")

if __name__ == "__main__":
    run_alembic_upgrade()