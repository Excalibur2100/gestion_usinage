from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.chiffrage_schemas import *
from services.ia.chiffrage_service import *

router = APIRouter(prefix="/chiffrages", tags=["Chiffrage"])

@router.post("/", response_model=ChiffrageRead)
def create(data: ChiffrageCreate, db: Session = Depends(get_db)):
    return create_chiffrage(db, data)

@router.get("/", response_model=List[ChiffrageRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_chiffrages(db)

@router.get("/{id_}", response_model=ChiffrageRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_chiffrage(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Chiffrage non trouvé")
    return obj

@router.put("/{id_}", response_model=ChiffrageRead)
def update(id_: int, data: ChiffrageUpdate, db: Session = Depends(get_db)):
    obj = update_chiffrage(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Chiffrage non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_chiffrage(db, id_):
        raise HTTPException(status_code=404, detail="Chiffrage non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ChiffrageSearchResults)
def search(data: ChiffrageSearch, db: Session = Depends(get_db)):
    return {"results": search_chiffrages(db, data)}