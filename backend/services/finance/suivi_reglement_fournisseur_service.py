from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.suivi_reglement_fournisseur import SuiviReglementFournisseur
from db.schemas.finance.suivi_reglement_fournisseur_schemas import *

def create_suivi(db: Session, data: SuiviReglementFournisseurCreate) -> SuiviReglementFournisseur:
    obj = SuiviReglementFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_suivi(db: Session, id_: int) -> Optional[SuiviReglementFournisseur]:
    return db.query(SuiviReglementFournisseur).filter(SuiviReglementFournisseur.id == id_).first()

def get_all_suivis(db: Session) -> List[SuiviReglementFournisseur]:
    return db.query(SuiviReglementFournisseur).all()

def update_suivi(db: Session, id_: int, data: SuiviReglementFournisseurUpdate) -> Optional[SuiviReglementFournisseur]:
    obj = get_suivi(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_suivi(db: Session, id_: int) -> bool:
    obj = get_suivi(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_suivis(db: Session, search_data: SuiviReglementFournisseurSearch) -> List[SuiviReglementFournisseur]:
    query = db.query(SuiviReglementFournisseur)
    if search_data.facture_fournisseur_id:
        query = query.filter(SuiviReglementFournisseur.facture_fournisseur_id == search_data.facture_fournisseur_id)
    if search_data.entreprise_id:
        query = query.filter(SuiviReglementFournisseur.entreprise_id == search_data.entreprise_id)
    if search_data.statut:
        query = query.filter(SuiviReglementFournisseur.statut == search_data.statut)
    return query.all()