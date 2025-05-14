 from sqlalchemy.orm import Session
from typing import List, Optional
from backend.db.models.tables.qualite.gestion_filtrage import GestionFiltrage
from backend.db.schemas.gestion_filtrage_schemas.gestion_filtrage_schemas import GestionFiltrageCreate

def creer_filtrage(db: Session, data: GestionFiltrageCreate) -> GestionFiltrage:
    """
    Crée un nouveau filtrage.
    """
    filtrage = GestionFiltrage(**data.dict())
    db.add(filtrage)
    db.commit()
    db.refresh(filtrage)
    return filtrage

def get_tous_filtrages(db: Session) -> List[GestionFiltrage]:
    """
    Récupère tous les filtrages.
    """
    return db.query(GestionFiltrage).all()

def get_filtrage_par_id(db: Session, id: int) -> Optional[GestionFiltrage]:
    """
    Récupère un filtrage par son ID.
    """
    return db.query(GestionFiltrage).filter(GestionFiltrage.id == id).first()

def supprimer_filtrage(db: Session, id: int) -> None:
    """
    Supprime un filtrage par son ID.
    """
    filtrage = get_filtrage_par_id(db, id)
    if filtrage:
        db.delete(filtrage)
        db.commit()