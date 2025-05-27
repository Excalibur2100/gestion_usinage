from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.client_schemas import *
from backend.services.crm.client_service import *

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=ClientRead)
def create(data: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, data)

@router.get("/", response_model=List[ClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_clients(db)

@router.get("/{client_id}", response_model=ClientRead)
def read(client_id: int, db: Session = Depends(get_db)):
    obj = get_client(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return obj

@router.put("/{client_id}", response_model=ClientRead)
def update(client_id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    obj = update_client(db, client_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return obj

@router.delete("/{client_id}")
def delete(client_id: int, db: Session = Depends(get_db)):
    if not delete_client(db, client_id):
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ClientSearchResults)
def search(data: ClientSearch, db: Session = Depends(get_db)):
    return {"results": search_clients(db, data)}