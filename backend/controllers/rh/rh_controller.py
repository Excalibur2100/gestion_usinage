from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.rh_schemas import RHCreate, RHRead, RHUpdate
from backend.db.models.database import get_db
from services.rh.rh_services import (
    creer_rh,
    get_tous_rh,
    get_rh_par_id,
    update_rh,
    supprimer_rh,
)

router = APIRouter(
    prefix="/rh",
    tags=["RH"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=RHRead, status_code=status.HTTP_201_CREATED)
async def create_rh(rh: RHCreate, db: Session = Depends(get_db)):
    """
    Crée un nouvel employé RH.
    """
    return creer_rh(db, rh)

# ========== TOUS ==========
@router.get("/", response_model=List[RHRead])
async def read_all_rh(db: Session = Depends(get_db)):
    """
    Récupère tous les employés RH.
    """
    return get_tous_rh(db)

# ========== PAR ID ==========
@router.get("/{rh_id}", response_model=RHRead)
async def read_rh(rh_id: int, db: Session = Depends(get_db)):
    """
    Récupère un employé RH par son ID.
    """
    rh = get_rh_par_id(db, rh_id)
    if not rh:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employé RH avec l'ID {rh_id} non trouvé."
        )
    return rh

# ========== MISE À JOUR ==========
@router.put("/{rh_id}", response_model=RHRead)
async def update_rh_details(rh_id: int, rh: RHUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un employé RH existant.
    """
    updated_rh = update_rh(db, rh_id, rh)
    if not updated_rh:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employé RH avec l'ID {rh_id} non trouvé."
        )
    return updated_rh

# ========== SUPPRESSION ==========
@router.delete("/{rh_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rh(rh_id: int, db: Session = Depends(get_db)):
    """
    Supprime un employé RH par son ID.
    """
    rh = get_rh_par_id(db, rh_id)
    if not rh:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employé RH avec l'ID {rh_id} non trouvé."
        )
    supprimer_rh(db, rh_id)