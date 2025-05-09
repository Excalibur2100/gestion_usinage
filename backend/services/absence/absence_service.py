# Service généré automatiquement
# Module : absence
from sqlalchemy.orm import Session
from  db.models.tables.absence import Absence
from backend.db.schemas.absence_schemas.absence_schemas import AbsenceCreate, AbsenceUpdate
from fastapi import HTTPException

def get_absences(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée d'absences.
    """
    return db.query(Absence).offset(skip).limit(limit).all()

def get_absence_by_id(db: Session, absence_id: int):
    """
    Récupère une absence par son ID.
    """
    absence = db.query(Absence).filter(Absence.id == absence_id).first()
    if not absence:
        raise HTTPException(status_code=404, detail="Absence non trouvée")
    return absence

def create_absence(db: Session, absence_data: AbsenceCreate):
    """
    Crée une nouvelle absence.
    """
    absence = Absence(
        utilisateur_id=absence_data.utilisateur_id,
        date_debut=absence_data.date_debut,
        date_fin=absence_data.date_fin,
        type_absence=absence_data.type_absence,
        commentaire=absence_data.commentaire,
    )
    db.add(absence)
    db.commit()
    db.refresh(absence)
    return absence

def update_absence(db: Session, absence_id: int, absence_data: AbsenceUpdate):
    """
    Met à jour une absence existante.
    """
    absence = get_absence_by_id(db, absence_id)
    if absence_data.date_debut:
        absence.date_debut = absence_data.date_debut
    if absence_data.date_fin:
        absence.date_fin = absence_data.date_fin
    if absence_data.type_absence:
        absence.type_absence = absence_data.type_absence
    if absence_data.commentaire:
        absence.commentaire = absence_data.commentaire
    db.commit()
    db.refresh(absence)
    return absence

def delete_absence(db: Session, absence_id: int):
    """
    Supprime une absence par son ID.
    """
    absence = get_absence_by_id(db, absence_id)
    db.delete(absence)
    db.commit()