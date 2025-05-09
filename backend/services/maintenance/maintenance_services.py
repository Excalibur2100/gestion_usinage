from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.maintenance import Maintenance
from backend.db.schemas.maintenance_schemas.maintenance_schemas import MaintenanceCreate, MaintenanceUpdate

def creer_maintenance(db: Session, maintenance_data: MaintenanceCreate) -> Maintenance:
    """
    Crée une nouvelle maintenance.
    """
    maintenance = Maintenance(**maintenance_data.dict())
    db.add(maintenance)
    db.commit()
    db.refresh(maintenance)
    return maintenance

def get_toutes_maintenances(db: Session) -> List[Maintenance]:
    """
    Récupère toutes les maintenances.
    """
    return db.query(Maintenance).all()

def get_maintenance_par_id(db: Session, maintenance_id: int) -> Optional[Maintenance]:
    """
    Récupère une maintenance par son ID.
    """
    return db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()

def update_maintenance(db: Session, maintenance_id: int, maintenance_data: MaintenanceUpdate) -> Optional[Maintenance]:
    """
    Met à jour une maintenance existante.
    """
    maintenance = get_maintenance_par_id(db, maintenance_id)
    if maintenance:
        for key, value in maintenance_data.dict(exclude_unset=True).items():
            setattr(maintenance, key, value)
        db.commit()
        db.refresh(maintenance)
    return maintenance

def supprimer_maintenance(db: Session, maintenance_id: int) -> None:
    """
    Supprime une maintenance par son ID.
    """
    maintenance = get_maintenance_par_id(db, maintenance_id)
    if maintenance:
        db.delete(maintenance)
        db.commit()