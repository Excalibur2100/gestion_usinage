from sqlalchemy.orm import Session
from typing import List, Optional
from backend.db.models.table.planning.pointages import Pointage
from backend.db.schemas.planning.pointage_schemas import PointageCreate, PointageUpdate

def creer_pointage(db: Session, pointage_data: PointageCreate) -> Pointage:
    """
    Crée un nouveau pointage.
    """
    pointage = Pointage(**pointage_data.dict())
    db.add(pointage)
    db.commit()
    db.refresh(pointage)
    return pointage

def get_tous_pointages(db: Session) -> List[Pointage]:
    """
    Récupère tous les pointages.
    """
    return db.query(Pointage).all()

def get_pointage_par_id(db: Session, pointage_id: int) -> Optional[Pointage]:
    """
    Récupère un pointage par son ID.
    """
    return db.query(Pointage).filter(Pointage.id == pointage_id).first()

def update_pointage(db: Session, pointage_id: int, pointage_data: PointageUpdate) -> Optional[Pointage]:
    """
    Met à jour un pointage existant.
    """
    pointage = get_pointage_par_id(db, pointage_id)
    if pointage:
        for key, value in pointage_data.dict(exclude_unset=True).items():
            setattr(pointage, key, value)
        db.commit()
        db.refresh(pointage)
    return pointage

def supprimer_pointage(db: Session, pointage_id: int) -> None:
    """
    Supprime un pointage par son ID.
    """
    pointage = get_pointage_par_id(db, pointage_id)
    if pointage:
        db.delete(pointage)
        db.commit()