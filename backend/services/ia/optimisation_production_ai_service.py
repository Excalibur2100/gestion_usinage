from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.optimisation_production_ai import OptimisationProductionAI
from db.schemas.ia.optimisation_production_ai_schemas import *

def create_optimisation(db: Session, data: OptimisationAICreate) -> OptimisationProductionAI:
    obj = OptimisationProductionAI(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_optimisation(db: Session, id_: int) -> Optional[OptimisationProductionAI]:
    return db.query(OptimisationProductionAI).filter(OptimisationProductionAI.id == id_).first()

def get_all_optimisations(db: Session) -> List[OptimisationProductionAI]:
    return db.query(OptimisationProductionAI).all()

def update_optimisation(db: Session, id_: int, data: OptimisationAIUpdate) -> Optional[OptimisationProductionAI]:
    obj = get_optimisation(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_optimisation(db: Session, id_: int) -> bool:
    obj = get_optimisation(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_optimisations(db: Session, search_data: OptimisationAISearch) -> List[OptimisationProductionAI]:
    query = db.query(OptimisationProductionAI)
    if search_data.utilisateur_id:
        query = query.filter(OptimisationProductionAI.utilisateur_id == search_data.utilisateur_id)
    if search_data.machine_id:
        query = query.filter(OptimisationProductionAI.machine_id == search_data.machine_id)
    if search_data.piece_id:
        query = query.filter(OptimisationProductionAI.piece_id == search_data.piece_id)
    if search_data.nom:
        query = query.filter(OptimisationProductionAI.nom.ilike(f"%{search_data.nom}%"))
    return query.all()