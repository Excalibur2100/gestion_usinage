from sqlalchemy.orm import Session
from db.models.tables import Pointage
from db.schemas.schemas import PointageCreate
from typing import List, Optional

# ========== CRÉER ==========
def creer_pointage(db: Session, pointage_data: PointageCreate) -> Pointage:
    pointage = Pointage(**pointage_data.dict())
    db.add(pointage)
    db.commit()
    db.refresh(pointage)
    return pointage

# ========== TOUS ==========
def get_tous_pointages(db: Session) -> List[Pointage]:
    return db.query(Pointage).all()

# ========== PAR ID ==========
def get_pointage_par_id(db: Session, pointage_id: int) -> Optional[Pointage]:
    return db.query(Pointage).filter(Pointage.id == pointage_id).first()

# ========== MISE À JOUR ==========
def update_pointage(db: Session, pointage_id: int, pointage_data: PointageCreate) -> Optional[Pointage]:
    pointage = get_pointage_par_id(db, pointage_id)
    if pointage:
        for key, value in pointage_data.dict().items():
            setattr(pointage, key, value)
        db.commit()
        db.refresh(pointage)
    return pointage

# ========== SUPPRESSION ==========
def supprimer_pointage(db: Session, pointage_id: int) -> None:
    pointage = get_pointage_par_id(db, pointage_id)
    if pointage:
        db.delete(pointage)
        db.commit()