from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.action_commerciale import ActionCommerciale
from db.schemas.commercial.action_commerciale_schemas import *

def create_action(db: Session, data: ActionCommercialeCreate) -> ActionCommerciale:
    obj = ActionCommerciale(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_action(db: Session, action_id: int) -> Optional[ActionCommerciale]:
    return db.query(ActionCommerciale).filter(ActionCommerciale.id == action_id).first()

def get_all_actions(db: Session) -> List[ActionCommerciale]:
    return db.query(ActionCommerciale).all()

def update_action(db: Session, action_id: int, data: ActionCommercialeUpdate) -> Optional[ActionCommerciale]:
    obj = get_action(db, action_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_action(db: Session, action_id: int) -> bool:
    obj = get_action(db, action_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_actions(db: Session, search_data: ActionCommercialeSearch) -> List[ActionCommerciale]:
    query = db.query(ActionCommerciale)
    if search_data.type_action:
        query = query.filter(ActionCommerciale.type_action.ilike(f"%{search_data.type_action}%"))
    if search_data.client_id:
        query = query.filter(ActionCommerciale.client_id == search_data.client_id)
    if search_data.utilisateur_id:
        query = query.filter(ActionCommerciale.utilisateur_id == search_data.utilisateur_id)
    return query.all()
