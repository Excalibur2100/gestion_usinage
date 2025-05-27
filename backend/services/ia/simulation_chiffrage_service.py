from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.simulation_chiffrage import SimulationChiffrage
from db.schemas.ia.simulation_chiffrage_schemas import *

def create_simulation(db: Session, data: SimulationChiffrageCreate) -> SimulationChiffrage:
    obj = SimulationChiffrage(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_simulation(db: Session, id_: int) -> Optional[SimulationChiffrage]:
    return db.query(SimulationChiffrage).filter(SimulationChiffrage.id == id_).first()

def get_all_simulations(db: Session) -> List[SimulationChiffrage]:
    return db.query(SimulationChiffrage).all()

def update_simulation(db: Session, id_: int, data: SimulationChiffrageUpdate) -> Optional[SimulationChiffrage]:
    obj = get_simulation(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_simulation(db: Session, id_: int) -> bool:
    obj = get_simulation(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_simulations(db: Session, search_data: SimulationChiffrageSearch) -> List[SimulationChiffrage]:
    query = db.query(SimulationChiffrage)
    if search_data.piece_id:
        query = query.filter(SimulationChiffrage.piece_id == search_data.piece_id)
    if search_data.utilisateur_id:
        query = query.filter(SimulationChiffrage.utilisateur_id == search_data.utilisateur_id)
    if search_data.scenario:
        query = query.filter(SimulationChiffrage.scenario.ilike(f"%{search_data.scenario}%"))
    return query.all()