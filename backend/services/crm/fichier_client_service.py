from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.fichier_client import FichierClient
from db.schemas.crm.fichier_client_schemas import *

def create_fichier(db: Session, data: FichierClientCreate) -> FichierClient:
    obj = FichierClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_fichier(db: Session, id_: int) -> Optional[FichierClient]:
    return db.query(FichierClient).filter(FichierClient.id == id_).first()

def get_all_fichiers(db: Session) -> List[FichierClient]:
    return db.query(FichierClient).all()

def update_fichier(db: Session, id_: int, data: FichierClientUpdate) -> Optional[FichierClient]:
    obj = get_fichier(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_fichier(db: Session, id_: int) -> bool:
    obj = get_fichier(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_fichiers(db: Session, search_data: FichierClientSearch) -> List[FichierClient]:
    query = db.query(FichierClient)
    if search_data.client_id:
        query = query.filter(FichierClient.client_id == search_data.client_id)
    if search_data.type_fichier:
        query = query.filter(FichierClient.type_fichier == search_data.type_fichier)
    if search_data.nom_fichier:
        query = query.filter(FichierClient.nom_fichier.ilike(f"%{search_data.nom_fichier}%"))
    return query.all()