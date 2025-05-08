from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.schemas.outils_schemas import OutilCreate, OutilRead, OutilUpdate
from db.models.database import get_db
from services.outil.outil_services import (
    creer_outil,
    get_tous_outils,
    get_outil_par_id,
    update_outil,
    supprimer_outil,
)

router = APIRouter(
    prefix="/outils",
    tags=["Outils"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=OutilRead, status_code=status.HTTP_201_CREATED)
async def create_outil(outil: OutilCreate, db: Session = Depends(get_db)):
    """
    Crée un nouvel outil.
    """
    return creer_outil(db, outil)

# ========== TOUS ==========
@router.get("/", response_model=List[OutilRead])
async def read_all_outils(db: Session = Depends(get_db)):
    """
    Récupère tous les outils.
    """
    return get_tous_outils(db)

# ========== PAR ID ==========
@router.get("/{outil_id}", response_model=OutilRead)
async def read_outil(outil_id: int, db: Session = Depends(get_db)):
    """
    Récupère un outil par son ID.
    """
    outil = get_outil_par_id(db, outil_id)
    if not outil:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Outil avec l'ID {outil_id} non trouvé."
        )
    return outil

# ========== MISE À JOUR ==========
@router.put("/{outil_id}", response_model=OutilRead)
async def update_outil_details(outil_id: int, outil: OutilUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un outil existant.
    """
    updated_outil = update_outil(db, outil_id, outil)
    if not updated_outil:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Outil avec l'ID {outil_id} non trouvé."
        )
    return updated_outil

# ========== SUPPRESSION ==========
@router.delete("/{outil_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_outil(outil_id: int, db: Session = Depends(get_db)):
    """
    Supprime un outil par son ID.
    """
    outil = get_outil_par_id(db, outil_id)
    if not outil:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Outil avec l'ID {outil_id} non trouvé."
        )
    supprimer_outil(db, outil_id)