from sqlalchemy.orm import Session
from backend.db.models.tables.production.ordre_fabrication import OrdreFabrication
from db.schemas.ordre_fabrication_schemas.ordre_fabrication_schemas import OFCreate, OFUpdate

def create_of(db: Session, data: OFCreate) -> OrdreFabrication:
    of = OrdreFabrication(**data.model_dump())
    db.add(of)
    db.commit()
    db.refresh(of)
    return of

def get_all_ofs(db: Session, skip: int = 0, limit: int = 100) -> list[OrdreFabrication]:
    return db.query(OrdreFabrication).offset(skip).limit(limit).all()

def get_of_by_id(db: Session, of_id: int) -> OrdreFabrication | None:
    return db.query(OrdreFabrication).filter(OrdreFabrication.id == of_id).first()

def update_of(db: Session, of_id: int, data: OFUpdate) -> OrdreFabrication | None:
    of = get_of_by_id(db, of_id)
    if of:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(of, key, value)
        db.commit()
        db.refresh(of)
    return of

def delete_of(db: Session, of_id: int) -> bool:
    of = get_of_by_id(db, of_id)
    if of:
        db.delete(of)
        db.commit()
        return True
    return False

def get_of_by_numero(db: Session, numero: str) -> OrdreFabrication | None:
    return db.query(OrdreFabrication).filter(OrdreFabrication.numero == numero).first()