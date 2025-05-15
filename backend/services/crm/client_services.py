from sqlalchemy.orm import Session
from db.models.tables.crm.client import Client
from db.schemas.crm.client_schemas import ClientCreate, ClientUpdate

def create_client(db: Session, client_data: ClientCreate):
    client = Client(**client_data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def get_all_clients(db: Session):
    return db.query(Client).order_by(Client.nom_entreprise).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, update_data: ClientUpdate):
    client = get_client_by_id(db, client_id)
    if not client:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(client, field, value)
    db.commit()
    db.refresh(client)
    return client

def delete_client(db: Session, client_id: int):
    client = get_client_by_id(db, client_id)
    if client:
        db.delete(client)
        db.commit()
    return client

def search_clients(db: Session, query: str):
    return db.query(Client).filter(Client.nom_entreprise.ilike(f"%{query}%")).all()
