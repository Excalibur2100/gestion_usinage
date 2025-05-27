from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.conditions_coupe_schemas import *
from services.ia.conditions_coupe_service import *

router = APIRouter(prefix="/conditions-coupe", tags=["Conditions de Coupe"])

@router.post("/", response_model=ConditionsCoupeRead)
def create(data: ConditionsCoupeCreate, db: Session = Depends(get_db)):
    return create_conditions(db, data)

@router.get("/", response_model=List[ConditionsCoupeRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_conditions(db)

@router.get("/{id_}", response_model=ConditionsCoupeRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_conditions(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Conditions non trouvées")
    return obj

@router.put("/{id_}", response_model=ConditionsCoupeRead)
def update(id_: int, data: ConditionsCoupeUpdate, db: Session = Depends(get_db)):
    obj = update_conditions(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Conditions non trouvées")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_conditions(db, id_):
        raise HTTPException(status_code=404, detail="Conditions non trouvées")
    return {"ok": True}

@router.post("/search", response_model=ConditionsCoupeSearchResults)
def search(data: ConditionsCoupeSearch, db: Session = Depends(get_db)):
    return {"results": search_conditions(db, data)}