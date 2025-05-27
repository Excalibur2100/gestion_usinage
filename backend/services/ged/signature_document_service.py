from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.signature_document import SignatureDocument
from db.schemas.ged.signature_document_schemas import *

def create_signature(db: Session, data: SignatureDocumentCreate) -> SignatureDocument:
    obj = SignatureDocument(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_signature(db: Session, id_: int) -> Optional[SignatureDocument]:
    return db.query(SignatureDocument).filter(SignatureDocument.id == id_).first()

def get_all_signatures(db: Session) -> List[SignatureDocument]:
    return db.query(SignatureDocument).all()

def update_signature(db: Session, id_: int, data: SignatureDocumentUpdate) -> Optional[SignatureDocument]:
    obj = get_signature(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_signature(db: Session, id_: int) -> bool:
    obj = get_signature(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_signatures(db: Session, search_data: SignatureDocumentSearch) -> List[SignatureDocument]:
    query = db.query(SignatureDocument)
    if search_data.document_id:
        query = query.filter(SignatureDocument.document_id == search_data.document_id)
    if search_data.utilisateur_id:
        query = query.filter(SignatureDocument.utilisateur_id == search_data.utilisateur_id)
    if search_data.statut:
        query = query.filter(SignatureDocument.statut == search_data.statut)
    return query.all()