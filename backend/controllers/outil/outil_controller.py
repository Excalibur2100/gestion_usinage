from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.outils_schemas.outils_schemas import OutilCreate, OutilUpdate, OutilRead
from services.outil.outil_services import (
    create_outil,
    get_all_outils,
    get_outil_by_id,
    update_outil,
    delete_outil
)

router = APIRouter(prefix="/api/outils", tags=["Outils"])

@router.post("/", response_model=OutilRead)
def create(data: OutilCreate, db: Session = Depends(get_db)):
    return create_outil(db, data)

@router.get("/", response_model=list[OutilRead])
def read_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all_outils(db, skip, limit)

@router.get("/{outil_id}", response_model=OutilRead)
def read_one(outil_id: int, db: Session = Depends(get_db)):
    outil = get_outil_by_id(db, outil_id)
    if not outil:
        raise HTTPException(status_code=404, detail="Outil non trouvé")
    return outil

@router.put("/{outil_id}", response_model=OutilRead)
def update(outil_id: int, data: OutilUpdate, db: Session = Depends(get_db)):
    outil = update_outil(db, outil_id, data)
    if not outil:
        raise HTTPException(status_code=404, detail="Outil non trouvé")
    return outil

@router.delete("/{outil_id}")
def delete(outil_id: int, db: Session = Depends(get_db)):
    if not delete_outil(db, outil_id):
        raise HTTPException(status_code=404, detail="Outil non trouvé")
    return {"detail": "Outil supprimé"}
