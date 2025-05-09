from sqlalchemy.orm import Session
from db.models.tables.epi import EPI
from db.schemas.epi_schemas.epi_schemas import EPICreate, EPIUpdate

def create_epi(db: Session, data: EPICreate) -> EPI:
    epi = EPI(**data.model_dump())
    db.add(epi)
    db.commit()
    db.refresh(epi)
    return epi

def get_all_epis(db: Session, skip: int = 0, limit: int = 100) -> list[EPI]:
    return db.query(EPI).offset(skip).limit(limit).all()

def get_epi_by_id(db: Session, epi_id: int) -> EPI | None:
    return db.query(EPI).filter(EPI.id == epi_id).first()

def update_epi(db: Session, epi_id: int, data: EPIUpdate) -> EPI | None:
    epi = get_epi_by_id(db, epi_id)
    if epi:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(epi, key, value)
        db.commit()
        db.refresh(epi)
    return epi

def delete_epi(db: Session, epi_id: int) -> bool:
    epi = get_epi_by_id(db, epi_id)
    if epi:
        db.delete(epi)
        db.commit()
        return True
    return False
