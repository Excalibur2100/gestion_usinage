from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import MachineCreate, MachineRead
from services.machine.machine_services import (
    creer_machine,
    get_toutes_machines,
    get_machine_par_id,
    update_machine,
    supprimer_machine
)

router = APIRouter(prefix="/machines", tags=["Machines"])

@router.post("/", response_model=MachineRead)
def creer(machine_data: MachineCreate, db: Session = Depends(get_db)):
    return creer_machine(db, machine_data)

@router.get("/", response_model=list[MachineRead])
def lire_toutes(db: Session = Depends(get_db)):
    return get_toutes_machines(db)

@router.get("/{id}", response_model=MachineRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    machine = get_machine_par_id(db, id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine non trouvée")
    return machine

@router.put("/{id}", response_model=MachineRead)
def maj_machine(id: int, machine_data: MachineCreate, db: Session = Depends(get_db)):
    machine = update_machine(db, id, machine_data)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine non trouvée pour mise à jour")
    return machine

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_machine(db, id)
