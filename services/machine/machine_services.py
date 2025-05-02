from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables import Machine
from db.schemas.schemas import MachineCreate

def creer_machine(db: Session, machine_data: MachineCreate) -> Machine:
    machine = Machine(**machine_data.dict())
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine

def get_toutes_machines(db: Session) -> List[Machine]:
    return db.query(Machine).all()

def get_machine_par_id(db: Session, machine_id: int) -> Optional[Machine]:
    return db.query(Machine).filter(Machine.id == machine_id).first()

def update_machine(db: Session, machine_id: int, machine_data: MachineCreate) -> Optional[Machine]:
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if machine:
        for key, value in machine_data.dict().items():
            setattr(machine, key, value)
        db.commit()
        db.refresh(machine)
    return machine

def supprimer_machine(db: Session, machine_id: int) -> None:
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if machine:
        db.delete(machine)
        db.commit()
