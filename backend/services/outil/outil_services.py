from sqlalchemy.orm import Session
from db.models.tables.outils import Outil
from db.schemas.outils_schemas.outils_schemas import OutilCreate, OutilUpdate

def create_outil(db: Session, data: OutilCreate) -> Outil:
    outil = Outil(**data.model_dump())
    db.add(outil)
    db.commit()
    db.refresh(outil)
    return outil

def get_all_outils(db: Session, skip: int = 0, limit: int = 100) -> list[Outil]:
    return db.query(Outil).offset(skip).limit(limit).all()

def get_outil_by_id(db: Session, outil_id: int) -> Outil | None:
    return db.query(Outil).filter(Outil.id == outil_id).first()

def update_outil(db: Session, outil_id: int, data: OutilUpdate) -> Outil | None:
    outil = get_outil_by_id(db, outil_id)
    if outil:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(outil, key, value)
        db.commit()
        db.refresh(outil)
    return outil

def delete_outil(db: Session, outil_id: int) -> bool:
    outil = get_outil_by_id(db, outil_id)
    if outil:
        db.delete(outil)
        db.commit()
        return True
    return False
