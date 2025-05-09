from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.absence_schemas.absence_schemas import AbsenceCreate, AbsenceUpdate, AbsenceRead
from services.absence.absence_service import (
    create_absence,
    get_all_absences,
    get_absence_by_id,
    update_absence,
    delete_absence
)

router = APIRouter(prefix="/api/absences", tags=["Absences"])

@router.post("/", response_model=AbsenceRead)
def create(data: AbsenceCreate, db: Session = Depends(get_db)):
    return create_absence(db, data)

@router.get("/", response_model=list[AbsenceRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_absences(db)

@router.get("/{absence_id}", response_model=AbsenceRead)
def read_one(absence_id: int, db: Session = Depends(get_db)):
    absence = get_absence_by_id(db, absence_id)
    if not absence:
        raise HTTPException(status_code=404, detail="Absence non trouvée")
    return absence

@router.put("/{absence_id}", response_model=AbsenceRead)
def update(absence_id: int, data: AbsenceUpdate, db: Session = Depends(get_db)):
    absence = update_absence(db, absence_id, data)
    if not absence:
        raise HTTPException(status_code=404, detail="Absence non trouvée")
    return absence

@router.delete("/{absence_id}")
def delete(absence_id: int, db: Session = Depends(get_db)):
    success = delete_absence(db, absence_id)
    if not success:
        raise HTTPException(status_code=404, detail="Absence non trouvée")
    return {"detail": "Absence supprimée"}
