from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.pointage_schemas import PointageCreate, PointageRead, PointageUpdate
from backend.db.models.database import get_db
from services.pointage.pointage_services import (
    creer_pointage,
    get_tous_pointages,
    get_pointage_par_id,
    update_pointage,
    supprimer_pointage,
)

router = APIRouter(
    prefix="/pointages",
    tags=["Pointages"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=PointageRead, status_code=status.HTTP_201_CREATED)
async def create_pointage(pointage: PointageCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau pointage.
    """
    return creer_pointage(db, pointage)

# ========== TOUS ==========
@router.get("/", response_model=List[PointageRead])
async def read_all_pointages(db: Session = Depends(get_db)):
    """
    Récupère tous les pointages.
    """
    return get_tous_pointages(db)

# ========== PAR ID ==========
@router.get("/{pointage_id}", response_model=PointageRead)
async def read_pointage(pointage_id: int, db: Session = Depends(get_db)):
    """
    Récupère un pointage par son ID.
    """
    pointage = get_pointage_par_id(db, pointage_id)
    if not pointage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pointage avec l'ID {pointage_id} non trouvé."
        )
    return pointage

# ========== MISE À JOUR ==========
@router.put("/{pointage_id}", response_model=PointageRead)
async def update_pointage_details(pointage_id: int, pointage: PointageUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un pointage existant.
    """
    updated_pointage = update_pointage(db, pointage_id, pointage)
    if not updated_pointage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pointage avec l'ID {pointage_id} non trouvé."
        )
    return updated_pointage

# ========== SUPPRESSION ==========
@router.delete("/{pointage_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pointage(pointage_id: int, db: Session = Depends(get_db)):
    """
    Supprime un pointage par son ID.
    """
    pointage = get_pointage_par_id(db, pointage_id)
    if not pointage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pointage avec l'ID {pointage_id} non trouvé."
        )
    supprimer_pointage(db, pointage_id)