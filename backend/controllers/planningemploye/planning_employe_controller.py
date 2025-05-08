from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.planning_employé_schemas import PlanningEmployeCreate, PlanningEmployeRead
from services.planning_employe.planning_employe_services import (
    creer_planning_employe,
    get_tous_plannings_employe,
    get_planning_employe_par_id,
    update_planning_employe,
    supprimer_planning_employe,
    verifier_conflits_planning_employe,  # Vérification des conflits
)

router = APIRouter(prefix="/planning-employe", tags=["Planning Employé"])

@router.post("/", response_model=PlanningEmployeRead)
def creer(planning_data: PlanningEmployeCreate, db: Session = Depends(get_db)):
    # Vérifier les conflits avant de créer le planning
    conflits = verifier_conflits_planning_employe(db, planning_data)
    if conflits:
        raise HTTPException(status_code=400, detail="Conflit détecté avec un autre planning")
    return creer_planning_employe(db, planning_data)

@router.get("/", response_model=list[PlanningEmployeRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_plannings_employe(db)

@router.get("/{id}", response_model=PlanningEmployeRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    planning = get_planning_employe_par_id(db, id)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning Employé non trouvé")
    return planning

@router.put("/{id}", response_model=PlanningEmployeRead)
def mise_a_jour(id: int, planning_data: PlanningEmployeCreate, db: Session = Depends(get_db)):
    # Vérifier les conflits avant de mettre à jour le planning
    conflits = verifier_conflits_planning_employe(db, planning_data, exclude_id=id)
    if conflits:
        raise HTTPException(status_code=400, detail="Conflit détecté avec un autre planning")
    planning = update_planning_employe(db, id, planning_data)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning Employé non trouvé pour mise à jour")
    return planning

@router.delete("/{id}", status_code=204)
def suppression(id: int, db: Session = Depends(get_db)):
    supprimer_planning_employe(db, id)
    return