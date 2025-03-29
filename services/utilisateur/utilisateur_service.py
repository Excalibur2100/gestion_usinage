from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.models import Utilisateur
from db.schemas.schemas import UtilisateurCreate, UtilisateurUpdate
import bcrypt

# Service : Récupérer tous les utilisateurs
def get_utilisateurs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Utilisateur).offset(skip).limit(limit).all()

# Service : Récupérer un utilisateur par ID
def get_utilisateur_par_id(db: Session, utilisateur_id: int):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

# Service : Créer un nouvel utilisateur
def creer_utilisateur(db: Session, utilisateur_data: UtilisateurCreate):
    # Vérifie si l'email existe déjà
    utilisateur_existant = db.query(Utilisateur).filter(Utilisateur.email == utilisateur_data.email).first()
    if utilisateur_existant:
        raise HTTPException(status_code=400, detail="Un utilisateur avec cet email existe déjà")

    # Hashage sécurisé du mot de passe
    hashed_password = bcrypt.hashpw(utilisateur_data.mot_de_passe.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_utilisateur = Utilisateur(
        nom=utilisateur_data.nom,
        email=utilisateur_data.email,
        mot_de_passe=hashed_password,
        role=utilisateur_data.role
    )
    db.add(new_utilisateur)
    db.commit()
    db.refresh(new_utilisateur)
    return new_utilisateur

# Service : Mettre à jour un utilisateur
def update_utilisateur(db: Session, utilisateur_id: int, utilisateur_data: UtilisateurUpdate):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in utilisateur_data.dict(exclude_unset=True).items():
        if key == "mot_de_passe" and value:  # Si le mot de passe est mis à jour
            value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        setattr(utilisateur, key, value)

    db.commit()
    db.refresh(utilisateur)
    return utilisateur

# Service : Supprimer un utilisateur
def supprimer_utilisateur(db: Session, utilisateur_id: int):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    db.delete(utilisateur)
    db.commit()