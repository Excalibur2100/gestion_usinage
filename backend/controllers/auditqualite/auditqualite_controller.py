from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from services.auditqualite.auditqualite_service import (
    get_audits_qualite,
    get_audit_qualite_by_id,
    create_audit_qualite,
    update_audit_qualite,
    delete_audit_qualite,
)
from backend.db.schemas.audit_qualite_schemas.audit_qualite_schemas import AuditQualiteCreate, AuditQualiteUpdate

router = APIRouter(prefix="/audit_qualite", tags=["Audit Qualité"])

@router.get("/", response_model=list)
def list_audits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_audits_qualite(db, skip=skip, limit=limit)

@router.get("/{audit_id}", response_model=dict)
def get_audit(audit_id: int, db: Session = Depends(get_db)):
    return get_audit_qualite_by_id(db, audit_id)

@router.post("/", response_model=dict)
def create_audit(audit_data: AuditQualiteCreate, db: Session = Depends(get_db)):
    return create_audit_qualite(db, audit_data)

@router.put("/{audit_id}", response_model=dict)
def update_audit(audit_id: int, audit_data: AuditQualiteUpdate, db: Session = Depends(get_db)):
    return update_audit_qualite(db, audit_id, audit_data)

@router.delete("/{audit_id}")
def delete_audit(audit_id: int, db: Session = Depends(get_db)):
    delete_audit_qualite(db, audit_id)
    return {"message": "Audit qualité supprimé avec succès"}