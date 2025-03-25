from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import MaintenanceCreate, MaintenanceRead
from services.maintenance.maintenance_services import (
    creer_maintenance,
    get_toutes_maintenances,
    get_maintenance_par_id,
    update_maintenance,
    supprimer_maintenance
)

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])

@router.post("/", response_model=MaintenanceRead)
def creer(maintenance_data: MaintenanceCreate, db: Session = Depends(get_db)):
    return creer_maintenance(db, maintenance_data)

@router.get("/", response_model=list[MaintenanceRead])
def lire_toutes(db: Session = Depends(get_db)):
    return get_toutes_maintenances(db)

@router.get("/{id}", response_model=MaintenanceRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    maintenance = get_maintenance_par_id(db, id)
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance non trouvée")
    return maintenance

@router.put("/{id}", response_model=MaintenanceRead)
def maj(id: int, maintenance_data: MaintenanceCreate, db: Session = Depends(get_db)):
    maintenance = update_maintenance(db, id, maintenance_data)
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance non trouvée pour mise à jour")
    return maintenance

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_maintenance(db, id)
    return
