from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.workflow_document import WorkflowDocument
from db.schemas.ged.workflow_document_schemas import *

def create_workflow_liaison(db: Session, data: WorkflowDocumentCreate) -> WorkflowDocument:
    obj = WorkflowDocument(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_workflow_liaison(db: Session, id_: int) -> Optional[WorkflowDocument]:
    return db.query(WorkflowDocument).filter(WorkflowDocument.id == id_).first()

def get_all_workflow_liaisons(db: Session) -> List[WorkflowDocument]:
    return db.query(WorkflowDocument).all()

def update_workflow_liaison(db: Session, id_: int, data: WorkflowDocumentUpdate) -> Optional[WorkflowDocument]:
    obj = get_workflow_liaison(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_workflow_liaison(db: Session, id_: int) -> bool:
    obj = get_workflow_liaison(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_workflow_liaisons(db: Session, search_data: WorkflowDocumentSearch) -> List[WorkflowDocument]:
    query = db.query(WorkflowDocument)
    if search_data.document_id:
        query = query.filter(WorkflowDocument.document_id == search_data.document_id)
    if search_data.workflow_id:
        query = query.filter(WorkflowDocument.workflow_id == search_data.workflow_id)
    if search_data.statut:
        query = query.filter(WorkflowDocument.statut == search_data.statut)
    return query.all()