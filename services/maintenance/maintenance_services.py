from sqlalchemy.orm import Session
from db.models.tables import Maintenance
from db.schemas.schemas import MaintenanceCreate
from typing import List, Optional

# ========== CRÉER ==========
def creer_maintenance(db: Session, maintenance_data: MaintenanceCreate) -> Maintenance:
    maintenance = Maintenance(**maintenance_data.dict())
    db.add(maintenance)
    db.commit()
    db.refresh(maintenance)
    return maintenance

# ========== TOUS ==========
def get_toutes_maintenances(db: Session) -> List[Maintenance]:
    return db.query(Maintenance).all()

# ========== PAR ID ==========
def get_maintenance_par_id(db: Session, maintenance_id: int) -> Optional[Maintenance]:
    return db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()

# ========== MISE À JOUR ==========
def update_maintenance(db: Session, maintenance_id: int, maintenance_data: MaintenanceCreate) -> Optional[Maintenance]:
    maintenance = get_maintenance_par_id(db, maintenance_id)
    if maintenance:
        for key, value in maintenance_data.dict().items():
            setattr(maintenance, key, value)
        db.commit()
        db.refresh(maintenance)
    return maintenance

# ========== SUPPRESSION ==========
def supprimer_maintenance(db: Session, maintenance_id: int) -> None:
    maintenance = get_maintenance_par_id(db, maintenance_id)
    if maintenance:
        db.delete(maintenance)
        db.commit()