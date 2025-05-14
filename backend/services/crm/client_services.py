from sqlalchemy.orm import Session
from backend.db.models.tables.crm.clients import Client
from backend.db.schemas.crm.client_schemas import ClientCreate, ClientRead
from typing import List, Optional
from fastapi import HTTPException

# ========== CRÉATION ==========
def creer_client(db: Session, client_data: ClientCreate) -> Client:
    """
    Crée un nouveau client.
    """
    client = Client(**client_data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

# ========== TOUS ==========
def get_tous_clients(db: Session) -> List[Client]:
    """
    Récupère tous les clients.
    """
    return db.query(Client).all()

# ========== PAR ID ==========
def get_client_par_id(db: Session, client_id: int) -> Optional[Client]:
    """
    Récupère un client par son ID.
    """
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

# ========== MISE À JOUR ==========
def update_client(db: Session, client_id: int, client_data: ClientCreate) -> Optional[Client]:
    """
    Met à jour un client existant.
    """
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    for key, value in client_data.dict().items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

# ========== SUPPRESSION ==========
def supprimer_client(db: Session, client_id: int) -> None:
    """
    Supprime un client par son ID.
    """
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    db.delete(client)
    db.commit()