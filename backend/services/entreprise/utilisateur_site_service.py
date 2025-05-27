from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.entreprise.utilisateur_site import UtilisateurSite
from db.schemas.entreprise.utilisateur_site_schemas import *

def create_utilisateur_site(db: Session, data: UtilisateurSiteCreate) -> UtilisateurSite:
    obj = UtilisateurSite(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_utilisateur_site(db: Session, id_: int) -> Optional[UtilisateurSite]:
    return db.query(UtilisateurSite).filter(UtilisateurSite.id == id_).first()

def get_all_utilisateurs_sites(db: Session) -> List[UtilisateurSite]:
    return db.query(UtilisateurSite).all()

def update_utilisateur_site(db: Session, id_: int, data: UtilisateurSiteUpdate) -> Optional[UtilisateurSite]:
    obj = get_utilisateur_site(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_utilisateur_site(db: Session, id_: int) -> bool:
    obj = get_utilisateur_site(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_utilisateurs_sites(db: Session, search_data: UtilisateurSiteSearch) -> List[UtilisateurSite]:
    query = db.query(UtilisateurSite)
    if search_data.utilisateur_id:
        query = query.filter(UtilisateurSite.utilisateur_id == search_data.utilisateur_id)
    if search_data.site_id:
        query = query.filter(UtilisateurSite.site_id == search_data.site_id)
    return query.all()