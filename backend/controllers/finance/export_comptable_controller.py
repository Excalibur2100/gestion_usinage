from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.export_comptable_schemas import *
from services.finance.export_comptable_service import *

router = APIRouter(prefix="/exports-comptables", tags=["Exports Comptables"])

@router.post("/", response_model=ExportComptableRead)
def create(data: ExportComptableCreate, db: Session = Depends(get_db)):
    return create_export(db, data)

@router.get("/", response_model=List[ExportComptableRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_exports(db)

@router.get("/{id_}", response_model=ExportComptableRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_export(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Export non trouvé")
    return obj

@router.put("/{id_}", response_model=ExportComptableRead)
def update(id_: int, data: ExportComptableUpdate, db: Session = Depends(get_db)):
    obj = update_export(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Export non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_export(db, id_):
        raise HTTPException(status_code=404, detail="Export non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ExportComptableSearchResults)
def search(data: ExportComptableSearch, db: Session = Depends(get_db)):
    return {"results": search_exports(db, data)}