from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ChiffrageBase(BaseModel):
    piece_id: Optional[int]
    utilisateur_id: Optional[int]
    entreprise_id: Optional[int]
    description: Optional[str]
    duree_estimee: float
    cout_estime: float
    taux_marge: Optional[float] = 0.0
    origine: str = "manuel"
    nom_version: Optional[str]

    class Config:
        from_attributes = True

class ChiffrageCreate(ChiffrageBase):
    pass

class ChiffrageUpdate(BaseModel):
    description: Optional[str]
    duree_estimee: Optional[float]
    cout_estime: Optional[float]
    taux_marge: Optional[float]
    origine: Optional[str]
    nom_version: Optional[str]

class ChiffrageRead(ChiffrageBase):
    id: int
    date_chiffrage: datetime

class ChiffrageSearch(BaseModel):
    piece_id: Optional[int]
    utilisateur_id: Optional[int]
    entreprise_id: Optional[int]
    origine: Optional[str]

class ChiffrageSearchResults(BaseModel):
    results: List[ChiffrageRead]