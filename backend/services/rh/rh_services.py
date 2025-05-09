from sqlalchemy.orm import Session
from db.models.tables import RH
from backend.db.schemas.rh_schemas.rh_schemas import RHCreate, RHUpdate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_rh(db: Session, rh_data: RHCreate) -> RH:
    rh = RH(**rh_data.dict())
    db.add(rh)
    db.commit()
    db.refresh(rh)
    return rh

# ========== TOUS ==========
def get_tous_rh(db: Session) -> List[RH]:
    return db.query(RH).all()

# ========== PAR ID ==========
def get_rh_par_id(db: Session, rh_id: int) -> Optional[RH]:
    return db.query(RH).filter(RH.id == rh_id).first()

# ========== MISE À JOUR ==========
def update_rh(db: Session, rh_id: int, rh_data: RHUpdate) -> Optional[RH]:
    """
    Met à jour un employé RH existant.
    """
    rh = db.query(RH).filter(RH.id == rh_id).first()
    if rh:
        for key, value in rh_data.dict(exclude_unset=True).items():
            setattr(rh, key, value)
        db.commit()
        db.refresh(rh)
    return rh

# ========== SUPPRESSION ==========
def supprimer_rh(db: Session, rh_id: int) -> None:
    rh = db.query(RH).filter(RH.id == rh_id).first()
    if rh:
        db.delete(rh)
        db.commit()
