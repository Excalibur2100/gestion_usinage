from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables import Materiau
from db.schemas.schemas import MateriauCreate

def creer_materiau(db: Session, materiau_data: MateriauCreate) -> Materiau:
    materiau = Materiau(**materiau_data.dict())
    db.add(materiau)
    db.commit()
    db.refresh(materiau)
    return materiau

def get_tous_materiaux(db: Session) -> List[Materiau]:
    return db.query(Materiau).all()

def get_materiau_par_id(db: Session, materiau_id: int) -> Optional[Materiau]:
    return db.query(Materiau).filter(Materiau.id == materiau_id).first()

def update_materiau(db: Session, materiau_id: int, materiau_data: MateriauCreate) -> Optional[Materiau]:
    materiau = db.query(Materiau).filter(Materiau.id == materiau_id).first()
    if materiau:
        for key, value in materiau_data.dict().items():
            setattr(materiau, key, value)
        db.commit()
        db.refresh(materiau)
    return materiau

def supprimer_materiau(db: Session, materiau_id: int) -> None:
    materiau = db.query(Materiau).filter(Materiau.id == materiau_id).first()
    if materiau:
        db.delete(materiau)
        db.commit()
