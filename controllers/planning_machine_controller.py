from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import PlanningMachineCreate, PlanningMachineRead
from services.planning_machine.planning_machine_service import (
    creer_planning_machine,
    get_tous_plannings_machine,
    get_planning_machine_par_id,
    update_planning_machine,
    supprimer_planning_machine,
)

router = APIRouter(prefix="/planning-machine", tags=["Planning Machine"])

@router.post("/", response_model=PlanningMachineRead)
def creer(planning_data: PlanningMachineCreate, db: Session = Depends(get_db)):
    return creer_planning_machine(db, planning_data)

@router.get("/", response_model=list[PlanningMachineRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_plannings_machine(db)

@router.get("/{id}", response_model=PlanningMachineRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    planning = get_planning_machine_par_id(db, id)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning Machine non trouvé")
    return planning

@router.put("/{id}", response_model=PlanningMachineRead)
def mise_a_jour(id: int, planning_data: PlanningMachineCreate, db: Session = Depends(get_db)):
    planning = update_planning_machine(db, id, planning_data)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning Machine non trouvé pour mise à jour")
    return planning

@router.delete("/{id}", status_code=204)
def suppression(id: int, db: Session = Depends(get_db)):
    supprimer_planning_machine(db, id)
    return