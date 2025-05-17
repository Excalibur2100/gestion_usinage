from sqlalchemy.orm import Session
from db.models.tables.crm.fichier_client import FichierClient
from schemas.crm.fichier_client_schemas import FichierClientCreate, FichierClientUpdate

def create_fichier(db: Session, data: FichierClientCreate):
    fichier = FichierClient(**data.dict())
    db.add(fichier)
    db.commit()
    db.refresh(fichier)
    return fichier

def get_all_fichiers(db: Session):
    return db.query(FichierClient).order_by(FichierClient.date_upload.desc()).all()

def get_fichiers_by_client(db: Session, client_id: int):
    return db.query(FichierClient).filter(FichierClient.client_id == client_id).all()

def get_fichier_by_id(db: Session, fichier_id: int):
    return db.query(FichierClient).filter(FichierClient.id == fichier_id).first()

def update_fichier(db: Session, fichier_id: int, update_data: FichierClientUpdate):
    fichier = get_fichier_by_id(db, fichier_id)
    if not fichier:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(fichier, field, value)
    db.commit()
    db.refresh(fichier)
    return fichier

def delete_fichier(db: Session, fichier_id: int):
    fichier = get_fichier_by_id(db, fichier_id)
    if fichier:
        db.delete(fichier)
        db.commit()
    return fichier

def search_fichiers(db: Session, query: str, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    return (
        db.query(FichierClient)
        .filter(FichierClient.nom_fichier.ilike(f"%{query}%"))
        .order_by(FichierClient.date_upload.desc())
        .offset(offset)
        .limit(per_page)
        .all()
    )
def count_fichiers(db: Session, query: str):
    return (
        db.query(FichierClient)
        .filter(FichierClient.nom_fichier.ilike(f"%{query}%"))
        .count()
    )
def count_fichiers_by_client(db: Session, client_id: int):
    return (
        db.query(FichierClient)
        .filter(FichierClient.client_id == client_id)
        .count()
    )