from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.surveillance_cameras import SurveillanceCamera
from db.schemas.surveillance_camera_schemas import SurveillanceCameraCreate

def creer_camera(db: Session, camera_data: SurveillanceCameraCreate) -> SurveillanceCamera:
    """
    Crée une nouvelle caméra de surveillance.
    """
    camera = SurveillanceCamera(**camera_data.dict())
    db.add(camera)
    db.commit()
    db.refresh(camera)
    return camera
def get_cameras(db: Session) -> List[SurveillanceCamera]:
    """
    Récupère toutes les caméras de surveillance.
    """
    return db.query(SurveillanceCamera).all()

def get_camera_par_id(db: Session, camera_id: int) -> Optional[SurveillanceCamera]:
    """
    Récupère une caméra de surveillance par son ID.
    """
    return db.query(SurveillanceCamera).filter(SurveillanceCamera.id == camera_id).first()

def update_camera(db: Session, camera_id: int, camera_data: SurveillanceCameraCreate) -> Optional[SurveillanceCamera]:
    """
    Met à jour une caméra de surveillance par son ID.
    """
    camera = get_camera_par_id(db, camera_id)
    if camera:
        for key, value in camera_data.dict(exclude_unset=True).items():
            setattr(camera, key, value)
        db.commit()
        db.refresh(camera)
    return camera

def supprimer_camera(db: Session, camera_id: int) -> None:
    """
    Supprime une caméra de surveillance par son ID.
    """
    camera = get_camera_par_id(db, camera_id)
    if camera:
        db.delete(camera)
        db.commit()