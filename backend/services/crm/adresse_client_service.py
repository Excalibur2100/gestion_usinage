from sqlalchemy.orm import Session
from db.models.tables.crm.adresse_client import AdresseClient
from schemas.crm.adresse_client_schemas import AdresseClientCreate, AdresseClientUpdate

def create_adresse(db: Session, data: AdresseClientCreate):
    adresse = AdresseClient(**data.dict())
    db.add(adresse)
    db.commit()
    db.refresh(adresse)
    return adresse

def get_adresses_by_client(db: Session, client_id: int):
    return db.query(AdresseClient).filter(AdresseClient.client_id == client_id).all()

def update_adresse(db: Session, adresse_id: int, update_data: AdresseClientUpdate):
    adresse = db.query(AdresseClient).filter(AdresseClient.id == adresse_id).first()
    if not adresse:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(adresse, key, value)
    db.commit()
    db.refresh(adresse)
    return adresse

def delete_adresse(db: Session, adresse_id: int):
    adresse = db.query(AdresseClient).filter(AdresseClient.id == adresse_id).first()
    if adresse:
        db.delete(adresse)
        db.commit()
    return adresse
def get_adresse_by_id(db: Session, adresse_id: int):
    return db.query(AdresseClient).filter(AdresseClient.id == adresse_id).first()