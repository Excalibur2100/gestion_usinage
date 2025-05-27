from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.config.config_notification import ConfigNotification
from db.schemas.config.config_notification_schemas import *

def create_notification(db: Session, data: ConfigNotificationCreate) -> ConfigNotification:
    obj = ConfigNotification(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_notification(db: Session, id_: int) -> Optional[ConfigNotification]:
    return db.query(ConfigNotification).filter(ConfigNotification.id == id_).first()

def get_all_notifications(db: Session) -> List[ConfigNotification]:
    return db.query(ConfigNotification).all()

def update_notification(db: Session, id_: int, data: ConfigNotificationUpdate) -> Optional[ConfigNotification]:
    obj = get_notification(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_notification(db: Session, id_: int) -> bool:
    obj = get_notification(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_notifications(db: Session, search_data: ConfigNotificationSearch) -> List[ConfigNotification]:
    query = db.query(ConfigNotification)
    if search_data.evenement:
        query = query.filter(ConfigNotification.evenement.ilike(f"%{search_data.evenement}%"))
    if search_data.canal:
        query = query.filter(ConfigNotification.canal.ilike(f"%{search_data.canal}%"))
    if search_data.actif is not None:
        query = query.filter(ConfigNotification.actif == search_data.actif)
    return query.all()