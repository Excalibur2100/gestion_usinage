from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import select, and_, func
from starlette.responses import StreamingResponse
import io
import csv

from backend.db.models.tables.achat.commande_fournisseur import CommandeFournisseur
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    CommandeFournisseurUpdate,
    CommandeFournisseurSearch
)


# -------- CRUD --------
def create_commande(db: Session, data: CommandeFournisseurCreate) -> CommandeFournisseur:
    new_commande = CommandeFournisseur(**data.model_dump())
    db.add(new_commande)
    db.commit()
    db.refresh(new_commande)
    return new_commande


def get_commande(db: Session, commande_id: int) -> CommandeFournisseur:
    commande = db.get(CommandeFournisseur, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée.")
    return commande


def update_commande(db: Session, commande_id: int, data: CommandeFournisseurUpdate) -> CommandeFournisseur:
    commande = get_commande(db, commande_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(commande, key, value)
    db.commit()
    db.refresh(commande)
    return commande


def delete_commande(db: Session, commande_id: int) -> dict:
    commande = get_commande(db, commande_id)
    db.delete(commande)
    db.commit()
    return {"detail": "Commande supprimée avec succès."}


# -------- SEARCH --------
def search_commandes(
    db: Session,
    filters: CommandeFournisseurSearch,
    skip: int = 0,
    limit: int = 100
) -> List[CommandeFournisseur]:

    query = select(CommandeFournisseur)
    conditions = []

    if filters.numero_commande:
        conditions.append(CommandeFournisseur.numero_commande.ilike(f"%{filters.numero_commande}%"))
    if filters.fournisseur_id:
        conditions.append(CommandeFournisseur.fournisseur_id == filters.fournisseur_id)
    if filters.statut:
        conditions.append(CommandeFournisseur.statut == filters.statut)
    if filters.date_min:
        conditions.append(CommandeFournisseur.date_commande >= filters.date_min)
    if filters.date_max:
        conditions.append(CommandeFournisseur.date_commande <= filters.date_max)
    if filters.is_archived is not None:
        conditions.append(CommandeFournisseur.is_archived == filters.is_archived)

    if conditions:
        query = query.where(and_(*conditions))

    query = query.order_by(CommandeFournisseur.date_commande.desc())
    query = query.offset(skip).limit(limit)

    return list(db.scalars(query))


# -------- BULK --------
def bulk_create_commandes(db: Session, data: List[CommandeFournisseurCreate]) -> List[CommandeFournisseur]:
    objets = [CommandeFournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(objets)
    db.commit()
    return objets


def bulk_delete_commandes(db: Session, ids: List[int]) -> dict:
    db.query(CommandeFournisseur).filter(CommandeFournisseur.id.in_(ids)).delete(synchronize_session=False)
    db.commit()
    return {"detail": f"{len(ids)} commandes supprimées"}


# -------- EXPORT --------
def export_commandes_csv(db: Session) -> StreamingResponse:
    commandes = db.scalars(select(CommandeFournisseur)).all()
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["ID", "Numéro", "Fournisseur", "Statut", "Montant", "Date", "Devise"])
    for c in commandes:
        writer.writerow([
            c.id,
            c.numero_commande,
            c.fournisseur_id,
            c.statut,
            c.montant_total,
            c.date_commande.strftime("%Y-%m-%d") if c.date_commande is not None else "",
            c.devise
        ])
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=commandes.csv"})