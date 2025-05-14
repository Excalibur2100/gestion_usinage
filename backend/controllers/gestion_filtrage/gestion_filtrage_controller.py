from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.gestion_filtrage_schemas.gestion_filtrage_schemas import GestionFiltrageCreate, GestionFiltrageRead
from db.models.database import get_db
from backend.services.qualite.gestionfiltrage_service import (
    creer_filtrage,
    get_tous_filtrages,
    get_filtrage_par_id,
    supprimer_filtrage,
)

router = APIRouter(
    prefix="/gestion-filtrage",
    tags=["Gestion Filtrage"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=GestionFiltrageRead, status_code=status.HTTP_201_CREATED)
def creer(data: GestionFiltrageCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau filtrage.
    """
    return creer_filtrage(db, data)

# ========== LISTER TOUS ==========
@router.get("/", response_model=List[GestionFiltrageRead])
def lire_tous(db: Session = Depends(get_db)):
    """
    Récupère tous les filtrages.
    """
    return get_tous_filtrages(db)

# ========== LIRE UN FILTRAGE ==========
@router.get("/{id}", response_model=GestionFiltrageRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    """
    Récupère un filtrage par son ID.
    """
    filtrage = get_filtrage_par_id(db, id)
    if not filtrage:
        raise HTTPException(status_code=404, detail="Filtrage non trouvé")
    return filtrage

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer(id: int, db: Session = Depends(get_db)):
    """
    Supprime un filtrage par son ID.
    """
    filtrage = get_filtrage_par_id(db, id)
    if not filtrage:
        raise HTTPException(status_code=404, detail="Filtrage non trouvé")
    supprimer_filtrage(db, id)