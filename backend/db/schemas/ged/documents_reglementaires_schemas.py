from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DocumentReglementaireBase(BaseModel):
    entreprise_id: int
    utilisateur_id: Optional[int]
    titre: str
    type_document: str
    chemin_fichier: str
    description: Optional[str]

    class Config:
        from_attributes = True

class DocumentReglementaireCreate(DocumentReglementaireBase):
    pass

class DocumentReglementaireUpdate(BaseModel):
    titre: Optional[str]
    type_document: Optional[str]
    chemin_fichier: Optional[str]
    description: Optional[str]

class DocumentReglementaireRead(DocumentReglementaireBase):
    id: int
    date_ajout: datetime

class DocumentReglementaireSearch(BaseModel):
    entreprise_id: Optional[int]
    type_document: Optional[str]

class DocumentReglementaireSearchResults(BaseModel):
    results: List[DocumentReglementaireRead]