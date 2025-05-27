from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FichierClientBase(BaseModel):
    client_id: int
    nom_fichier: str
    chemin: str
    type_fichier: Optional[str]
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class FichierClientCreate(FichierClientBase):
    pass

class FichierClientUpdate(BaseModel):
    nom_fichier: Optional[str]
    chemin: Optional[str]
    type_fichier: Optional[str]
    commentaire: Optional[str]

class FichierClientRead(FichierClientBase):
    id: int
    date_ajout: datetime

class FichierClientSearch(BaseModel):
    client_id: Optional[int]
    type_fichier: Optional[str]
    nom_fichier: Optional[str]

class FichierClientSearchResults(BaseModel):
    results: List[FichierClientRead]