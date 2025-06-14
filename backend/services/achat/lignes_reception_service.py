from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.db.models.tables.achat.lignes_reception import LigneReception
from backend.db.schemas.achat.lignes_reception_schemas import (
    LigneReceptionCreate, LigneReceptionUpdate, LigneReceptionSearch
)

def creer_ligne_reception(db: Session, data: LigneReceptionCreate):
    ligne = LigneReception(**data.dict())
    db.add(ligne)
    db.commit()
    db.refresh(ligne)
    return ligne

def get_ligne_reception(db: Session, ligne_id: int):
    ligne = db.query(LigneReception).filter(LigneReception.id == ligne_id).first()
    if not ligne:
        raise HTTPException(status_code=404, detail="Ligne de réception non trouvée")
    return ligne

def list_lignes_reception(db: Session, skip: int = 0, limit: int = 20):
    return db.query(LigneReception).offset(skip).limit(limit).all()

def update_ligne_reception(db: Session, ligne_id: int, data: dict):
    ligne = get_ligne_reception(db, ligne_id)
    for key, value in data.items():
        setattr(ligne, key, value)
    db.commit()
    db.refresh(ligne)
    return ligne

def delete_ligne_reception(db: Session, ligne_id: int):
    ligne = get_ligne_reception(db, ligne_id)
    db.delete(ligne)
    db.commit()
    return {"detail": "Ligne supprimée avec succès"}

def bulk_create_lignes_reception(db: Session, data: list):
    objets = [LigneReception(**item.dict()) for item in data]
    db.add_all(objets)
    db.commit()
    for obj in objets:
        db.refresh(obj)
    return objets

def bulk_delete_lignes_reception(db: Session, ids: list):
    count = db.query(LigneReception).filter(LigneReception.id.in_(ids)).delete(synchronize_session=False)
    db.commit()
    return count

def search_lignes_reception(db: Session, filters: LigneReceptionSearch):
    query = db.query(LigneReception)
    if filters.designation:
        query = query.filter(LigneReception.designation.like(f"%{filters.designation}%"))
    if filters.reception_id:
        query = query.filter(LigneReception.reception_id == filters.reception_id)
    if filters.statut:
        query = query.filter(LigneReception.statut == filters.statut)
    if filters.etat:
        query = query.filter(LigneReception.etat == filters.etat)
    if filters.date_debut:
        query = query.filter(LigneReception.timestamp_creation >= filters.date_debut)
    if filters.date_fin:
        query = query.filter(LigneReception.timestamp_creation <= filters.date_fin)
    results = query.all()
    return {"results": results, "total": len(results)}

def export_lignes_reception_csv(db: Session):
    import io, csv
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "ID", "Réception", "Désignation", "Quantité commandée", "Quantité reçue", "Statut", "Etat", "Date création"
    ])
    for l in db.query(LigneReception).all():
        writer.writerow([
            l.id, l.reception_id, l.designation, l.quantite_commandee, l.quantite_recue, l.statut, l.etat, l.timestamp_creation
        ])
    output.seek(0)
    return output