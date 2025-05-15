from sqlalchemy.orm import Session
from backend.db.models.table.rh.poste import Poste
from backend.db.schemas.rh.poste_schemas import PosteCreate, PosteUpdate

def create_poste(db: Session, data: PosteCreate) -> Poste:
    poste = Poste(**data.model_dump())
    db.add(poste)
    db.commit()
    db.refresh(poste)
    return poste

def get_all_postes(db: Session, skip: int = 0, limit: int = 100) -> list[Poste]:
    return db.query(Poste).offset(skip).limit(limit).all()

def get_poste_by_id(db: Session, poste_id: int) -> Poste | None:
    return db.query(Poste).filter(Poste.id == poste_id).first()

def update_poste(db: Session, poste_id: int, data: PosteUpdate) -> Poste | None:
    poste = get_poste_by_id(db, poste_id)
    if poste:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(poste, key, value)
        db.commit()
        db.refresh(poste)
    return poste

def delete_poste(db: Session, poste_id: int) -> bool:
    poste = get_poste_by_id(db, poste_id)
    if poste:
        db.delete(poste)
        db.commit()
        return True
    return False
