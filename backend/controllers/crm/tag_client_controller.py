from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.tag_client_schemas import *
from services.crm.tag_client_service import *

router = APIRouter(prefix="/tags-clients", tags=["Tags Clients"])

@router.post("/", response_model=TagClientRead)
def create(data: TagClientCreate, db: Session = Depends(get_db)):
    return create_tag_client(db, data)

@router.get("/", response_model=List[TagClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_tags_clients(db)

@router.get("/{id_}", response_model=TagClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_tag_client(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Association tag-client non trouvée")
    return obj

@router.put("/{id_}", response_model=TagClientRead)
def update(id_: int, data: TagClientUpdate, db: Session = Depends(get_db)):
    obj = update_tag_client(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Association tag-client non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_tag_client(db, id_):
        raise HTTPException(status_code=404, detail="Association tag-client non trouvée")
    return {"ok": True}

@router.post("/search", response_model=TagClientSearchResults)
def search(data: TagClientSearch, db: Session = Depends(get_db)):
    return {"results": search_tag_clients(db, data)}