from typing import List, Optional
from sqlalchemy.orm import Session
from backend.db.models.tables.achat.suivis_reglement_fournisseur import SuiviReglementFournisseur
from db.schemas.achat.suivi_reglement_fournisseur_schemas import *

def create_reglement(db: Session, data: SuiviReglementFournisseurCreate) -> SuiviReglementFournisseur:
    obj = SuiviReglementFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_reglement(db: Session, reglement_id: int) -> Optional[SuiviReglementFournisseur]:
    return db.query(SuiviReglementFournisseur).filter(SuiviReglementFournisseur.id == reglement_id).first()

def get_all_reglements(db: Session) -> List[SuiviReglementFournisseur]:
    return db.query(SuiviReglementFournisseur).all()

def update_reglement(db: Session, reglement_id: int, data: SuiviReglementFournisseurUpdate) -> Optional[SuiviReglementFournisseur]:
    obj = get_reglement(db, reglement_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_reglement(db: Session, reglement_id: int) -> bool:
    obj = get_reglement(db, reglement_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_reglements(db: Session, search_data: SuiviReglementFournisseurSearch) -> List[SuiviReglementFournisseur]:
    query = db.query(SuiviReglementFournisseur)
    if search_data.facture_id:
        query = query.filter(SuiviReglementFournisseur.facture_id == search_data.facture_id)
    if search_data.statut:
        query = query.filter(SuiviReglementFournisseur.statut == search_data.statut)
    return query.all()
