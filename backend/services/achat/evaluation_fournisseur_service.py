from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
import csv
import io

from backend.db.models.tables.achat.evaluation_fournisseur import EvaluationFournisseur, StatutEvaluation, TypeEvaluation
from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    EvaluationFournisseurUpdate,
    EvaluationFournisseurSearch
)

# -------- CRÉATION --------

def creer_evaluation(db: Session, data: EvaluationFournisseurCreate) -> EvaluationFournisseur:
    if not (0 <= data.note_globale <= 100):
        raise HTTPException(status_code=400, detail="La note globale doit être comprise entre 0 et 100.")

    evaluation = EvaluationFournisseur(**data.model_dump())
    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)
    return evaluation

# -------- LECTURE --------

def get_evaluation(db: Session, evaluation_id: int) -> EvaluationFournisseur:
    evaluation = db.query(EvaluationFournisseur).filter_by(id=evaluation_id).first()
    if not evaluation:
        raise HTTPException(status_code=404, detail="Évaluation fournisseur introuvable")
    return evaluation

def list_evaluations(db: Session, skip: int = 0, limit: int = 50) -> List[EvaluationFournisseur]:
    return db.query(EvaluationFournisseur).order_by(EvaluationFournisseur.date_evaluation.desc()).offset(skip).limit(limit).all()

# -------- MISE À JOUR --------

def update_evaluation(db: Session, evaluation_id: int, data: EvaluationFournisseurUpdate) -> EvaluationFournisseur:
    evaluation = get_evaluation(db, evaluation_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(evaluation, field, value)
    db.commit()
    db.refresh(evaluation)
    return evaluation

# -------- SUPPRESSION --------

def delete_evaluation(db: Session, evaluation_id: int) -> dict:
    evaluation = get_evaluation(db, evaluation_id)
    db.delete(evaluation)
    db.commit()
    return {"detail": "Évaluation supprimée avec succès."}

# -------- RECHERCHE --------

def search_evaluations(db: Session, filters: EvaluationFournisseurSearch, skip: int = 0, limit: int = 50):
    query = db.query(EvaluationFournisseur)

    if filters.fournisseur_id:
        query = query.filter(EvaluationFournisseur.fournisseur_id == filters.fournisseur_id)
    if filters.statut:
        query = query.filter(EvaluationFournisseur.statut == filters.statut.value)
    if filters.type_evaluation:
        query = query.filter(EvaluationFournisseur.type_evaluation == filters.type_evaluation.value)
    if filters.date_min:
        query = query.filter(EvaluationFournisseur.date_evaluation >= filters.date_min)
    if filters.date_max:
        query = query.filter(EvaluationFournisseur.date_evaluation <= filters.date_max)
    if filters.is_archived is not None:
        query = query.filter(EvaluationFournisseur.is_archived == filters.is_archived)

    total = query.count()
    results = query.order_by(EvaluationFournisseur.date_evaluation.desc()).offset(skip).limit(limit).all()
    return {"total": total, "results": results}

# -------- EXPORT --------

def export_evaluations_csv(db: Session) -> io.StringIO:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "ID", "Fournisseur", "Note Globale", "Statut", "Type", "Date", "Commentaire"
    ])
    for e in db.query(EvaluationFournisseur).all():
        writer.writerow([
            e.id,
            e.fournisseur_id,
            e.note_globale,
            e.statut.value,
            e.type_evaluation.value,
            e.date_evaluation.strftime("%Y-%m-%d") if getattr(e, "date_evaluation", None) else "",
            e.commentaire or ""
        ])
    buffer.seek(0)
    return buffer

# -------- BULK --------

def bulk_create_evaluations(db: Session, data: List[EvaluationFournisseurCreate]) -> List[EvaluationFournisseur]:
    objets = [EvaluationFournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(objets)
    db.commit()
    return objets

def bulk_delete_evaluations(db: Session, ids: List[int]) -> int:
    evaluations = db.query(EvaluationFournisseur).filter(EvaluationFournisseur.id.in_(ids)).all()
    for e in evaluations:
        db.delete(e)
    db.commit()
    return len(evaluations)