from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.remise_client_schemas import *
from services.commercial.remise_client_service import *

router = APIRouter(prefix="/remises-clients", tags=["Remises Client"])

@router.post("/", response_model=RemiseClientRead)
def create(data: RemiseClientCreate, db: Session = Depends(get_db)):
    return create_remise(db, data)

@router.get("/", response_model=List[RemiseClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_remises(db)

@router.get("/{id_}", response_model=RemiseClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_remise(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Remise non trouvée")
    return obj

@router.put("/{id_}", response_model=RemiseClientRead)
def update(id_: int, data: RemiseClientUpdate, db: Session = Depends(get_db)):
    obj = update_remise(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Remise non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_remise(db, id_):
        raise HTTPException(status_code=404, detail="Remise non trouvée")
    return {"ok": True}

@router.post("/search", response_model=RemiseClientSearchResults)
def search(data: RemiseClientSearch, db: Session = Depends(get_db)):
    return {"results": search_remises(db, data)}
