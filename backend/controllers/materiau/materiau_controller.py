from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.materiaux_schemas import MateriauCreate, MateriauRead, MateriauUpdate
from backend.db.models.database import get_db
from backend.services.materiau.materiau_services import (
    creer_materiau,
    get_tous_materiaux,
    get_materiau_par_id,
    update_materiau,
    supprimer_materiau,
)

router = APIRouter(
    prefix="/materiaux",
    tags=["Matériaux"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=MateriauRead, status_code=status.HTTP_201_CREATED)
async def create_materiau(materiau: MateriauCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau matériau.
    """
    return creer_materiau(db, materiau)

# ========== TOUS ==========
@router.get("/", response_model=List[MateriauRead])
async def read_all_materiaux(db: Session = Depends(get_db)):
    """
    Récupère tous les matériaux.
    """
    return get_tous_materiaux(db)

# ========== PAR ID ==========
@router.get("/{materiau_id}", response_model=MateriauRead)
async def read_materiau(materiau_id: int, db: Session = Depends(get_db)):
    """
    Récupère un matériau par son ID.
    """
    materiau = get_materiau_par_id(db, materiau_id)
    if not materiau:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Matériau avec l'ID {materiau_id} non trouvé."
        )
    return materiau

# ========== MISE À JOUR ==========
@router.put("/{materiau_id}", response_model=MateriauRead)
async def update_materiau_details(materiau_id: int, materiau: MateriauUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un matériau existant.
    """
    updated_materiau = update_materiau(db, materiau_id, materiau)
    if not updated_materiau:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Matériau avec l'ID {materiau_id} non trouvé."
        )
    return updated_materiau

# ========== SUPPRESSION ==========
@router.delete("/{materiau_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_materiau(materiau_id: int, db: Session = Depends(get_db)):
    """
    Supprime un matériau par son ID.
    """
    materiau = get_materiau_par_id(db, materiau_id)
    if not materiau:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Matériau avec l'ID {materiau_id} non trouvé."
        )
    supprimer_materiau(db, materiau_id)