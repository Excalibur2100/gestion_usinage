from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.models.database import get_db
from backend.db.schemas.surveillance_camera_schemas import SurveillanceCameraCreate, SurveillanceCameraRead
from backend.services.surveillance_camera.surveillancecamera_service import (
    creer_camera,
    get_cameras,
    get_camera_par_id,
    update_camera,
    supprimer_camera
)

router = APIRouter(prefix="/surveillance-cameras", tags=["Surveillance Cameras"])

@router.post("/", response_model=SurveillanceCameraRead)
def creer(camera_data: SurveillanceCameraCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle caméra de surveillance.
    """
    return creer_camera(db, camera_data)

@router.get("/", response_model=list[SurveillanceCameraRead])
def lire_toutes(db: Session = Depends(get_db)):
    """
    Récupère toutes les caméras de surveillance.
    """
    return get_cameras(db)

@router.get("/{id}", response_model=SurveillanceCameraRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    """
    Récupère une caméra de surveillance par son ID.
    """
    camera = get_camera_par_id(db, id)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra de surveillance non trouvée")
    return camera

@router.put("/{id}", response_model=SurveillanceCameraRead)
def maj(id: int, camera_data: SurveillanceCameraCreate, db: Session = Depends(get_db)):
    """
    Met à jour une caméra de surveillance par son ID.
    """
    camera = update_camera(db, id, camera_data)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra de surveillance non trouvée pour mise à jour")
    return camera

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    """
    Supprime une caméra de surveillance par son ID.
    """
    supprimer_camera(db, id)
    return