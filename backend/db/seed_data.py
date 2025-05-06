from passlib.context import CryptContext  # Import tiers
from db.models.database import SessionLocal  # Import interne
from db.models.tables.utilisateur import Utilisateur  # Import interne

# Configuration de Passlib pour utiliser bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def seed_data():
    db = SessionLocal()
    try:
        # Vérifier si un utilisateur admin existe déjà
        existing_admin = (
            db.query(Utilisateur).filter_by(email="admin@example.com").first()
        )
        if existing_admin:
            print("Un utilisateur admin existe déjà. Aucune donnée n'a été ajoutée.")
        else:
            # Ajouter un utilisateur admin
            admin = Utilisateur(
                nom="Admin",
                email="admin@example.com",
                mot_de_passe=pwd_context.hash(
                    "admin_password"
                ),  # Hachage du mot de passe
                role="admin",
                actif=True,
            )
            db.add(admin)
            print("Utilisateur admin ajouté.")

        # Ajouter un utilisateur standard
        existing_user = (
            db.query(Utilisateur).filter_by(email="user@example.com").first()
        )
        if not existing_user:
            user = Utilisateur(
                nom="Utilisateur",
                email="user@example.com",
                mot_de_passe=pwd_context.hash(
                    "user_password"
                ),  # Hachage du mot de passe
                role="user",
                actif=True,
            )
            db.add(user)
            print("Utilisateur standard ajouté.")
        else:
            print("Un utilisateur standard existe déjà. Aucune donnée n'a été ajoutée.")

        # Commit des modifications
        db.commit()
        print("Données initiales insérées avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
