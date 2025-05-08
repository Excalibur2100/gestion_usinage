from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from services.client.client_services import (
    creer_client,
    get_tous_clients,
    get_client_par_id,
    update_client,
    supprimer_client,
)
from db.schemas.client_schemas import ClientCreate, ClientRead

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

@router.get("/", response_model=list[ClientRead])
def list_clients(db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer tous les clients.
    """
    return get_tous_clients(db)

@router.get("/{client_id}", response_model=ClientRead)
def get_client(client_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer un client spécifique par son ID.
    """
    return get_client_par_id(db, client_id)

@router.post("/", response_model=ClientRead)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    """
    Endpoint pour créer un nouveau client.
    """
    return creer_client(db, client)

@router.put("/{client_id}", response_model=ClientRead)
def update_client_endpoint(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    """
    Endpoint pour mettre à jour un client existant.
    """
    return update_client(db, client_id, client)

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour supprimer un client par son ID.
    """
    supprimer_client(db, client_id)
    return {"message": f"Client avec l'ID {client_id} supprimé avec succès"}