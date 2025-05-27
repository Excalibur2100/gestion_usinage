from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.entreprise.site import Site
from db.schemas.entreprise.site_schemas import *

def create_site(db: Session, data: SiteCreate) -> Site:
    obj = Site(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_site(db: Session, id_: int) -> Optional[Site]:
    return db.query(Site).filter(Site.id == id_).first()

def get_all_sites(db: Session) -> List[Site]:
    return db.query(Site).all()

def update_site(db: Session, id_: int, data: SiteUpdate) -> Optional[Site]:
    obj = get_site(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_site(db: Session, id_: int) -> bool:
    obj = get_site(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_sites(db: Session, search_data: SiteSearch) -> List[Site]:
    query = db.query(Site)
    if search_data.entreprise_id:
        query = query.filter(Site.entreprise_id == search_data.entreprise_id)
    if search_data.nom:
        query = query.filter(Site.nom.ilike(f"%{search_data.nom}%"))
    return query.all()