from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.contact_client_schemas import *
from services.crm.contact_client_service import *

router = APIRouter(prefix="/contacts-client", tags=["Contacts Client"])

@router.post("/", response_model=ContactClientRead)
def create(data: ContactClientCreate, db: Session = Depends(get_db)):
    return create_contact(db, data)

@router.get("/", response_model=List[ContactClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_contacts(db)

@router.get("/{id_}", response_model=ContactClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_contact(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Contact non trouvé")
    return obj

@router.put("/{id_}", response_model=ContactClientRead)
def update(id_: int, data: ContactClientUpdate, db: Session = Depends(get_db)):
    obj = update_contact(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Contact non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_contact(db, id_):
        raise HTTPException(status_code=404, detail="Contact non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ContactClientSearchResults)
def search(data: ContactClientSearch, db: Session = Depends(get_db)):
    return {"results": search_contacts(db, data)}