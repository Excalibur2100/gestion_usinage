from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.models.models import Utilisateur
from db.schemas.schemas import UtilisateurCreate, UtilisateurRead
from services.utilisateur.utilisateur_services import (
    creer_utilisateur,
    get_utilisateur_par_id,
    get_tous_utilisateurs,
    supprimer_utilisateur,
    update_utilisateur,
    authentifier_utilisateur
)

router = APIRouter(prefix="/utilisateurs", tags=["Utilisateurs"])

# ========== CRÉATION ==========
@router.post("/", response_model=UtilisateurRead)
def creer(user: UtilisateurCreate, db: Session = Depends(get_db)):
    return creer_utilisateur(db, user)

# ========== LISTE ==========
@router.get("/", response_model=list[UtilisateurRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_utilisateurs(db)

# ========== LECTURE PAR ID ==========
@router.get("/{id}", response_model=UtilisateurRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    db_user = get_utilisateur_par_id(db, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_user

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=UtilisateurRead)
def maj_utilisateur(id: int, user: UtilisateurCreate, db: Session = Depends(get_db)):
    return update_utilisateur(db, id, user)

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def suppression(id: int, db: Session = Depends(get_db)):
    supprimer_utilisateur(db, id)
    return

# ========== AUTHENTIFICATION ==========
@router.post("/login")
def login(user: UtilisateurCreate, db: Session = Depends(get_db)):
    utilisateur = authentifier_utilisateur(db, user.email, user.mot_de_passe)
    if not utilisateur:
        raise HTTPException(status_code=401, detail="Identifiants invalides")
    return {"message": "Authentification réussie", "utilisateur_id": utilisateur.id}