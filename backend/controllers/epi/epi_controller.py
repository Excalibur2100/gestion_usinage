from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.epi_schemas.epi_schemas import EPICreate, EPIUpdate, EPIRead
from services.epi.epi_service import (
    create_epi,
    get_all_epis,
    get_epi_by_id,
    update_epi,
    delete_epi
)

router = APIRouter(prefix="/api/epis", tags=["EPI"])

@router.post("/", response_model=EPIRead)
def create(data: EPICreate, db: Session = Depends(get_db)):
    return create_epi(db, data)

@router.get("/", response_model=list[EPIRead])
def read_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all_epis(db, skip, limit)

@router.get("/{epi_id}", response_model=EPIRead)
def read_one(epi_id: int, db: Session = Depends(get_db)):
    epi = get_epi_by_id(db, epi_id)
    if not epi:
        raise HTTPException(status_code=404, detail="Équipement non trouvé")
    return epi

@router.put("/{epi_id}", response_model=EPIRead)
def update(epi_id: int, data: EPIUpdate, db: Session = Depends(get_db)):
    epi = update_epi(db, epi_id, data)
    if not epi:
        raise HTTPException(status_code=404, detail="Équipement non trouvé")
    return epi

@router.delete("/{epi_id}")
def delete(epi_id: int, db: Session = Depends(get_db)):
    if not delete_epi(db, epi_id):
        raise HTTPException(status_code=404, detail="Équipement non trouvé")
    return {"detail": "Équipement supprimé"}
