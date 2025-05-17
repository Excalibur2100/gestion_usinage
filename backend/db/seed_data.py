from db.config.config_database import SessionLocal
from db.models.tables.securite.role_utilisateur import RoleUtilisateur
from backend.db.models.tables.securite.utilisateur import Utilisateur
from db.models.tables.crm.tag import Tag
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("seed")

def seed_roles(db):
    roles = [
        "admin", "comptable", "responsable_achat", "acheteur", "responsable_commercial",
        "commercial", "atelier", "chef_atelier", "controle_qualite", "responsable_qualite",
        "magasinier", "maintenance", "responsable_maintenance", "planificateur", "developpeur",
        "utilisateur_limite", "client_externe", "operateur_mobile"
    ]

    for role in roles:
        if not db.query(RoleUtilisateur).filter_by(nom=role).first():
            db.add(RoleUtilisateur(nom=role, description=f"Rôle système : {role}"))
            logger.info(f"✅ Rôle ajouté : {role}")
    db.commit()

def seed_admin(db):
    if not db.query(Utilisateur).filter_by(email="admin@usine.local").first():
        admin = Utilisateur(
            nom="Admin",
            email="admin@usine.local",
            mot_de_passe="admin123",  # 🔐 à hasher en production
            role_id=1
        )
        db.add(admin)
        db.commit()
        logger.info("✅ Utilisateur admin créé.")

def seed_tags(db):
    default_tags = ["VIP", "Prospect", "Inactif"]
    for tag in default_tags:
        if not db.query(Tag).filter_by(nom=tag).first():
            db.add(Tag(nom=tag))
            logger.info(f"✅ Tag ajouté : {tag}")
    db.commit()

def seed_all():
    db = SessionLocal()
    try:
        logger.info("🚀 Démarrage du seed initial...")
        seed_roles(db)
        seed_admin(db)
        seed_tags(db)
        logger.info("🎉 Seed terminé avec succès.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_all()
