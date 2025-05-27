from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.autorisation_document import AutorisationDocument
from db.schemas.ged.autorisation_document_schemas import *

def create_autorisation(db: Session, data: AutorisationDocumentCreate) -> AutorisationDocument:
    obj = AutorisationDocument(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_autorisation(db: Session, id_: int) -> Optional[AutorisationDocument]:
    return db.query(AutorisationDocument).filter(AutorisationDocument.id == id_).first()

def get_all_autorisations(db: Session) -> List[AutorisationDocument]:
    return db.query(AutorisationDocument).all()

def update_autorisation(db: Session, id_: int, data: AutorisationDocumentUpdate) -> Optional[AutorisationDocument]:
    obj = get_autorisation(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_autorisation(db: Session, id_: int) -> bool:
    obj = get_autorisation(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_autorisations(db: Session, search_data: AutorisationDocumentSearch) -> List[AutorisationDocument]:
    query = db.query(AutorisationDocument)
    if search_data.document_id:
        query = query.filter(AutorisationDocument.document_id == search_data.document_id)
    if search_data.utilisateur_id:
        query = query.filter(AutorisationDocument.utilisateur_id == search_data.utilisateur_id)
    return query.all()