from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables import GestionFiltrage
from db.schemas.schemas import GestionFiltrageCreate

def creer_filtrage(db: Session, data: GestionFiltrageCreate) -> GestionFiltrage:
    filtrage = GestionFiltrage(**data.model_dump())
    db.add(filtrage)
    db.commit()
    db.refresh(filtrage)
    return filtrage

def get_filtrages(db: Session) -> List[GestionFiltrage]:
    return db.query(GestionFiltrage).all()

def get_filtrage_par_id(db: Session, filtrage_id: int) -> Optional[GestionFiltrage]:
    return db.query(GestionFiltrage).filter(GestionFiltrage.id == filtrage_id).first()

def update_filtrage(db: Session, filtrage_id: int, data: GestionFiltrageCreate) -> Optional[GestionFiltrage]:
    filtrage = get_filtrage_par_id(db, filtrage_id)
    if filtrage:
        for key, value in data.model_dump().items():
            setattr(filtrage, key, value)
        db.commit()
        db.refresh(filtrage)
    return filtrage

def supprimer_filtrage(db: Session, filtrage_id: int) -> None:
    filtrage = get_filtrage_par_id(db, filtrage_id)
    if filtrage:
        db.delete(filtrage)
        db.commit()