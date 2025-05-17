from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.facture_fournisseur import FactureFournisseur
from db.schemas.achat.facture_fournisseur_schemas import *

def create_facture(db: Session, data: FactureFournisseurCreate) -> FactureFournisseur:
    obj = FactureFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_facture(db: Session, facture_id: int) -> Optional[FactureFournisseur]:
    return db.query(FactureFournisseur).filter(FactureFournisseur.id == facture_id).first()

def get_all_factures(db: Session) -> List[FactureFournisseur]:
    return db.query(FactureFournisseur).all()

def update_facture(db: Session, facture_id: int, data: FactureFournisseurUpdate) -> Optional[FactureFournisseur]:
    obj = get_facture(db, facture_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_facture(db: Session, facture_id: int) -> bool:
    obj = get_facture(db, facture_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_factures(db: Session, search_data: FactureFournisseurSearch) -> List[FactureFournisseur]:
    query = db.query(FactureFournisseur)
    if search_data.numero_facture:
        query = query.filter(FactureFournisseur.numero_facture.ilike(f"%{search_data.numero_facture}%"))
    if search_data.fournisseur_id:
        query = query.filter(FactureFournisseur.fournisseur_id == search_data.fournisseur_id)
    if search_data.statut:
        query = query.filter(FactureFournisseur.statut == search_data.statut)
    return query.all()
