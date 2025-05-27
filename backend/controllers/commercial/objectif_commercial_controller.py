from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.objectif_commercial_schemas import *
from services.commercial.objectif_commercial_service import *

router = APIRouter(prefix="/objectifs-commerciaux", tags=["Objectifs Commerciaux"])

@router.post("/", response_model=ObjectifCommercialRead)
def create(data: ObjectifCommercialCreate, db: Session = Depends(get_db)):
    return create_objectif(db, data)

@router.get("/", response_model=List[ObjectifCommercialRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_objectifs(db)

@router.get("/{id_}", response_model=ObjectifCommercialRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_objectif(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Objectif non trouvé")
    return obj

@router.put("/{id_}", response_model=ObjectifCommercialRead)
def update(id_: int, data: ObjectifCommercialUpdate, db: Session = Depends(get_db)):
    obj = update_objectif(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Objectif non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_objectif(db, id_):
        raise HTTPException(status_code=404, detail="Objectif non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ObjectifCommercialSearchResults)
def search(data: ObjectifCommercialSearch, db: Session = Depends(get_db)):
    return {"results": search_objectifs(db, data)}
