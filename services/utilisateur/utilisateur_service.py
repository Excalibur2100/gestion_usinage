from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.models import Utilisateur
from db.schemas.schemas import UtilisateurCreate
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
def creer_utilisateur(db: Session, utilisateur_data: UtilisateurCreate) -> Utilisateur:
    # Vérifie si l'utilisateur existe déjà
    if db.query(Utilisateur).filter(Utilisateur.email == utilisateur_data.email).first():
        raise HTTPException(status_code=400, detail="Un utilisateur avec cet email existe déjà.")
    
    utilisateur = Utilisateur(**utilisateur_data.model_dump())
    db.add(utilisateur)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

# Service : Mettre à jour un utilisateur
def update_utilisateur(db: Session, utilisateur_id: int, utilisateur_data: UtilisateurUpdate):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in utilisateur_data.model_dump(exclude_unset=True).items():
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