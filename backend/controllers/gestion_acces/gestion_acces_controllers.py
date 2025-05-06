from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.gestion_acces_schemas import GestionAccesCreate, GestionAccesRead, GestionAccesUpdate
from backend.db.models.database import get_db
from backend.services.gestionacces.gestionacces_service import (
    creer_gestion_acces,
    get_toutes_gestions_acces,
    get_gestion_acces,
    mettre_a_jour_gestion_acces,
    supprimer_gestion_acces,
)

router = APIRouter(
    prefix="/gestion-acces",
    tags=["Gestion des accès"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=GestionAccesRead, status_code=status.HTTP_201_CREATED)
def creer(data: GestionAccesCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle gestion d'accès.
    """
    return creer_gestion_acces(db, data)

# ========== LISTER TOUS ==========
@router.get("/", response_model=List[GestionAccesRead])
def lire_tous(db: Session = Depends(get_db)):
    """
    Récupère toutes les gestions d'accès.
    """
    return get_toutes_gestions_acces(db)

# ========== LIRE UN ACCÈS ==========
@router.get("/{id}", response_model=GestionAccesRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    """
    Récupère une gestion d'accès par son ID.
    """
    acces = get_gestion_acces(db, id)
    if not acces:
        raise HTTPException(status_code=404, detail="Accès non trouvé")
    return acces

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=GestionAccesRead)
def maj_acces(id: int, data: GestionAccesUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une gestion d'accès existante.
    """
    acces = mettre_a_jour_gestion_acces(db, id, data)
    if not acces:
        raise HTTPException(status_code=404, detail="Accès non trouvé pour mise à jour")
    return acces

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer(id: int, db: Session = Depends(get_db)):
    """
    Supprime une gestion d'accès par son ID.
    """
    supprimer_gestion_acces(db, id)