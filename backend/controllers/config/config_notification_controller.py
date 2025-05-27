from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.config.config_notification_schemas import *
from services.config.config_notification_service import *

router = APIRouter(prefix="/config-notifications", tags=["Configuration Notifications"])

@router.post("/", response_model=ConfigNotificationRead)
def create(data: ConfigNotificationCreate, db: Session = Depends(get_db)):
    return create_notification(db, data)

@router.get("/", response_model=List[ConfigNotificationRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_notifications(db)

@router.get("/{id_}", response_model=ConfigNotificationRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_notification(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Notification non trouvée")
    return obj

@router.put("/{id_}", response_model=ConfigNotificationRead)
def update(id_: int, data: ConfigNotificationUpdate, db: Session = Depends(get_db)):
    obj = update_notification(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Notification non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_notification(db, id_):
        raise HTTPException(status_code=404, detail="Notification non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConfigNotificationSearchResults)
def search(data: ConfigNotificationSearch, db: Session = Depends(get_db)):
    return {"results": search_notifications(db, data)}