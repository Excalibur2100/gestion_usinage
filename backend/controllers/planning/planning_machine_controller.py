from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.services.planning.planning_machine_service import verifier_conflits_planning
from backend.db.schemas.planning.planning_machine_schemas import PlanningMachineCreate, PlanningMachineRead
from backend.services.planning.planning_machine_service import (
    creer_planning_machine,
    get_tous_plannings_machine,
    get_planning_machine_par_id,
    update_planning_machine,
    supprimer_planning_machine,
    verifier_conflits_planning,  # Ajout de la vérification des conflits
)

router = APIRouter(prefix="/planning-machine", tags=["Planning Machine"])

@router.post("/", response_model=PlanningMachineRead)
def creer(planning_data: PlanningMachineCreate, db: Session = Depends(get_db)):
    # Vérifier les conflits avant de créer le planning
    conflits = verifier_conflits_planning(db, planning_data)
    if conflits:
        raise HTTPException(status_code=400, detail="Conflit détecté avec un autre planning")
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
    # Vérifier les conflits avant de mettre à jour le planning
    conflits = verifier_conflits_planning(db, planning_data, exclude_id=id)
    if conflits:
        raise HTTPException(status_code=400, detail="Conflit détecté avec un autre planning")
    planning = update_planning_machine(db, id, planning_data)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning Machine non trouvé pour mise à jour")
    return planning

@router.delete("/{id}", status_code=204)
def suppression(id: int, db: Session = Depends(get_db)):
    supprimer_planning_machine(db, id)
    return

@router.get("/verifier-conflits")
async def verifier_conflits(planning: list[dict], db: Session = Depends(get_db)):
    """
    Vérifie les conflits dans un planning.
    """
    conflits = verifier_conflits_planning(db, planning)
    return {"conflits": conflits}