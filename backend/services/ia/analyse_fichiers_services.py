from sqlalchemy.orm import Session
from backend.db.models.tables.ia.analyse_fichier import AnalyseFichier
from backend.db.schemas.ia.analyse_fichier_schemas import AnalyseFichierCreate, AnalyseFichierUpdate
from fastapi import HTTPException

def get_analyses_fichiers(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des analyses de fichiers.
    """
    return db.query(AnalyseFichier).offset(skip).limit(limit).all()

def get_analyse_fichier_by_id(db: Session, analyse_id: int):
    """
    Récupère une analyse de fichier par son ID.
    """
    analyse = db.query(AnalyseFichier).filter(AnalyseFichier.id == analyse_id).first()
    if not analyse:
        raise HTTPException(status_code=404, detail="Analyse de fichier non trouvée")
    return analyse

def create_analyse_fichier(db: Session, analyse_data: AnalyseFichierCreate):
    """
    Crée une nouvelle analyse de fichier.
    """
    analyse = AnalyseFichier(
        nom_fichier=analyse_data.nom_fichier,
        type_fichier=analyse_data.type_fichier,
        resultat=analyse_data.resultat,
        date_analyse=analyse_data.date_analyse,
    )
    db.add(analyse)
    db.commit()
    db.refresh(analyse)
    return analyse

def update_analyse_fichier(db: Session, analyse_id: int, analyse_data: AnalyseFichierUpdate):
    """
    Met à jour une analyse de fichier existante.
    """
    analyse = get_analyse_fichier_by_id(db, analyse_id)
    if analyse_data.nom_fichier:
        analyse.nom_fichier = analyse_data.nom_fichier
    if analyse_data.type_fichier:
        setattr(analyse, "type_fichier", analyse_data.type_fichier)
    if analyse_data.resultat:
        analyse.resultat = analyse_data.resultat
    if analyse_data.date_analyse:
        setattr(analyse, "date_analyse", analyse_data.date_analyse)
    db.commit()
    db.refresh(analyse)
    return analyse

def delete_analyse_fichier(db: Session, analyse_id: int):
    """
    Supprime une analyse de fichier par son ID.
    """
    analyse = get_analyse_fichier_by_id(db, analyse_id)
    db.delete(analyse)
    db.commit()