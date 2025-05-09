from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from services.absence.absence_service import (
    get_absences,
    get_absence_by_id,
    create_absence,
    update_absence,
    delete_absence,
)
from backend.db.schemas.absence_schemas.absence_schemas import AbsenceCreate, AbsenceUpdate

router = APIRouter(prefix="/absence", tags=["absence"])

@router.get("/", response_model=list)
def list_absences(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_absences(db, skip=skip, limit=limit)

@router.get("/{absence_id}", response_model=dict)
def get_absence(absence_id: int, db: Session = Depends(get_db)):
    return get_absence_by_id(db, absence_id)

@router.post("/", response_model=dict)
def create_new_absence(absence_data: AbsenceCreate, db: Session = Depends(get_db)):
    return create_absence(db, absence_data)

@router.put("/{absence_id}", response_model=dict)
def update_existing_absence(absence_id: int, absence_data: AbsenceUpdate, db: Session = Depends(get_db)):
    return update_absence(db, absence_id, absence_data)

@router.delete("/{absence_id}")
def delete_existing_absence(absence_id: int, db: Session = Depends(get_db)):
    delete_absence(db, absence_id)
    return {"message": "Absence deleted successfully"}