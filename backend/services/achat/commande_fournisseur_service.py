from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
import csv
import io

from backend.db.models.tables.achat.commande_fournisseur import CommandeFournisseur, StatutCommandeFournisseur
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    CommandeFournisseurUpdate,
    CommandeFournisseurSearch
)


# -------- CRUD --------

def creer_commande(db: Session, data: CommandeFournisseurCreate) -> CommandeFournisseur:
    commande = CommandeFournisseur(**data.model_dump())
    db.add(commande)
    db.commit()
    db.refresh(commande)
    return commande


def get_commande(db: Session, commande_id: int) -> CommandeFournisseur:
    commande = db.query(CommandeFournisseur).filter_by(id=commande_id).first()
    if not commande:
        raise HTTPException(status_code=404, detail="Commande introuvable")
    return commande


def list_commandes(db: Session, skip: int = 0, limit: int = 50) -> List[CommandeFournisseur]:
    return db.query(CommandeFournisseur).offset(skip).limit(limit).all()


def update_commande(db: Session, commande_id: int, data: CommandeFournisseurUpdate) -> CommandeFournisseur:
    commande = get_commande(db, commande_id)
    if str(commande.statut) != str(StatutCommandeFournisseur.brouillon):
        raise HTTPException(status_code=400, detail="Seules les commandes en brouillon peuvent être modifiées.")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(commande, field, value)
    db.commit()
    db.refresh(commande)
    return commande


def delete_commande(db: Session, commande_id: int) -> dict:
    commande = get_commande(db, commande_id)
    if str(commande.statut) != str(StatutCommandeFournisseur.brouillon):
        raise HTTPException(status_code=400, detail="Seules les commandes en brouillon peuvent être supprimées.")
    db.delete(commande)
    db.commit()
    return {"detail": "Commande supprimée avec succès."}


# -------- SEARCH --------

def search_commandes(db: Session, filters: CommandeFournisseurSearch, skip: int = 0, limit: int = 50):
    query = db.query(CommandeFournisseur)

    if filters.numero_commande:
        query = query.filter(CommandeFournisseur.numero_commande.ilike(f"%{filters.numero_commande}%"))
    if filters.fournisseur_id:
        query = query.filter(CommandeFournisseur.fournisseur_id == filters.fournisseur_id)
    if filters.statut:
        query = query.filter(CommandeFournisseur.statut == filters.statut)
    if filters.date_min:
        query = query.filter(CommandeFournisseur.date_commande >= filters.date_min)
    if filters.date_max:
        query = query.filter(CommandeFournisseur.date_commande <= filters.date_max)
    if filters.is_archived is not None:
        query = query.filter(CommandeFournisseur.is_archived == filters.is_archived)

    total = query.count()
    results = query.order_by(CommandeFournisseur.date_commande.desc()).offset(skip).limit(limit).all()
    return {"total": total, "results": results}


# -------- EXPORT --------

def export_commandes_csv(db: Session) -> io.StringIO:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "ID", "Numéro", "Fournisseur", "Montant", "Statut", "Date", "Devise"
    ])
    for c in db.query(CommandeFournisseur).all():
        writer.writerow([
            c.id,
            c.numero_commande,
            c.fournisseur_id,
            c.montant_total,
            c.statut,
            c.date_commande.strftime("%Y-%m-%d") if getattr(c, "date_commande", None) else "",
            c.devise
        ])
    buffer.seek(0)
    return buffer


# -------- BULK CREATE --------

def bulk_create_commandes(db: Session, data: List[CommandeFournisseurCreate]) -> List[CommandeFournisseur]:
    objets = [CommandeFournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(objets)
    db.commit()
    return objets


# -------- BULK DELETE --------

def bulk_delete_commandes(db: Session, ids: List[int]) -> int:
    commandes = db.query(CommandeFournisseur).filter(CommandeFournisseur.id.in_(ids)).all()
    count = 0
    for c in commandes:
        if str(c.statut) == str(StatutCommandeFournisseur.brouillon):
            db.delete(c)
            count += 1
    db.commit()
    return count
