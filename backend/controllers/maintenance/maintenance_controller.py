from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.maintenance_schemas import MaintenanceCreate, MaintenanceRead, MaintenanceUpdate
from backend.db.models.database import get_db
from backend.services.maintenance.maintenance_services import (
    creer_maintenance,
    get_toutes_maintenances,
    get_maintenance_par_id,
    update_maintenance,
    supprimer_maintenance,
)

router = APIRouter(
    prefix="/maintenances",
    tags=["Maintenances"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=MaintenanceRead, status_code=status.HTTP_201_CREATED)
async def create_maintenance(maintenance: MaintenanceCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle maintenance.
    """
    return creer_maintenance(db, maintenance)

# ========== TOUS ==========
@router.get("/", response_model=List[MaintenanceRead])
async def read_all_maintenances(db: Session = Depends(get_db)):
    """
    Récupère toutes les maintenances.
    """
    return get_toutes_maintenances(db)

# ========== PAR ID ==========
@router.get("/{maintenance_id}", response_model=MaintenanceRead)
async def read_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    """
    Récupère une maintenance par son ID.
    """
    maintenance = get_maintenance_par_id(db, maintenance_id)
    if not maintenance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Maintenance avec l'ID {maintenance_id} non trouvée."
        )
    return maintenance

# ========== MISE À JOUR ==========
@router.put("/{maintenance_id}", response_model=MaintenanceRead)
async def update_maintenance_details(maintenance_id: int, maintenance: MaintenanceUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une maintenance existante.
    """
    updated_maintenance = update_maintenance(db, maintenance_id, maintenance)
    if not updated_maintenance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Maintenance avec l'ID {maintenance_id} non trouvée."
        )
    return updated_maintenance

# ========== SUPPRESSION ==========
@router.delete("/{maintenance_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    """
    Supprime une maintenance par son ID.
    """
    maintenance = get_maintenance_par_id(db, maintenance_id)
    if not maintenance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Maintenance avec l'ID {maintenance_id} non trouvée."
        )
    supprimer_maintenance(db, maintenance_id)