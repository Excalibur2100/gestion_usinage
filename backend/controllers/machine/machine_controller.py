from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.machine_schemas import MachineCreate, MachineRead, MachineUpdate
from backend.db.models.database import get_db
from backend.services.machine.machine_services import (
    creer_machine,
    get_toutes_machines,
    get_machine_par_id,
    update_machine,
    supprimer_machine,
)

router = APIRouter(
    prefix="/machines",
    tags=["Machines"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=MachineRead, status_code=status.HTTP_201_CREATED)
async def create_machine(machine: MachineCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle machine.
    """
    return creer_machine(db, machine)

# ========== TOUS ==========
@router.get("/", response_model=List[MachineRead])
async def read_all_machines(db: Session = Depends(get_db)):
    """
    Récupère toutes les machines.
    """
    return get_toutes_machines(db)

# ========== PAR ID ==========
@router.get("/{machine_id}", response_model=MachineRead)
async def read_machine(machine_id: int, db: Session = Depends(get_db)):
    """
    Récupère une machine par son ID.
    """
    machine = get_machine_par_id(db, machine_id)
    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Machine avec l'ID {machine_id} non trouvée."
        )
    return machine

# ========== MISE À JOUR ==========
@router.put("/{machine_id}", response_model=MachineRead)
async def update_machine_details(machine_id: int, machine: MachineUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une machine existante.
    """
    updated_machine = update_machine(db, machine_id, machine)
    if not updated_machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Machine avec l'ID {machine_id} non trouvée."
        )
    return updated_machine

# ========== SUPPRESSION ==========
@router.delete("/{machine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_machine(machine_id: int, db: Session = Depends(get_db)):
    """
    Supprime une machine par son ID.
    """
    machine = get_machine_par_id(db, machine_id)
    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Machine avec l'ID {machine_id} non trouvée."
        )
    supprimer_machine(db, machine_id)