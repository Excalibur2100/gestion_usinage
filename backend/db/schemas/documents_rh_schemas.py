from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentRHBase(BaseModel):
    nom: str
    type_document: str
    chemin_fichier: str
    date_creation: Optional[datetime] = None
    description: Optional[str] = None
    actif: Optional[str] = "actif"

class DocumentRHCreate(DocumentRHBase):
    pass

class DocumentRHUpdate(BaseModel):
    nom: Optional[str] = None
    type_document: Optional[str] = None
    chemin_fichier: Optional[str] = None
    date_creation: Optional[datetime] = None
    description: Optional[str] = None
    actif: Optional[str] = None

class DocumentRHResponse(DocumentRHBase):
    id: int

    class Config:
        orm_mode = True