from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables import SurveillanceCamera
from db.schemas.surveillance_camera_schemas import SurveillanceCameraCreate

def creer_camera(db: Session, data: SurveillanceCameraCreate) -> SurveillanceCamera:
    camera = SurveillanceCamera(**data.model_dump())
    db.add(camera)
    db.commit()
    db.refresh(camera)
    return camera

def get_toutes_cameras(db: Session) -> List[SurveillanceCamera]:
    return db.query(SurveillanceCamera).all()

def get_camera_par_id(db: Session, camera_id: int) -> Optional[SurveillanceCamera]:
    return db.query(SurveillanceCamera).filter(SurveillanceCamera.id == camera_id).first()

def update_camera(db: Session, camera_id: int, data: SurveillanceCameraCreate) -> Optional[SurveillanceCamera]:
    camera = get_camera_par_id(db, camera_id)
    if camera:
        for key, value in data.model_dump().items():
            setattr(camera, key, value)
        db.commit()
        db.refresh(camera)
    return camera

def supprimer_camera(db: Session, camera_id: int) -> None:
    camera = get_camera_par_id(db, camera_id)
    if camera:
        db.delete(camera)
        db.commit()

