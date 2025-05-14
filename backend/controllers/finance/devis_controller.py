from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.finance.devis_schemas import DevisCreate, DevisRead, DevisUpdate
from db.models.database import get_db
from backend.services.finance.devis_services import (
    creer_devis,
    get_tous_devis,
    get_devis_par_id,
    update_devis,
    supprimer_devis,
)

router = APIRouter(
    prefix="/devis",
    tags=["Devis"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=DevisRead, status_code=status.HTTP_201_CREATED)
async def create_devis(devis: DevisCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau devis.
    """
    return creer_devis(db, devis)

# ========== TOUS ==========
@router.get("/", response_model=List[DevisRead])
async def read_all_devis(db: Session = Depends(get_db)):
    """
    Récupère tous les devis.
    """
    return get_tous_devis(db)

# ========== PAR ID ==========
@router.get("/{devis_id}", response_model=DevisRead)
async def read_devis(devis_id: int, db: Session = Depends(get_db)):
    """
    Récupère un devis par son ID.
    """
    devis = get_devis_par_id(db, devis_id)
    if not devis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Devis avec l'ID {devis_id} non trouvé."
        )
    return devis

# ========== MISE À JOUR ==========
@router.put("/{devis_id}", response_model=DevisRead)
async def update_devis_details(devis_id: int, devis: DevisUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un devis existant.
    """
    updated_devis = update_devis(db, devis_id, devis)
    if not updated_devis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Devis avec l'ID {devis_id} non trouvé."
        )
    return updated_devis

# ========== SUPPRESSION ==========
@router.delete("/{devis_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_devis(devis_id: int, db: Session = Depends(get_db)):
    """
    Supprime un devis par son ID.
    """
    devis = get_devis_par_id(db, devis_id)
    if not devis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Devis avec l'ID {devis_id} non trouvé."
        )
    supprimer_devis(db, devis_id)