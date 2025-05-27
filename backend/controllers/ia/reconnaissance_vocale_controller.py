from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.reconnaissance_vocale_schemas import *
from services.ia.reconnaissance_vocale_service import *

router = APIRouter(prefix="/reconnaissances-vocales", tags=["Reconnaissance Vocale"])

@router.post("/", response_model=ReconnaissanceVocaleRead)
def create(data: ReconnaissanceVocaleCreate, db: Session = Depends(get_db)):
    return create_reconnaissance(db, data)

@router.get("/", response_model=List[ReconnaissanceVocaleRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_reconnaissances(db)

@router.get("/{id_}", response_model=ReconnaissanceVocaleRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_reconnaissance(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Reconnaissance non trouvée")
    return obj

@router.put("/{id_}", response_model=ReconnaissanceVocaleRead)
def update(id_: int, data: ReconnaissanceVocaleUpdate, db: Session = Depends(get_db)):
    obj = update_reconnaissance(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Reconnaissance non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_reconnaissance(db, id_):
        raise HTTPException(status_code=404, detail="Reconnaissance non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ReconnaissanceVocaleSearchResults)
def search(data: ReconnaissanceVocaleSearch, db: Session = Depends(get_db)):
    return {"results": search_reconnaissances(db, data)}