from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DocumentQualiteBase(BaseModel):
    entreprise_id: int
    utilisateur_id: Optional[int]
    titre: str
    type_document: str
    chemin_fichier: str
    description: Optional[str]

    class Config:
        from_attributes = True

class DocumentQualiteCreate(DocumentQualiteBase):
    pass

class DocumentQualiteUpdate(BaseModel):
    titre: Optional[str]
    type_document: Optional[str]
    chemin_fichier: Optional[str]
    description: Optional[str]

class DocumentQualiteRead(DocumentQualiteBase):
    id: int
    date_creation: datetime

class DocumentQualiteSearch(BaseModel):
    entreprise_id: Optional[int]
    type_document: Optional[str]

class DocumentQualiteSearchResults(BaseModel):
    results: List[DocumentQualiteRead]