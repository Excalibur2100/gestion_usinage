from sqlalchemy.orm import Session
from db.models.tables.surveillance_cameras import SurveillanceCamera
from backend.db.schemas.surveillance_camera_schemas.surveillance_camera_schemas import (
    SurveillanceCameraCreate,
    SurveillanceCameraUpdate
)

def create_camera(db: Session, data: SurveillanceCameraCreate) -> SurveillanceCamera:
    camera = SurveillanceCamera(**data.dict())
    db.add(camera)
    db.commit()
    db.refresh(camera)
    return camera

def get_all_cameras(db: Session):
    return db.query(SurveillanceCamera).all()

def get_camera_by_id(db: Session, camera_id: int):
    return db.query(SurveillanceCamera).filter(SurveillanceCamera.id == camera_id).first()

def update_camera(db: Session, camera_id: int, data: SurveillanceCameraUpdate):
    camera = get_camera_by_id(db, camera_id)
    if camera:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(camera, key, value)
        db.commit()
        db.refresh(camera)
    return camera

def delete_camera(db: Session, camera_id: int):
    camera = get_camera_by_id(db, camera_id)
    if camera:
        db.delete(camera)
        db.commit()
    return camera

