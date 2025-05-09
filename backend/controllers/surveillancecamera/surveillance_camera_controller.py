import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.schemas.surveillance_camera_schemas.surveillance_camera_schemas import (
    SurveillanceCameraCreate,
    SurveillanceCameraRead,
    SurveillanceCameraUpdate
)
from services.surveillance_camera.surveillance_camera_service import (
    create_camera,
    get_all_cameras,
    get_camera_by_id,
    update_camera,
    delete_camera
)
from db.models.database import get_db

router = APIRouter(prefix="/api/surveillance-cameras", tags=["Surveillance Cameras"])

@router.post("/", response_model=SurveillanceCameraRead)
def create(data: SurveillanceCameraCreate, db: Session = Depends(get_db)):
    return create_camera(db, data)

@router.get("/", response_model=list[SurveillanceCameraRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_cameras(db)

@router.get("/{camera_id}", response_model=SurveillanceCameraRead)
def read_one(camera_id: int, db: Session = Depends(get_db)):
    camera = get_camera_by_id(db, camera_id)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra non trouvée")
    return camera

@router.put("/{camera_id}", response_model=SurveillanceCameraRead)
def update(camera_id: int, data: SurveillanceCameraUpdate, db: Session = Depends(get_db)):
    camera = update_camera(db, camera_id, data)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra non trouvée")
    return camera

@router.delete("/{camera_id}")
def delete(camera_id: int, db: Session = Depends(get_db)):
    camera = delete_camera(db, camera_id)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra non trouvée")
    return {"detail": "Caméra supprimée"}
