from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentsQHSEBase(BaseModel):
    nom: str
    type_document: str
    chemin_fichier: str
    date_creation: Optional[datetime] = None
    description: Optional[str] = None
    actif: Optional[str] = "actif"

class DocumentsQHSECreate(DocumentsQHSEBase):
    pass

class DocumentsQHSEUpdate(BaseModel):
    nom: Optional[str] = None
    type_document: Optional[str] = None
    chemin_fichier: Optional[str] = None
    date_creation: Optional[datetime] = None
    description: Optional[str] = None
    actif: Optional[str] = None

class DocumentsQHSEResponse(DocumentsQHSEBase):
    id: int

    class Config:
        orm_mode = True