from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.type_fournisseur import TypeFournisseur
from db.schemas.achat.type_fournisseur_schemas import *

def create_type(db: Session, data: TypeFournisseurCreate) -> TypeFournisseur:
    obj = TypeFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_type(db: Session, type_id: int) -> Optional[TypeFournisseur]:
    return db.query(TypeFournisseur).filter(TypeFournisseur.id == type_id).first()

def get_all_types(db: Session) -> List[TypeFournisseur]:
    return db.query(TypeFournisseur).all()

def update_type(db: Session, type_id: int, data: TypeFournisseurUpdate) -> Optional[TypeFournisseur]:
    obj = get_type(db, type_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_type(db: Session, type_id: int) -> bool:
    obj = get_type(db, type_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_types(db: Session, search_data: TypeFournisseurSearch) -> List[TypeFournisseur]:
    query = db.query(TypeFournisseur)
    if search_data.nom:
        query = query.filter(TypeFournisseur.nom.ilike(f"%{search_data.nom}%"))
    return query.all()
