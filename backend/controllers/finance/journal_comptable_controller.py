from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.journal_comptable_schemas import *
from services.finance.journal_comptable_service import *

router = APIRouter(prefix="/journal-comptable", tags=["Journal Comptable"])

@router.post("/", response_model=JournalComptableRead)
def create(data: JournalComptableCreate, db: Session = Depends(get_db)):
    return create_ecriture(db, data)

@router.get("/", response_model=List[JournalComptableRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_ecritures(db)

@router.get("/{id_}", response_model=JournalComptableRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_ecriture(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Écriture non trouvée")
    return obj

@router.put("/{id_}", response_model=JournalComptableRead)
def update(id_: int, data: JournalComptableUpdate, db: Session = Depends(get_db)):
    obj = update_ecriture(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Écriture non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_ecriture(db, id_):
        raise HTTPException(status_code=404, detail="Écriture non trouvée")
    return {"ok": True}

@router.post("/search", response_model=JournalComptableSearchResults)
def search(data: JournalComptableSearch, db: Session = Depends(get_db)):
    return {"results": search_ecritures(db, data)}