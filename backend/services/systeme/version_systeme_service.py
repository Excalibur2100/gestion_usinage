from sqlalchemy.orm import Session
from db.models.tables.systeme.version_systeme import VersionSysteme
from db.schemas.systeme.version_systeme_schemas import VersionSystemeCreate

def create_version(db: Session, version_data: VersionSystemeCreate):
    version = VersionSysteme(**version_data.dict())
    db.add(version)
    db.commit()
    db.refresh(version)
    return version

def get_all_versions(db: Session):
    return db.query(VersionSysteme).order_by(VersionSysteme.date_appliquee.desc()).all()

def get_version_by_id(db: Session, version_id: int):
    return db.query(VersionSysteme).filter(VersionSysteme.id == version_id).first()
