from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.tables.utilisateur import Utilisateur
from db.schemas.utilisateur_schemas import UtilisateurCreate, UtilisateurUpdate
from passlib.context import CryptContext

# Configuration de Passlib pour le hachage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_utilisateurs(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée d'utilisateurs.
    """
    return db.query(Utilisateur).offset(skip).limit(limit).all()

def get_utilisateur_par_id(db: Session, utilisateur_id: int):
    """
    Récupère un utilisateur par son ID.
    """
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

def creer_utilisateur(db: Session, utilisateur_data: UtilisateurCreate) -> Utilisateur:
    """
    Crée un nouvel utilisateur avec un mot de passe haché.
    """
    hashed_password = pwd_context.hash(utilisateur_data.mot_de_passe)
    utilisateur = Utilisateur(
        nom=utilisateur_data.nom,
        email=utilisateur_data.email,
        mot_de_passe=hashed_password,
        role=utilisateur_data.role,
        actif=True
    )
    db.add(utilisateur)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

def update_utilisateur(db: Session, utilisateur_id: int, utilisateur_data: UtilisateurUpdate):
    """
    Met à jour les informations d'un utilisateur existant.
    """
    utilisateur = get_utilisateur_par_id(db, utilisateur_id)
    if utilisateur_data.nom:
        utilisateur.nom = utilisateur_data.nom
    if utilisateur_data.email:
        utilisateur.email = utilisateur_data.email
    if utilisateur_data.mot_de_passe:
        utilisateur.mot_de_passe = pwd_context.hash(utilisateur_data.mot_de_passe)
    if utilisateur_data.role:
        utilisateur.role = utilisateur_data.role
    if utilisateur_data.actif is not None:
        utilisateur.actif = utilisateur_data.actif
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

def supprimer_utilisateur(db: Session, utilisateur_id: int):
    """
    Supprime un utilisateur par son ID.
    """
    utilisateur = get_utilisateur_par_id(db, utilisateur_id)
    db.delete(utilisateur)
    db.commit()