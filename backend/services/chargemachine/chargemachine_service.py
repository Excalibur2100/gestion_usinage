from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.charges_machine import ChargeMachine
from db.schemas.schemas import ChargeMachineCreate, ChargeMachineRead


def creer_charge_machine(db: Session, charge_data: ChargeMachineCreate) -> ChargeMachine:
    """
    Crée une nouvelle charge machine.
    """
    charge = ChargeMachine(**charge_data.dict())
    db.add(charge)
    db.commit()
    db.refresh(charge)
    return charge


def get_charges_machine(db: Session) -> List[ChargeMachine]:
    """
    Récupère toutes les charges machines.
    """
    return db.query(ChargeMachine).all()


def get_charge_machine_par_id(db: Session, charge_id: int) -> Optional[ChargeMachine]:
    """
    Récupère une charge machine par son ID.
    """
    return db.query(ChargeMachine).filter(ChargeMachine.id == charge_id).first()


def update_charge_machine(
    db: Session, charge_id: int, charge_data: ChargeMachineCreate
) -> Optional[ChargeMachine]:
    """
    Met à jour une charge machine par son ID.
    """
    charge = get_charge_machine_par_id(db, charge_id)
    if charge:
        for key, value in charge_data.dict(exclude_unset=True).items():
            setattr(charge, key, value)
        db.commit()
        db.refresh(charge)
    return charge


def supprimer_charge_machine(db: Session, charge_id: int) -> None:
    """
    Supprime une charge machine par son ID.
    """
    charge = get_charge_machine_par_id(db, charge_id)
    if charge:
        db.delete(charge)
        db.commit()