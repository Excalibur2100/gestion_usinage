from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DocumentQHSEBase(BaseModel):
    entreprise_id: int
    utilisateur_id: Optional[int]
    titre: str
    categorie: str
    chemin_fichier: str
    description: Optional[str]

    class Config:
        from_attributes = True

class DocumentQHSECreate(DocumentQHSEBase):
    pass

class DocumentQHSEUpdate(BaseModel):
    titre: Optional[str]
    categorie: Optional[str]
    chemin_fichier: Optional[str]
    description: Optional[str]

class DocumentQHSERead(DocumentQHSEBase):
    id: int
    date_ajout: datetime

class DocumentQHSESearch(BaseModel):
    entreprise_id: Optional[int]
    categorie: Optional[str]

class DocumentQHSESearchResults(BaseModel):
    results: List[DocumentQHSERead]