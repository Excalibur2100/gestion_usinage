from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.campagne_commerciale import CampagneCommerciale
from db.schemas.commercial.campagne_commerciale_schemas import *

def create_campagne(db: Session, data: CampagneCommercialeCreate) -> CampagneCommerciale:
    obj = CampagneCommerciale(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_campagne(db: Session, campagne_id: int) -> Optional[CampagneCommerciale]:
    return db.query(CampagneCommerciale).filter(CampagneCommerciale.id == campagne_id).first()

def get_all_campagnes(db: Session) -> List[CampagneCommerciale]:
    return db.query(CampagneCommerciale).all()

def update_campagne(db: Session, campagne_id: int, data: CampagneCommercialeUpdate) -> Optional[CampagneCommerciale]:
    obj = get_campagne(db, campagne_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_campagne(db: Session, campagne_id: int) -> bool:
    obj = get_campagne(db, campagne_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_campagnes(db: Session, search_data: CampagneCommercialeSearch) -> List[CampagneCommerciale]:
    query = db.query(CampagneCommerciale)
    if search_data.nom:
        query = query.filter(CampagneCommerciale.nom.ilike(f"%{search_data.nom}%"))
    if search_data.statut:
        query = query.filter(CampagneCommerciale.statut == search_data.statut)
    return query.all()
