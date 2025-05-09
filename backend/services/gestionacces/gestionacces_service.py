from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.gestion_acces import GestionAcces
from backend.db.schemas.gestion_acces_schemas.gestion_acces_schemas import GestionAccesCreate, GestionAccesUpdate

def creer_gestion_acces(db: Session, data: GestionAccesCreate) -> GestionAcces:
    """
    Crée une nouvelle gestion d'accès.
    """
    gestion_acces = GestionAcces(**data.dict())
    db.add(gestion_acces)
    db.commit()
    db.refresh(gestion_acces)
    return gestion_acces

def get_gestion_acces(db: Session, id: int) -> Optional[GestionAcces]:
    """
    Récupère une gestion d'accès par son ID.
    """
    return db.query(GestionAcces).filter(GestionAcces.id == id).first()

def get_toutes_gestions_acces(db: Session) -> List[GestionAcces]:
    """
    Récupère toutes les gestions d'accès.
    """
    return db.query(GestionAcces).all()

def mettre_a_jour_gestion_acces(db: Session, id: int, data: GestionAccesUpdate) -> Optional[GestionAcces]:
    """
    Met à jour une gestion d'accès existante.
    """
    gestion_acces = get_gestion_acces(db, id)
    if gestion_acces:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(gestion_acces, key, value)
        db.commit()
        db.refresh(gestion_acces)
    return gestion_acces

def supprimer_gestion_acces(db: Session, id: int) -> None:
    """
    Supprime une gestion d'accès par son ID.
    """
    gestion_acces = get_gestion_acces(db, id)
    if gestion_acces:
        db.delete(gestion_acces)
        db.commit()