from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.tables.utilisateur import Utilisateur
from db.schemas.utilisateur_schemas import UtilisateurCreate, UtilisateurUpdate
import bcrypt

def get_utilisateurs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Utilisateur).offset(skip).limit(limit).all()

def get_utilisateur_par_id(db: Session, utilisateur_id: int):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

def creer_utilisateur(db: Session, utilisateur_data: UtilisateurCreate) -> Utilisateur:
    if db.query(Utilisateur).filter(Utilisateur.email == utilisateur_data.email).first():
        raise HTTPException(status_code=400, detail="Un utilisateur avec cet email existe déjà.")
    
    hashed_password = bcrypt.hashpw(utilisateur_data.mot_de_passe.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    utilisateur = Utilisateur(
        nom=utilisateur_data.nom,
        email=utilisateur_data.email,
        role=utilisateur_data.role,
        actif=utilisateur_data.actif,
        mot_de_passe=hashed_password
    )
    db.add(utilisateur)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

def update_utilisateur(db: Session, utilisateur_id: int, utilisateur_data: UtilisateurUpdate):
    utilisateur = get_utilisateur_par_id(db, utilisateur_id)
    for key, value in utilisateur_data.dict(exclude_unset=True).items():
        if key == "mot_de_passe" and value:
            value = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        setattr(utilisateur, key, value)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

def supprimer_utilisateur(db: Session, utilisateur_id: int):
    utilisateur = get_utilisateur_par_id(db, utilisateur_id)
    db.delete(utilisateur)
    db.commit()