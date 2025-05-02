from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from typing import List, Optional
from db.schemas.charge_machine_schemas import ChargeMachineCreate, ChargeMachineRead
from services.chargemachine.chargemachine_service import (
    creer_charge_machine,
    get_charges_machine,
    get_charge_machine_par_id,
    update_charge_machine,
    supprimer_charge_machine,
)

router = APIRouter(prefix="/charges-machine", tags=["Charges Machine"])


@router.post("/", response_model=ChargeMachineRead)
def creer(charge_data: ChargeMachineCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle charge machine.
    """
    return creer_charge_machine(db, charge_data)


@router.get("/", response_model=List[ChargeMachineRead])
def lire_toutes(db: Session = Depends(get_db)):
    """
    Récupère toutes les charges machines.
    """
    return get_charges_machine(db)


@router.get("/{id}", response_model=ChargeMachineRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    """
    Récupère une charge machine par son ID.
    """
    charge = get_charge_machine_par_id(db, id)
    if not charge:
        raise HTTPException(status_code=404, detail="Charge Machine non trouvée")
    return charge


@router.put("/{id}", response_model=ChargeMachineRead)
def maj(id: int, charge_data: ChargeMachineCreate, db: Session = Depends(get_db)):
    """
    Met à jour une charge machine par son ID.
    """
    charge = update_charge_machine(db, id, charge_data)
    if not charge:
        raise HTTPException(status_code=404, detail="Charge Machine non trouvée pour mise à jour")
    return charge


@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    """
    Supprime une charge machine par son ID.
    """
    supprimer_charge_machine(db, id)
    return