from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
import csv
import io

from backend.db.models.tables.achat.factures_fournisseur import (
    FactureFournisseur,
    StatutFactureFournisseur
)
from backend.db.schemas.achat.facture_fournisseur_schemas import (
    FactureFournisseurCreate,
    FactureFournisseurUpdate,
    FactureFournisseurSearch
)


# -------- CRUD --------

def creer_facture(db: Session, data: FactureFournisseurCreate) -> FactureFournisseur:
    facture = FactureFournisseur(**data.model_dump())
    db.add(facture)
    db.commit()
    db.refresh(facture)
    return facture


def get_facture(db: Session, facture_id: int) -> FactureFournisseur:
    facture = db.query(FactureFournisseur).filter_by(id=facture_id).first()
    if not facture:
        raise HTTPException(status_code=404, detail="Facture introuvable")
    return facture


def list_factures(db: Session, skip: int = 0, limit: int = 50) -> List[FactureFournisseur]:
    return db.query(FactureFournisseur).order_by(FactureFournisseur.date_emission.desc()).offset(skip).limit(limit).all()


def update_facture(db: Session, facture_id: int, data: FactureFournisseurUpdate) -> FactureFournisseur:
    facture = get_facture(db, facture_id)
    if str(facture.statut) != str(StatutFactureFournisseur.brouillon):
        raise HTTPException(status_code=400, detail="Seules les factures en brouillon peuvent être modifiées.")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(facture, field, value)
    db.commit()
    db.refresh(facture)
    return facture


def delete_facture(db: Session, facture_id: int) -> dict:
    facture = get_facture(db, facture_id)
    if str(facture.statut) != str(StatutFactureFournisseur.brouillon):
        raise HTTPException(status_code=400, detail="Seules les factures en brouillon peuvent être supprimées.")
    db.delete(facture)
    db.commit()
    return {"detail": "Facture supprimée avec succès."}


# -------- SEARCH --------

def search_factures(db: Session, filters: FactureFournisseurSearch, skip: int = 0, limit: int = 50):
    query = db.query(FactureFournisseur)

    if filters.numero_facture:
        query = query.filter(FactureFournisseur.numero_facture.ilike(f"%{filters.numero_facture}%"))
    if filters.fournisseur_id:
        query = query.filter(FactureFournisseur.fournisseur_id == filters.fournisseur_id)
    if filters.statut:
        query = query.filter(FactureFournisseur.statut == filters.statut)
    if filters.date_min:
        query = query.filter(FactureFournisseur.date_emission >= filters.date_min)
    if filters.date_max:
        query = query.filter(FactureFournisseur.date_emission <= filters.date_max)
    if filters.is_archived is not None:
        query = query.filter(FactureFournisseur.is_archived == filters.is_archived)

    total = query.count()
    results = query.order_by(FactureFournisseur.date_emission.desc()).offset(skip).limit(limit).all()
    return {"total": total, "results": results}


# -------- EXPORT --------

def export_factures_csv(db: Session) -> io.StringIO:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["ID", "Numéro", "Fournisseur", "Montant TTC", "Statut", "Date émission", "Devise"])

    for f in db.query(FactureFournisseur).all():
        writer.writerow([
            f.id,
            f.numero_facture,
            f.fournisseur_id,
            f.montant_ttc,
            f.statut.value if f.statut is not None else "",
            f.date_emission.strftime("%Y-%m-%d") if getattr(f, "date_emission", None) else "",
            f.devise or ""
        ])

    buffer.seek(0)
    return buffer


# -------- BULK --------

def bulk_create_factures(db: Session, data: List[FactureFournisseurCreate]) -> List[FactureFournisseur]:
    objets = [FactureFournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(objets)
    db.commit()
    return objets


def bulk_delete_factures(db: Session, ids: List[int]) -> int:
    factures = db.query(FactureFournisseur).filter(FactureFournisseur.id.in_(ids)).all()
    count = 0
    for f in factures:
        if str(f.statut) == str(StatutFactureFournisseur.brouillon):
            db.delete(f)
            count += 1
    db.commit()
    return count