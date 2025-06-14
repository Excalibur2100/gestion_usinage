from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
import csv
import io

from backend.db.models.tables.achat.fournisseurs import Fournisseur
from backend.db.schemas.achat.fournisseur_schemas import (
    FournisseurCreate,
    FournisseurUpdate,
    FournisseurSearch,
)

# -------- CRUD --------

def creer_fournisseur(db: Session, data: FournisseurCreate) -> Fournisseur:
    fournisseur = Fournisseur(**data.model_dump())
    db.add(fournisseur)
    db.commit()
    db.refresh(fournisseur)
    return fournisseur

def get_fournisseur(db: Session, fournisseur_id: int) -> Fournisseur:
    fournisseur = db.query(Fournisseur).filter_by(id=fournisseur_id).first()
    if not fournisseur:
        raise HTTPException(status_code=404, detail="Fournisseur introuvable")
    return fournisseur

def list_fournisseurs(db: Session, skip: int = 0, limit: int = 100) -> List[Fournisseur]:
    return db.query(Fournisseur).offset(skip).limit(limit).all()

def update_fournisseur(db: Session, fournisseur_id: int, data: FournisseurUpdate) -> Fournisseur:
    fournisseur = get_fournisseur(db, fournisseur_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(fournisseur, field, value)
    db.commit()
    db.refresh(fournisseur)
    return fournisseur

def delete_fournisseur(db: Session, fournisseur_id: int) -> dict:
    fournisseur = get_fournisseur(db, fournisseur_id)
    db.delete(fournisseur)
    db.commit()
    return {"detail": "Fournisseur supprimé avec succès."}

# -------- SEARCH --------

def search_fournisseurs(db: Session, filters: FournisseurSearch, skip: int = 0, limit: int = 50):
    query = db.query(Fournisseur)

    if filters.nom:
        query = query.filter(Fournisseur.nom.ilike(f"%{filters.nom}%"))
    if filters.code:
        query = query.filter(Fournisseur.code.ilike(f"%{filters.code}%"))
    if filters.type:
        query = query.filter(Fournisseur.type == filters.type)
    if filters.statut:
        query = query.filter(Fournisseur.statut == filters.statut)
    if filters.pays:
        query = query.filter(Fournisseur.pays.ilike(f"%{filters.pays}%"))
    if filters.actif is not None:
        query = query.filter(Fournisseur.actif == filters.actif)

    total = query.count()
    results = query.offset(skip).limit(limit).all()

    return {"total": total, "results": results}

# -------- EXPORT --------

def export_fournisseurs_csv(db: Session) -> io.StringIO:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "ID", "Nom", "Code", "Type", "Statut", "Email", "Téléphone", "Pays", "Actif"
    ])
    for f in db.query(Fournisseur).all():
        writer.writerow([
            f.id,
            f.nom,
            f.code or "",
            f.type.value if getattr(f, "type", None) is not None else "",
            f.statut.value if getattr(f, "statut", None) is not None else "",
            f.email or "",
            f.telephone or "",
            f.pays or "",
            "Oui" if getattr(f, "actif", False) else "Non"
        ])
    buffer.seek(0)
    return buffer

# -------- BULK --------

def bulk_create_fournisseurs(db: Session, data: List[FournisseurCreate]) -> List[Fournisseur]:
    fournisseurs = [Fournisseur(**item.model_dump()) for item in data]
    db.bulk_save_objects(fournisseurs)
    db.commit()
    return fournisseurs

def bulk_delete_fournisseurs(db: Session, ids: List[int]) -> int:
    fournisseurs = db.query(Fournisseur).filter(Fournisseur.id.in_(ids)).all()
    count = len(fournisseurs)
    for f in fournisseurs:
        db.delete(f)
    db.commit()
    return count