from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.assistant_ia_schemas import *
from services.ia.assistant_ia_service import *

router = APIRouter(prefix="/assistants-ia", tags=["Assistant IA"])

@router.post("/", response_model=AssistantIARead)
def create(data: AssistantIACreate, db: Session = Depends(get_db)):
    return create_session(db, data)

@router.get("/", response_model=List[AssistantIARead])
def read_all(db: Session = Depends(get_db)):
    return get_all_sessions(db)

@router.get("/{id_}", response_model=AssistantIARead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_session(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    return obj

@router.put("/{id_}", response_model=AssistantIARead)
def update(id_: int, data: AssistantIAUpdate, db: Session = Depends(get_db)):
    obj = update_session(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_session(db, id_):
        raise HTTPException(status_code=404, detail="Session non trouvée")
    return {"ok": True}

@router.post("/search", response_model=AssistantIASearchResults)
def search(data: AssistantIASearch, db: Session = Depends(get_db)):
    return {"results": search_sessions(db, data)}