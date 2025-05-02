from sqlalchemy.orm import Session
from db.models.tables import PlanningEmploye
from db.schemas.schemas import PlanningEmployeCreate

def verifier_conflits_planning_employe(db: Session, data: PlanningEmployeCreate, exclude_id: int = None):
    query = db.query(PlanningEmploye).filter(
        PlanningEmploye.employe_id == data.employe_id,
        PlanningEmploye.date_debut < data.date_fin,
        PlanningEmploye.date_fin > data.date_debut
    )
    if exclude_id:
        query = query.filter(PlanningEmploye.id != exclude_id)
    conflits = query.all()
    return conflits

def creer_planning_employe(db: Session, data: PlanningEmployeCreate):
    planning = PlanningEmploye(**data.dict())
    db.add(planning)
    db.commit()
    db.refresh(planning)
    return planning

def get_tous_plannings_employe(db: Session):
    return db.query(PlanningEmploye).all()

def get_planning_employe_par_id(db: Session, id: int):
    return db.query(PlanningEmploye).filter(PlanningEmploye.id == id).first()

def update_planning_employe(db: Session, id: int, data: PlanningEmployeCreate):
    planning = get_planning_employe_par_id(db, id)
    if not planning:
        return None
    for key, value in data.dict().items():
        setattr(planning, key, value)
    db.commit()
    db.refresh(planning)
    return planning

def supprimer_planning_employe(db: Session, id: int):
    planning = get_planning_employe_par_id(db, id)
    if planning:
        db.delete(planning)
        db.commit()