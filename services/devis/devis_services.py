from sqlalchemy.orm import Session
from db.models.models import Devis
from db.schemas.schemas import DevisCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_devis(db: Session, devis_data: DevisCreate) -> Devis:
    devis = Devis(**devis_data.dict())
    db.add(devis)
    db.commit()
    db.refresh(devis)
    return devis

# ========== TOUS ==========
def get_tous_devis(db: Session) -> List[Devis]:
    return db.query(Devis).all()

# ========== PAR ID ==========
def get_devis_par_id(db: Session, devis_id: int) -> Optional[Devis]:
    return db.query(Devis).filter(Devis.id == devis_id).first()

# ========== MISE À JOUR ==========
def update_devis(db: Session, devis_id: int, devis_data: DevisCreate) -> Optional[Devis]:
    devis = db.query(Devis).filter(Devis.id == devis_id).first()
    if devis:
        for key, value in devis_data.dict().items():
            setattr(devis, key, value)
        db.commit()
        db.refresh(devis)
    return devis

# ========== SUPPRESSION ==========
def supprimer_devis(db: Session, devis_id: int) -> None:
    devis = db.query(Devis).filter(Devis.id == devis_id).first()
    if devis:
        db.delete(devis)
        db.commit()
