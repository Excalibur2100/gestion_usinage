from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.log_ia_schemas import *
from services.ia.logs_ia_service import *

router = APIRouter(prefix="/logs-ia", tags=["Logs IA"])

@router.post("/", response_model=LogIARead)
def create(data: LogIACreate, db: Session = Depends(get_db)):
    return create_log(db, data)

@router.get("/", response_model=List[LogIARead])
def read_all(db: Session = Depends(get_db)):
    return get_all_logs(db)

@router.get("/{id_}", response_model=LogIARead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_log(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Log IA non trouvé")
    return obj

@router.put("/{id_}", response_model=LogIARead)
def update(id_: int, data: LogIAUpdate, db: Session = Depends(get_db)):
    obj = update_log(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Log IA non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_log(db, id_):
        raise HTTPException(status_code=404, detail="Log IA non trouvé")
    return {"ok": True}

@router.post("/search", response_model=LogIASearchResults)
def search(data: LogIASearch, db: Session = Depends(get_db)):
    return {"results": search_logs(db, data)}