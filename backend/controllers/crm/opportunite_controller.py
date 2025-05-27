from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.opportunite_schemas import *
from services.crm.opportunite_service import *

router = APIRouter(prefix="/opportunites", tags=["Opportunités Client"])

@router.post("/", response_model=OpportuniteRead)
def create(data: OpportuniteCreate, db: Session = Depends(get_db)):
    return create_opportunite(db, data)

@router.get("/", response_model=List[OpportuniteRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_opportunites(db)

@router.get("/{id_}", response_model=OpportuniteRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_opportunite(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Opportunité non trouvée")
    return obj

@router.put("/{id_}", response_model=OpportuniteRead)
def update(id_: int, data: OpportuniteUpdate, db: Session = Depends(get_db)):
    obj = update_opportunite(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Opportunité non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_opportunite(db, id_):
        raise HTTPException(status_code=404, detail="Opportunité non trouvée")
    return {"ok": True}

@router.post("/search", response_model=OpportuniteSearchResults)
def search(data: OpportuniteSearch, db: Session = Depends(get_db)):
    return {"results": search_opportunites(db, data)}