from sqlalchemy.orm import Session
from db.models.tables import Devis
from backend.db.schemas.devis_schemas.devis_schemas import DevisCreate
from typing import List, Optional
from backend.db.schemas.devis_schemas.devis_schemas import DevisCreate, DevisUpdate



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



# ========== MISE À JOUR ==========
def update_devis(db: Session, devis_id: int, devis_data: DevisUpdate) -> Optional[Devis]:
    """
    Met à jour un devis existant.
    """
    devis = db.query(Devis).filter(Devis.id == devis_id).first()
    if devis:
        for key, value in devis_data.dict(exclude_unset=True).items():
            setattr(devis, key, value)
        db.commit()
        db.refresh(devis)
    return devis
