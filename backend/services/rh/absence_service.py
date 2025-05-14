from sqlalchemy.orm import Session
from db.models.tables.absence import Absence
from db.schemas.absence_schemas.absence_schemas import AbsenceCreate, AbsenceUpdate

def create_absence(db: Session, data: AbsenceCreate) -> Absence:
    absence = Absence(**data.model_dump())
    db.add(absence)
    db.commit()
    db.refresh(absence)
    return absence

def get_all_absences(db: Session, skip: int = 0, limit: int = 100) -> list[Absence]:
    return db.query(Absence).offset(skip).limit(limit).all()

def get_absence_by_id(db: Session, absence_id: int) -> Absence | None:
    return db.query(Absence).filter(Absence.id == absence_id).first()

def update_absence(db: Session, absence_id: int, data: AbsenceUpdate) -> Absence | None:
    absence = get_absence_by_id(db, absence_id)
    if absence:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(absence, key, value)
        db.commit()
        db.refresh(absence)
    return absence

def delete_absence(db: Session, absence_id: int) -> bool:
    absence = get_absence_by_id(db, absence_id)
    if absence:
        db.delete(absence)
        db.commit()
        return True
    return False
