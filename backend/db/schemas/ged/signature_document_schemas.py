from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SignatureDocumentBase(BaseModel):
    document_id: int
    utilisateur_id: int
    statut: Optional[str] = "en attente"
    commentaire: Optional[str]
    signature_validee: Optional[bool] = False

    class Config:
        from_attributes = True

class SignatureDocumentCreate(SignatureDocumentBase):
    pass

class SignatureDocumentUpdate(BaseModel):
    statut: Optional[str]
    commentaire: Optional[str]
    signature_validee: Optional[bool]

class SignatureDocumentRead(SignatureDocumentBase):
    id: int
    date_signature: datetime

class SignatureDocumentSearch(BaseModel):
    document_id: Optional[int]
    utilisateur_id: Optional[int]
    statut: Optional[str]

class SignatureDocumentSearchResults(BaseModel):
    results: List[SignatureDocumentRead]