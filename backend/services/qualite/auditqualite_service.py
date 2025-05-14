from sqlalchemy.orm import Session
from db.models.tables.audit_qualite import AuditQualite
from backend.db.schemas.audit_qualite_schemas.audit_qualite_schemas import AuditQualiteCreate, AuditQualiteUpdate
from fastapi import HTTPException

def get_audits_qualite(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des audits qualité.
    """
    return db.query(AuditQualite).offset(skip).limit(limit).all()

def get_audit_qualite_by_id(db: Session, audit_id: int):
    """
    Récupère un audit qualité par son ID.
    """
    audit = db.query(AuditQualite).filter(AuditQualite.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit qualité non trouvé")
    return audit

def create_audit_qualite(db: Session, audit_data: AuditQualiteCreate):
    """
    Crée un nouvel audit qualité.
    """
    audit = AuditQualite(
        responsable_utilisateur_id=audit_data.responsable_utilisateur_id,
        date_audit=audit_data.date_audit,
        type_audit=audit_data.type_audit,
        resultat=audit_data.resultat,
        commentaire=audit_data.commentaire,
    )
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit

def update_audit_qualite(db: Session, audit_id: int, audit_data: AuditQualiteUpdate):
    """
    Met à jour un audit qualité existant.
    """
    audit = get_audit_qualite_by_id(db, audit_id)
    if audit_data.responsable_utilisateur_id:
        audit.responsable_utilisateur_id = audit_data.responsable_utilisateur_id
    if audit_data.date_audit:
        audit.date_audit = audit_data.date_audit
    if audit_data.type_audit:
        audit.type_audit = audit_data.type_audit
    if audit_data.resultat:
        audit.resultat = audit_data.resultat
    if audit_data.commentaire:
        audit.commentaire = audit_data.commentaire
    db.commit()
    db.refresh(audit)
    return audit

def delete_audit_qualite(db: Session, audit_id: int):
    """
    Supprime un audit qualité par son ID.
    """
    audit = get_audit_qualite_by_id(db, audit_id)
    db.delete(audit)
    db.commit()