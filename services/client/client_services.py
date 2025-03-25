from sqlalchemy.orm import Session
from db.models.models import Client
from db.schemas.schemas import ClientCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_client(db: Session, client_data: ClientCreate) -> Client:
    client = Client(**client_data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

# ========== TOUS ==========
def get_tous_clients(db: Session) -> List[Client]:
    return db.query(Client).all()

# ========== PAR ID ==========
def get_client_par_id(db: Session, client_id: int) -> Optional[Client]:
    return db.query(Client).filter(Client.id == client_id).first()

# ========== MISE À JOUR ==========
def update_client(db: Session, client_id: int, client_data: ClientCreate) -> Optional[Client]:
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        for key, value in client_data.dict().items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return client

# ========== SUPPRESSION ==========
def supprimer_client(db: Session, client_id: int) -> None:
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
