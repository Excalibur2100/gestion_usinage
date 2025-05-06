from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.outils import Outil
from db.schemas.outils_schemas import OutilCreate, OutilUpdate

def creer_outil(db: Session, outil_data: OutilCreate) -> Outil:
    """
    Crée un nouvel outil.
    """
    outil = Outil(**outil_data.dict())
    db.add(outil)
    db.commit()
    db.refresh(outil)
    return outil

def get_tous_outils(db: Session) -> List[Outil]:
    """
    Récupère tous les outils.
    """
    return db.query(Outil).all()

def get_outil_par_id(db: Session, outil_id: int) -> Optional[Outil]:
    """
    Récupère un outil par son ID.
    """
    return db.query(Outil).filter(Outil.id == outil_id).first()

def update_outil(db: Session, outil_id: int, outil_data: OutilUpdate) -> Optional[Outil]:
    """
    Met à jour un outil existant.
    """
    outil = db.query(Outil).filter(Outil.id == outil_id).first()
    if outil:
        for key, value in outil_data.dict(exclude_unset=True).items():
            setattr(outil, key, value)
        db.commit()
        db.refresh(outil)
    return outil

def supprimer_outil(db: Session, outil_id: int) -> None:
    """
    Supprime un outil par son ID.
    """
    outil = db.query(Outil).filter(Outil.id == outil_id).first()
    if outil:
        db.delete(outil)
        db.commit()