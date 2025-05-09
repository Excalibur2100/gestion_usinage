from sqlalchemy.orm import Session
from db.models.tables.formation import Formation
from db.schemas.formation_schemas.formation_schemas import FormationCreate, FormationUpdate

def create_formation(db: Session, data: FormationCreate):
    formation = Formation(**data.model_dump())
    db.add(formation)
    db.commit()
    db.refresh(formation)
    return formation

def get_all_formations(db: Session):
    return db.query(Formation).all()

def get_formation_by_id(db: Session, formation_id: int):
    return db.query(Formation).filter(Formation.id == formation_id).first()

def update_formation(db: Session, formation_id: int, data: FormationUpdate):
    formation = get_formation_by_id(db, formation_id)
    if formation:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(formation, key, value)
        db.commit()
        db.refresh(formation)  
    return formation

def delete_formation(db: Session, formation_id: int):
    formation = get_formation_by_id(db, formation_id)
    if formation:
        db.delete(formation)
        db.commit()
    return formation
