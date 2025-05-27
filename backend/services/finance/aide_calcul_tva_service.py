from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.aide_calcul_tva import AideCalculTVA
from db.schemas.finance.aide_calcul_tva_schemas import *

def create_aide_tva(db: Session, data: AideCalculTVACreate) -> AideCalculTVA:
    obj = AideCalculTVA(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_aide_tva(db: Session, id_: int) -> Optional[AideCalculTVA]:
    return db.query(AideCalculTVA).filter(AideCalculTVA.id == id_).first()

def get_all_aides_tva(db: Session) -> List[AideCalculTVA]:
    return db.query(AideCalculTVA).all()

def update_aide_tva(db: Session, id_: int, data: AideCalculTVAUpdate) -> Optional[AideCalculTVA]:
    obj = get_aide_tva(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_aide_tva(db: Session, id_: int) -> bool:
    obj = get_aide_tva(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_aides_tva(db: Session, search_data: AideCalculTVASearch) -> List[AideCalculTVA]:
    query = db.query(AideCalculTVA)
    if search_data.calcul_type:
        query = query.filter(AideCalculTVA.calcul_type == search_data.calcul_type)
    return query.all()