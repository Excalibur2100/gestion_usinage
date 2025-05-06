from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.materiau import Materiau
from db.schemas.materiaux_schemas import MateriauCreate, MateriauUpdate

def creer_materiau(db: Session, materiau_data: MateriauCreate) -> Materiau:
    """
    Crée un nouveau matériau.
    """
    materiau = Materiau(**materiau_data.dict())
    db.add(materiau)
    db.commit()
    db.refresh(materiau)
    return materiau

def get_tous_materiaux(db: Session) -> List[Materiau]:
    """
    Récupère tous les matériaux.
    """
    return db.query(Materiau).all()

def get_materiau_par_id(db: Session, materiau_id: int) -> Optional[Materiau]:
    """
    Récupère un matériau par son ID.
    """
    return db.query(Materiau).filter(Materiau.id == materiau_id).first()

def update_materiau(db: Session, materiau_id: int, materiau_data: MateriauUpdate) -> Optional[Materiau]:
    """
    Met à jour un matériau existant.
    """
    materiau = db.query(Materiau).filter(Materiau.id == materiau_id).first()
    if materiau:
        for key, value in materiau_data.dict(exclude_unset=True).items():
            setattr(materiau, key, value)
        db.commit()
        db.refresh(materiau)
    return materiau

def supprimer_materiau(db: Session, materiau_id: int) -> None:
    """
    Supprime un matériau par son ID.
    """
    materiau = db.query(Materiau).filter(Materiau.id == materiau_id).first()
    if materiau:
        db.delete(materiau)
        db.commit()