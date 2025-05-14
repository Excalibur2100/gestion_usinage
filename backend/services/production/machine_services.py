from sqlalchemy.orm import Session
from db.models.tables.machine import Machine
from backend.db.schemas.production.machine_schemas import MachineCreate, MachineUpdate

def create_machine(db: Session, data: MachineCreate) -> Machine:
    machine = Machine(**data.model_dump())
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine

def get_all_machines(db: Session, skip: int = 0, limit: int = 100) -> list[Machine]:
    return db.query(Machine).offset(skip).limit(limit).all()

def get_machine_by_id(db: Session, machine_id: int) -> Machine | None:
    return db.query(Machine).filter(Machine.id == machine_id).first()

def update_machine(db: Session, machine_id: int, data: MachineUpdate) -> Machine | None:
    machine = get_machine_by_id(db, machine_id)
    if machine:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(machine, key, value)
        db.commit()
        db.refresh(machine)
    return machine

def delete_machine(db: Session, machine_id: int) -> bool:
    machine = get_machine_by_id(db, machine_id)
    if machine:
        db.delete(machine)
        db.commit()
        return True
    return False
