from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import PlanningEmployeCreate, PlanningEmployeRead
from services.planning_employe.planning_employe_services import (
    creer_planning_employe,
    get_tous_plannings_employe,
    get_planning_employe_par_id,
    update_planning_employe,
    supprimer_planning_employe
)

router = APIRouter(prefix="/planning-employes", tags=["Planning Employés"])

# ========== CRÉATION ==========
@router.post("/", response_model=PlanningEmployeRead)
def creer(planning_data: PlanningEmployeCreate, db: Session = Depends(get_db)):
    return creer_planning_employe(db, planning_data)

# ========== TOUS ==========
@router.get("/", response_model=list[PlanningEmployeRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_plannings_employe(db)

# ========== PAR ID ==========
@router.get("/{id}", response_model=PlanningEmployeRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    planning = get_planning_employe_par_id(db, id)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning non trouvé")
    return planning

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=PlanningEmployeRead)
def maj(id: int, planning_data: PlanningEmployeCreate, db: Session = Depends(get_db)):
    planning = update_planning_employe(db, id, planning_data)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning non trouvé pour mise à jour")
    return planning

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_planning_employe(db, id)
    return