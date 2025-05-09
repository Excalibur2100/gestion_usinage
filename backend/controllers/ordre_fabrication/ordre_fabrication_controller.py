from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ordre_fabrication_schemas.ordre_fabrication_schemas import OFCreate, OFUpdate, OFRead
from services.ordre_fabrication.ordre_fabrication_services import (
    create_of,
    get_all_ofs,
    get_of_by_id,
    update_of,
    delete_of,
    get_of_by_numero
)

router = APIRouter(prefix="/api/ordres-fabrication", tags=["Ordres Fabrication"])

@router.post("/", response_model=OFRead)
def create(data: OFCreate, db: Session = Depends(get_db)):
    return create_of(db, data)

@router.get("/", response_model=list[OFRead])
def read_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all_ofs(db, skip, limit)

@router.get("/{of_id}", response_model=OFRead)
def read_one(of_id: int, db: Session = Depends(get_db)):
    of = get_of_by_id(db, of_id)
    if not of:
        raise HTTPException(status_code=404, detail="Ordre non trouvé")
    return of

@router.put("/{of_id}", response_model=OFRead)
def update(of_id: int, data: OFUpdate, db: Session = Depends(get_db)):
    of = update_of(db, of_id, data)
    if not of:
        raise HTTPException(status_code=404, detail="Ordre non trouvé")
    return of

@router.delete("/{of_id}")
def delete(of_id: int, db: Session = Depends(get_db)):
    if not delete_of(db, of_id):
        raise HTTPException(status_code=404, detail="Ordre non trouvé")
    return {"detail": "Ordre supprimé"}

@router.get("/numero/{numero}", response_model=OFRead)
def read_by_numero(numero: str, db: Session = Depends(get_db)):
    of = get_of_by_numero(db, numero)
    if not of:
        raise HTTPException(status_code=404, detail="Ordre non trouvé")
    return of
