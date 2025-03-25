# controllers/gestion_acces_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import GestionAccesCreate, GestionAccesRead
from services.securite.gestion_acces_services import (
    creer_gestion_acces,
    get_tous_gestion_acces,
    get_gestion_acces_par_id,
    update_gestion_acces,
    supprimer_gestion_acces
)

router = APIRouter(prefix="/gestion-acces", tags=["Gestion des accès"])

# ========== CRÉATION ========== 
@router.post("/", response_model=GestionAccesRead)
def creer(data: GestionAccesCreate, db: Session = Depends(get_db)):
    return creer_gestion_acces(db, data)

# ========== LISTER TOUS ========== 
@router.get("/", response_model=list[GestionAccesRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_gestion_acces(db)

# ========== LIRE UN ACCÈS ========== 
@router.get("/{id}", response_model=GestionAccesRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    acces = get_gestion_acces_par_id(db, id)
    if not acces:
        raise HTTPException(status_code=404, detail="Accès non trouvé")
    return acces

# ========== MISE À JOUR ========== 
@router.put("/{id}", response_model=GestionAccesRead)
def maj_acces(id: int, data: GestionAccesCreate, db: Session = Depends(get_db)):
    acces = update_gestion_acces(db, id, data)
    if not acces:
        raise HTTPException(status_code=404, detail="Accès non trouvé pour mise à jour")
    return acces

# ========== SUPPRESSION ========== 
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_gestion_acces(db, id)
    return