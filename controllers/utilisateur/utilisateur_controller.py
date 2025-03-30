from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import UtilisateurCreate, UtilisateurUpdate, UtilisateurRead
from services.utilisateur.utilisateur_service import (
    creer_utilisateur,
    get_utilisateurs,
    get_utilisateur_par_id,
    update_utilisateur,
    supprimer_utilisateur
)

# Initialisation du routeur
router = APIRouter(prefix="/utilisateurs", tags=["Utilisateurs"])

# Endpoint : Créer un nouvel utilisateur
# filepath: /home/excalibur/gestion_usinage/controllers/utilisateur/utilisateur_controller.py
@router.post("/", response_model=UtilisateurRead)
def creer(utilisateur_data: UtilisateurCreate, db: Session = Depends(get_db)):
    utilisateur = creer_utilisateur(db, utilisateur_data)
    return utilisateur

# Endpoint : Récupérer tous les utilisateurs
@router.get("/", response_model=list[UtilisateurRead], operation_id="list_utilisateurs_v1")
def lire_tous(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_utilisateurs(db, skip=skip, limit=limit)

# Endpoint : Récupérer un utilisateur par ID
@router.get("/{id}", response_model=UtilisateurRead, operation_id="get_utilisateur_v1")
def lire_un(id: int, db: Session = Depends(get_db)):
    utilisateur = get_utilisateur_par_id(db, id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

# Endpoint : Mettre à jour un utilisateur
@router.put("/{id}", response_model=UtilisateurRead, operation_id="update_utilisateur_v1")
def maj(id: int, utilisateur_data: UtilisateurUpdate, db: Session = Depends(get_db)):
    utilisateur = update_utilisateur(db, id, utilisateur_data)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé pour mise à jour")
    return utilisateur

# Endpoint : Supprimer un utilisateur
@router.delete("/{id}", status_code=204, operation_id="delete_utilisateur_v1")
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_utilisateur(db, id)
    return
