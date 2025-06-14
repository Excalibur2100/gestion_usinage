from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
import csv
import io

from backend.db.models.tables.achat.lignes_commande_fournisseur import LigneCommandeFournisseur, StatutLigneCommande
from backend.db.schemas.achat.ligne_commande_fournisseur_schemas import (
    LigneCommandeFournisseurCreate,
    LigneCommandeFournisseurUpdate,
    LigneCommandeFournisseurSearch
)


# -------- CRUD --------

def creer_ligne_commande(db: Session, data: LigneCommandeFournisseurCreate) -> LigneCommandeFournisseur:
    ligne = LigneCommandeFournisseur(**data.model_dump())
    db.add(ligne)
    db.commit()
    db.refresh(ligne)
    return ligne


def get_ligne_commande(db: Session, ligne_id: int) -> LigneCommandeFournisseur:
    ligne = db.query(LigneCommandeFournisseur).filter_by(id=ligne_id).first()
    if not ligne:
        raise HTTPException(status_code=404, detail="Ligne introuvable")
    return ligne


def list_lignes_commande(db: Session, skip: int = 0, limit: int = 100) -> List[LigneCommandeFournisseur]:
    return db.query(LigneCommandeFournisseur).offset(skip).limit(limit).all()


def update_ligne_commande(db: Session, ligne_id: int, data: LigneCommandeFournisseurUpdate) -> LigneCommandeFournisseur:
    ligne = get_ligne_commande(db, ligne_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(ligne, field, value)
    db.commit()
    db.refresh(ligne)
    return ligne


def delete_ligne_commande(db: Session, ligne_id: int) -> dict:
    ligne = get_ligne_commande(db, ligne_id)
    db.delete(ligne)
    db.commit()
    return {"detail": "Ligne supprimée avec succès."}


# -------- SEARCH --------

def search_lignes_commande(db: Session, filters: LigneCommandeFournisseurSearch, skip: int = 0, limit: int = 100):
    query = db.query(LigneCommandeFournisseur)

    if filters.commande_id is not None:
        query = query.filter(LigneCommandeFournisseur.commande_id == filters.commande_id)
    if filters.article_id is not None:
        query = query.filter(LigneCommandeFournisseur.article_id == filters.article_id)
    if filters.designation:
        query = query.filter(LigneCommandeFournisseur.designation.ilike(f"%{filters.designation}%"))
    if filters.statut:
        query = query.filter(LigneCommandeFournisseur.statut == filters.statut)

    total = query.count()
    results = query.offset(skip).limit(limit).all()

    return {"total": total, "results": results}


# -------- EXPORT --------

def export_lignes_commande_csv(db: Session) -> io.StringIO:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "ID", "Commande", "Article", "Désignation", "Quantité", "PU HT", "Montant TTC", "Statut"
    ])
    for l in db.query(LigneCommandeFournisseur).all():
        writer.writerow([
            l.id,
            l.commande_id,
            l.article_id or "",
            l.designation,
            l.quantite,
            l.prix_unitaire_ht,
            l.montant_ttc,
            l.statut.value
        ])
    buffer.seek(0)
    return buffer


# -------- BULK --------

def bulk_create_lignes_commande(db: Session, data: List[LigneCommandeFournisseurCreate]) -> List[LigneCommandeFournisseur]:
    lignes = [LigneCommandeFournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(lignes)
    db.commit()
    return lignes


def bulk_delete_lignes_commande(db: Session, ids: List[int]) -> int:
    lignes = db.query(LigneCommandeFournisseur).filter(LigneCommandeFournisseur.id.in_(ids)).all()
    for l in lignes:
        db.delete(l)
    db.commit()
    return len(lignes)