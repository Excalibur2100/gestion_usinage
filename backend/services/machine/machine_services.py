from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.machine import Machine
from db.schemas.machine_schemas import MachineCreate, MachineUpdate

def creer_machine(db: Session, machine_data: MachineCreate) -> Machine:
    """
    Crée une nouvelle machine.
    """
    machine = Machine(**machine_data.dict())
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine

def get_toutes_machines(db: Session) -> List[Machine]:
    """
    Récupère toutes les machines.
    """
    return db.query(Machine).all()

def get_machine_par_id(db: Session, machine_id: int) -> Optional[Machine]:
    """
    Récupère une machine par son ID.
    """
    return db.query(Machine).filter(Machine.id == machine_id).first()

def update_machine(db: Session, machine_id: int, machine_data: MachineUpdate) -> Optional[Machine]:
    """
    Met à jour une machine existante.
    """
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if machine:
        for key, value in machine_data.dict(exclude_unset=True).items():
            setattr(machine, key, value)
        db.commit()
        db.refresh(machine)
    return machine

def supprimer_machine(db: Session, machine_id: int) -> None:
    """
    Supprime une machine par son ID.
    """
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if machine:
        db.delete(machine)
        db.commit()