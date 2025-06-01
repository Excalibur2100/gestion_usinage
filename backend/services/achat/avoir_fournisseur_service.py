from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List, Dict
import csv
import io

from backend.db.models.tables.achat.avoir_fournisseur import AvoirFournisseur, StatutAvoir
from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    AvoirFournisseurUpdate,
    AvoirFournisseurSearch
)


# -------- CRUD --------

def creer_avoir(db: Session, data: AvoirFournisseurCreate) -> AvoirFournisseur:
    """Créer un nouvel avoir fournisseur."""
    avoir = AvoirFournisseur(**data.model_dump())
    db.add(avoir)
    db.commit()
    db.refresh(avoir)
    return avoir


def get_avoir(db: Session, avoir_id: int) -> AvoirFournisseur:
    """Récupérer un avoir fournisseur par son ID."""
    avoir = db.query(AvoirFournisseur).filter(AvoirFournisseur.id == avoir_id).first()
    if not avoir:
        raise HTTPException(status_code=404, detail="Avoir introuvable")
    return avoir


def list_avoirs(db: Session, skip: int = 0, limit: int = 50) -> List[AvoirFournisseur]:
    """Lister les avoirs fournisseurs avec pagination."""
    return db.query(AvoirFournisseur).offset(skip).limit(limit).all()


def update_avoir(db: Session, avoir_id: int, data: AvoirFournisseurUpdate) -> AvoirFournisseur:
    """Mettre à jour un avoir fournisseur uniquement s’il est en brouillon."""
    avoir = get_avoir(db, avoir_id)
    if str(avoir.statut) != str(StatutAvoir.brouillon):
        raise HTTPException(status_code=400, detail="Seuls les avoirs en brouillon peuvent être modifiés.")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(avoir, field, value)
    db.commit()
    db.refresh(avoir)
    return avoir


def delete_avoir(db: Session, avoir_id: int) -> Dict[str, str]:
    """Supprimer un avoir fournisseur uniquement s’il est en brouillon."""
    avoir = get_avoir(db, avoir_id)
    if str(avoir.statut) != str(StatutAvoir.brouillon):
        raise HTTPException(status_code=400, detail="Seuls les avoirs en brouillon peuvent être supprimés.")
    db.delete(avoir)
    db.commit()
    return {"detail": "Avoir supprimé avec succès."}


# -------- SEARCH --------

from typing import Any

def search_avoirs(db: Session, filters: AvoirFournisseurSearch, skip: int = 0, limit: int = 50) -> Dict[str, Any]:
    """Recherche multi-critères sur les avoirs fournisseurs."""
    query = db.query(AvoirFournisseur)

    if filters.reference:
        query = query.filter(AvoirFournisseur.reference.ilike(f"%{filters.reference}%"))
    if filters.fournisseur_id:
        query = query.filter(AvoirFournisseur.fournisseur_id == filters.fournisseur_id)
    if filters.statut:
        query = query.filter(AvoirFournisseur.statut == filters.statut)
    if filters.type_avoir:
        query = query.filter(AvoirFournisseur.type_avoir == filters.type_avoir)
    if filters.date_min:
        query = query.filter(AvoirFournisseur.date_emission >= filters.date_min)
    if filters.date_max:
        query = query.filter(AvoirFournisseur.date_emission <= filters.date_max)
    if filters.is_archived is not None:
        query = query.filter(AvoirFournisseur.is_archived == filters.is_archived)

    total = query.count()
    results = query.order_by(AvoirFournisseur.date_emission.desc()).offset(skip).limit(limit).all()
    return {"total": total, "results": results}


# -------- EXPORT CSV --------

def export_avoirs_csv(db: Session) -> io.StringIO:
    """Exporter tous les avoirs au format CSV."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "ID", "Référence", "Fournisseur", "Montant TTC", "Statut", "Date émission", "Devise"
    ])
    for a in db.query(AvoirFournisseur).all():
        writer.writerow([
            a.id,
            a.reference,
            a.fournisseur_id,
            a.montant_ttc,
            a.statut.value,
            a.date_emission.strftime("%Y-%m-%d") if getattr(a, "date_emission", None) else "",
            a.devise
        ])
    buffer.seek(0)
    return buffer


# -------- BULK CREATE --------

def bulk_create_avoirs(db: Session, data: List[AvoirFournisseurCreate]) -> List[AvoirFournisseur]:
    """Créer plusieurs avoirs en une seule opération."""
    objets = [AvoirFournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(objets)
    db.commit()
    return objets


# -------- BULK DELETE --------

def bulk_delete_avoirs(db: Session, ids: List[int]) -> int:
    """Supprimer plusieurs avoirs en fonction d’une liste d’IDs."""
    avoirs = db.query(AvoirFournisseur).filter(AvoirFournisseur.id.in_(ids)).all()
    count = 0
    for a in avoirs:
        if str(a.statut) == str(StatutAvoir.brouillon):
            db.delete(a)
            count += 1
    db.commit()
    return count