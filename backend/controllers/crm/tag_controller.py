from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.tag_schemas import *
from services.crm.tag_service import *

router = APIRouter(prefix="/tags", tags=["Tags"])

@router.post("/", response_model=TagRead)
def create(data: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, data)

@router.get("/", response_model=List[TagRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_tags(db)

@router.get("/{id_}", response_model=TagRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_tag(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Tag non trouvé")
    return obj

@router.put("/{id_}", response_model=TagRead)
def update(id_: int, data: TagUpdate, db: Session = Depends(get_db)):
    obj = update_tag(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Tag non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_tag(db, id_):
        raise HTTPException(status_code=404, detail="Tag non trouvé")
    return {"ok": True}

@router.post("/search", response_model=TagSearchResults)
def search(data: TagSearch, db: Session = Depends(get_db)):
    return {"results": search_tags(db, data)}