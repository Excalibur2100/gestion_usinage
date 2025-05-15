from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.schemas.systeme.version_systeme_schemas import VersionSystemeCreate, VersionSystemeRead
from db.services.systeme.version_systeme_service import create_version, get_all_versions, get_version_by_id

router = APIRouter(prefix="/versions", tags=["Version système"])

@router.post("/", response_model=VersionSystemeRead)
def create(version: VersionSystemeCreate, db: Session = Depends(get_db)):
    return create_version(db, version)

@router.get("/", response_model=list[VersionSystemeRead])
def list_versions(db: Session = Depends(get_db)):
    return get_all_versions(db)

@router.get("/{version_id}", response_model=VersionSystemeRead)
def read_version(version_id: int, db: Session = Depends(get_db)):
    version = get_version_by_id(db, version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version non trouvée")
    return version
