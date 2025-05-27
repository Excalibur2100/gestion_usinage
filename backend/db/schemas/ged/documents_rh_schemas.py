from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DocumentRHBase(BaseModel):
    employe_id: int
    utilisateur_id: Optional[int]
    entreprise_id: Optional[int]
    type_document: str
    titre: str
    description: Optional[str]
    chemin_fichier: str

    class Config:
        from_attributes = True

class DocumentRHCreate(DocumentRHBase):
    pass

class DocumentRHUpdate(BaseModel):
    type_document: Optional[str]
    titre: Optional[str]
    description: Optional[str]
    chemin_fichier: Optional[str]

class DocumentRHRead(DocumentRHBase):
    id: int
    date_creation: datetime

class DocumentRHSearch(BaseModel):
    employe_id: Optional[int]
    type_document: Optional[str]

class DocumentRHSearchResults(BaseModel):
    results: List[DocumentRHRead]