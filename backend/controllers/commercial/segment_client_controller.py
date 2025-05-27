from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.segment_client_schemas import *
from services.commercial.segment_client_service import *

router = APIRouter(prefix="/segments-clients", tags=["Segments Client"])

@router.post("/", response_model=SegmentClientRead)
def create(data: SegmentClientCreate, db: Session = Depends(get_db)):
    return create_segment(db, data)

@router.get("/", response_model=List[SegmentClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_segments(db)

@router.get("/{id_}", response_model=SegmentClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_segment(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Segment non trouvé")
    return obj

@router.put("/{id_}", response_model=SegmentClientRead)
def update(id_: int, data: SegmentClientUpdate, db: Session = Depends(get_db)):
    obj = update_segment(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Segment non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_segment(db, id_):
        raise HTTPException(status_code=404, detail="Segment non trouvé")
    return {"ok": True}

@router.post("/search", response_model=SegmentClientSearchResults)
def search(data: SegmentClientSearch, db: Session = Depends(get_db)):
    return {"results": search_segments(db, data)}
