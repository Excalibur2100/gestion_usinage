from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables import Outil
from db.schemas.schemas import OutilCreate

def creer_outil(db: Session, outil_data: OutilCreate) -> Outil:
    outil = Outil(**outil_data.dict())
    db.add(outil)
    db.commit()
    db.refresh(outil)
    return outil

def get_tous_outils(db: Session) -> List[Outil]:
    return db.query(Outil).all()

def get_outil_par_id(db: Session, outil_id: int) -> Optional[Outil]:
    return db.query(Outil).filter(Outil.id == outil_id).first()

def update_outil(db: Session, outil_id: int, outil_data: OutilCreate) -> Optional[Outil]:
    outil = db.query(Outil).filter(Outil.id == outil_id).first()
    if outil:
        for key, value in outil_data.dict().items():
            setattr(outil, key, value)
        db.commit()
        db.refresh(outil)
    return outil

def supprimer_outil(db: Session, outil_id: int) -> None:
    outil = db.query(Outil).filter(Outil.id == outil_id).first()
    if outil:
        db.delete(outil)
        db.commit()
