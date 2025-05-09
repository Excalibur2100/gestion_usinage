from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.machine_schemas.machine_schemas import MachineCreate, MachineUpdate, MachineRead
from services.machine.machine_services import (
    create_machine,
    get_all_machines,
    get_machine_by_id,
    update_machine,
    delete_machine
)

router = APIRouter(prefix="/api/machines", tags=["Machines"])

@router.post("/", response_model=MachineRead)
def create(data: MachineCreate, db: Session = Depends(get_db)):
    return create_machine(db, data)

@router.get("/", response_model=list[MachineRead])
def read_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all_machines(db, skip, limit)

@router.get("/{machine_id}", response_model=MachineRead)
def read_one(machine_id: int, db: Session = Depends(get_db)):
    machine = get_machine_by_id(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine non trouvée")
    return machine

@router.put("/{machine_id}", response_model=MachineRead)
def update(machine_id: int, data: MachineUpdate, db: Session = Depends(get_db)):
    machine = update_machine(db, machine_id, data)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine non trouvée")
    return machine

@router.delete("/{machine_id}")
def delete(machine_id: int, db: Session = Depends(get_db)):
    if not delete_machine(db, machine_id):
        raise HTTPException(status_code=404, detail="Machine non trouvée")
    return {"detail": "Machine supprimée"}
