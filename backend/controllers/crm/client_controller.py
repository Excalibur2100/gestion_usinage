from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.schemas.crm.client_schemas import (
    ClientCreate, ClientRead, ClientUpdate, ClientDelete, ClientList,
    ClientSearch, ClientSearchResults
)
from db.services.crm.client_service import (
    create_client, get_all_clients, get_client_by_id,
    update_client, delete_client, search_clients
)

router = APIRouter(prefix="/clients", tags=["Client"])

@router.post("/", response_model=ClientRead)
def create(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/", response_model=ClientList)
def list_clients(db: Session = Depends(get_db)):
    clients = get_all_clients(db)
    return {"clients": clients}

@router.get("/{client_id}", response_model=ClientRead)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

@router.put("/{client_id}", response_model=ClientRead)
def update(client_id: int, client_data: ClientUpdate, db: Session = Depends(get_db)):
    updated = update_client(db, client_id, client_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return updated

@router.delete("/{client_id}", response_model=ClientDelete)
def delete(client_id: int, db: Session = Depends(get_db)):
    deleted = delete_client(db, client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return {"id": client_id}

@router.post("/search", response_model=ClientSearchResults)
def search(search: ClientSearch, db: Session = Depends(get_db)):
    results = search_clients(db, search.query)
    return {"results": results}
