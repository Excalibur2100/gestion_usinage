from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import SurveillanceCameraCreate, SurveillanceCameraRead
from services.robotique.surveillance_camera import (
    creer_camera,
    get_toutes_cameras,
    get_camera_par_id,
    update_camera,
    supprimer_camera,
)

router = APIRouter(prefix="/surveillance-cameras", tags=["Surveillance Caméras"])

@router.post("/", response_model=SurveillanceCameraRead)
def create(data: SurveillanceCameraCreate, db: Session = Depends(get_db)):
    return creer_camera(db, data)

@router.get("/", response_model=list[SurveillanceCameraRead])
def read_all(db: Session = Depends(get_db)):
    return get_toutes_cameras(db)

@router.get("/{id}", response_model=SurveillanceCameraRead)
def read_one(id: int, db: Session = Depends(get_db)):
    camera = get_camera_par_id(db, id)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra non trouvée")
    return camera

@router.put("/{id}", response_model=SurveillanceCameraRead)
def update(id: int, data: SurveillanceCameraCreate, db: Session = Depends(get_db)):
    camera = update_camera(db, id, data)
    if not camera:
        raise HTTPException(status_code=404, detail="Caméra non trouvée pour mise à jour")
    return camera

@router.delete("/{id}", status_code=204)
def delete(id: int, db: Session = Depends(get_db)):
    supprimer_camera(db, id)
    return

@router.get("/")
async def get_surveillance_cameras():
    return {"message": "Liste des caméras de surveillance"}
