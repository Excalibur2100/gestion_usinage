from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VersionDocumentBase(BaseModel):
    document_id: int
    utilisateur_id: Optional[int]
    numero_version: str
    commentaire: Optional[str]
    chemin_fichier: str

    class Config:
        from_attributes = True

class VersionDocumentCreate(VersionDocumentBase):
    pass

class VersionDocumentUpdate(BaseModel):
    numero_version: Optional[str]
    commentaire: Optional[str]
    chemin_fichier: Optional[str]

class VersionDocumentRead(VersionDocumentBase):
    id: int
    date_version: datetime

class VersionDocumentSearch(BaseModel):
    document_id: Optional[int]
    numero_version: Optional[str]

class VersionDocumentSearchResults(BaseModel):
    results: List[VersionDocumentRead]