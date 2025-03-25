# services/gestion_acces_services.py

from sqlalchemy.orm import Session
from db.models.models import GestionAcces
from db.schemas.schemas import GestionAccesCreate
from typing import List, Optional

# CRÉER un accès
def creer_gestion_acces(db: Session, data: GestionAccesCreate) -> GestionAcces:
    gestion_acces = GestionAcces(**data.dict())
    db.add(gestion_acces)
    db.commit()
    db.refresh(gestion_acces)
    return gestion_acces

# LISTER tous les accès
def get_tous_gestion_acces(db: Session) -> List[GestionAcces]:
    return db.query(GestionAcces).all()

# LIRE un accès par ID
def get_gestion_acces_par_id(db: Session, acces_id: int) -> Optional[GestionAcces]:
    return db.query(GestionAcces).filter(GestionAcces.id == acces_id).first()

# METTRE À JOUR un accès
def update_gestion_acces(db: Session, acces_id: int, data: GestionAccesCreate) -> Optional[GestionAcces]:
    acces = db.query(GestionAcces).filter(GestionAcces.id == acces_id).first()
    if acces:
        for key, value in data.dict().items():
            setattr(acces, key, value)
        db.commit()
        db.refresh(acces)
    return acces

# SUPPRIMER un accès
def supprimer_gestion_acces(db: Session, acces_id: int) -> None:
    acces = db.query(GestionAcces).filter(GestionAcces.id == acces_id).first()
    if acces:
        db.delete(acces)
        db.commit()