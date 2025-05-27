from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class WorkflowDocumentBase(BaseModel):
    document_id: int
    workflow_id: int
    statut: Optional[str] = "en attente"

    class Config:
        from_attributes = True

class WorkflowDocumentCreate(WorkflowDocumentBase):
    pass

class WorkflowDocumentUpdate(BaseModel):
    statut: Optional[str]

class WorkflowDocumentRead(WorkflowDocumentBase):
    id: int
    date_liaison: datetime

class WorkflowDocumentSearch(BaseModel):
    document_id: Optional[int]
    workflow_id: Optional[int]
    statut: Optional[str]

class WorkflowDocumentSearchResults(BaseModel):
    results: List[WorkflowDocumentRead]