from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ged.workflow_document_schemas import *
from services.ged.workflow_document_service import *

router = APIRouter(prefix="/workflows-documents", tags=["Workflow Documents"])

@router.post("/", response_model=WorkflowDocumentRead)
def create(data: WorkflowDocumentCreate, db: Session = Depends(get_db)):
    return create_workflow_liaison(db, data)

@router.get("/", response_model=List[WorkflowDocumentRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_workflow_liaisons(db)

@router.get("/{id_}", response_model=WorkflowDocumentRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_workflow_liaison(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Liaison non trouvée")
    return obj

@router.put("/{id_}", response_model=WorkflowDocumentRead)
def update(id_: int, data: WorkflowDocumentUpdate, db: Session = Depends(get_db)):
    obj = update_workflow_liaison(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Liaison non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_workflow_liaison(db, id_):
        raise HTTPException(status_code=404, detail="Liaison non trouvée")
    return {"ok": True}

@router.post("/search", response_model=WorkflowDocumentSearchResults)
def search(data: WorkflowDocumentSearch, db: Session = Depends(get_db)):
    return {"results": search_workflow_liaisons(db, data)}