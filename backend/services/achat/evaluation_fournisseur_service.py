from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.evaluation_fournisseur import EvaluationFournisseur
from db.schemas.achat.evaluation_fournisseur_schemas import *

def create_evaluation(db: Session, data: EvaluationFournisseurCreate) -> EvaluationFournisseur:
    obj = EvaluationFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_evaluation(db: Session, evaluation_id: int) -> Optional[EvaluationFournisseur]:
    return db.query(EvaluationFournisseur).filter(EvaluationFournisseur.id == evaluation_id).first()

def get_all_evaluations(db: Session) -> List[EvaluationFournisseur]:
    return db.query(EvaluationFournisseur).all()

def update_evaluation(db: Session, evaluation_id: int, data: EvaluationFournisseurUpdate) -> Optional[EvaluationFournisseur]:
    obj = get_evaluation(db, evaluation_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_evaluation(db: Session, evaluation_id: int) -> bool:
    obj = get_evaluation(db, evaluation_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_evaluations(db: Session, search_data: EvaluationFournisseurSearch) -> List[EvaluationFournisseur]:
    query = db.query(EvaluationFournisseur)
    if search_data.fournisseur_id:
        query = query.filter(EvaluationFournisseur.fournisseur_id == search_data.fournisseur_id)
    if search_data.utilisateur_id:
        query = query.filter(EvaluationFournisseur.utilisateur_id == search_data.utilisateur_id)
    return query.all()
