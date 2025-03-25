from sqlalchemy.orm import Session
from db.models.models import Utilisateur
from db.schemas.schemas import UtilisateurCreate
from typing import Optional
import bcrypt

# ========== CRÉATION ==========
def creer_utilisateur(db: Session, user_data: UtilisateurCreate) -> Utilisateur:
    hashed_password = bcrypt.hashpw(user_data.mot_de_passe.encode("utf-8"), bcrypt.gensalt())
    utilisateur = Utilisateur(
        nom=user_data.nom,
        email=user_data.email,
        mot_de_passe=hashed_password.decode("utf-8"),
        role=user_data.role,
        actif=user_data.actif
    )
    db.add(utilisateur)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

# ========== TOUS UTILISATEURS ==========
def get_tous_utilisateurs(db: Session):
    return db.query(Utilisateur).all()

# ========== UTILISATEUR PAR ID ==========
def get_utilisateur_par_id(db: Session, user_id: int):
    return db.query(Utilisateur).filter(Utilisateur.id == user_id).first()

# ========== SUPPRESSION ==========
def supprimer_utilisateur(db: Session, user_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

# ========== AUTHENTIFICATION UTILISATEUR ==========
def authentifier_utilisateur(db: Session, email: str, mot_de_passe: str) -> Optional[Utilisateur]:
    utilisateur = db.query(Utilisateur).filter(Utilisateur.email == email).first()
    if not utilisateur:
        return None
    if not utilisateur.check_password(mot_de_passe):
        return None
    return utilisateur

# ========== MISE À JOUR ==========
def update_utilisateur(db: Session, user_id: int, user_data: UtilisateurCreate):
    user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if user:
        user.nom = user_data.nom
        user.email = user_data.email
        user.role = user_data.role
        user.actif = user_data.actif
        db.commit()
        db.refresh(user)
    return user