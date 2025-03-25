from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.models import PlanningEmploye
from db.schemas.schemas import PlanningEmployeCreate

# ========== CRÉATION ==========
def creer_planning_employe(db: Session, planning_data: PlanningEmployeCreate) -> PlanningEmploye:
    planning = PlanningEmploye(**planning_data.model_dump())
    db.add(planning)
    db.commit()
    db.refresh(planning)
    return planning

# ========== TOUS ==========
def get_tous_plannings_employe(db: Session) -> List[PlanningEmploye]:
    return db.query(PlanningEmploye).all()

# ========== PAR ID ==========
def get_planning_employe_par_id(db: Session, planning_id: int) -> Optional[PlanningEmploye]:
    return db.query(PlanningEmploye).filter(PlanningEmploye.id == planning_id).first()

# ========== MISE À JOUR ==========
def update_planning_employe(db: Session, planning_id: int, planning_data: PlanningEmployeCreate) -> Optional[PlanningEmploye]:
    planning = get_planning_employe_par_id(db, planning_id)
    if planning:
        for key, value in planning_data.model_dump().items():
            setattr(planning, key, value)
        db.commit()
        db.refresh(planning)
    return planning

# ========== SUPPRESSION ==========
def supprimer_planning_employe(db: Session, planning_id: int) -> None:
    planning = get_planning_employe_par_id(db, planning_id)
    if planning:
        db.delete(planning)
        db.commit()