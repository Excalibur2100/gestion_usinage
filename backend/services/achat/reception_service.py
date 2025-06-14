from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_

from backend.db.models.tables.achat.receptions import Reception
from backend.db.schemas.achat.reception_schemas import (
    ReceptionCreate,
    ReceptionUpdate,
    ReceptionSearch
)


def create_reception(db: Session, reception_in: ReceptionCreate) -> Reception:
    reception = Reception(**reception_in.dict())
    db.add(reception)
    db.commit()
    db.refresh(reception)
    return reception


def get_reception_by_id(db: Session, reception_id: int) -> Optional[Reception]:
    return db.get(Reception, reception_id)


def get_all_receptions(db: Session, skip: int = 0, limit: int = 100) -> List[Reception]:
    return list(
        db.execute(
            select(Reception).offset(skip).limit(limit)
        ).scalars().all()
    )


def update_reception(db: Session, reception_id: int, reception_in: ReceptionUpdate) -> Optional[Reception]:
    reception = db.get(Reception, reception_id)
    if not reception:
        return None
    for field, value in reception_in.dict(exclude_unset=True).items():
        setattr(reception, field, value)
    db.commit()
    db.refresh(reception)
    return reception


def delete_reception(db: Session, reception_id: int) -> bool:
    reception = db.get(Reception, reception_id)
    if not reception:
        return False
    db.delete(reception)
    db.commit()
    return True


def search_receptions(db: Session, search: ReceptionSearch) -> List[Reception]:
    query = select(Reception)

    filters = []

    if search.numero_reception:
        filters.append(Reception.numero_reception.ilike(f"%{search.numero_reception}%"))

    if search.commande_id:
        filters.append(Reception.commande_id == search.commande_id)

    if search.statut:
        filters.append(Reception.statut == search.statut)

    if search.date_debut and search.date_fin:
        filters.append(Reception.date_reception.between(search.date_debut, search.date_fin))
    elif search.date_debut:
        filters.append(Reception.date_reception >= search.date_debut)
    elif search.date_fin:
        filters.append(Reception.date_reception <= search.date_fin)

    if filters:
        query = query.where(and_(*filters))

    return list(db.execute(query).scalars().all())


def bulk_create_receptions(db: Session, receptions_in: List[ReceptionCreate]) -> List[Reception]:
    receptions = [Reception(**reception.dict()) for reception in receptions_in]
    db.add_all(receptions)
    db.commit()
    for reception in receptions:
        db.refresh(reception)
    return receptions