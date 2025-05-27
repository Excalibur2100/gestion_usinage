from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class HistoriqueChiffrageBase(BaseModel):
    chiffrage_id: int
    utilisateur_id: Optional[int]
    version: str
    commentaire: Optional[str]
    duree_estimee: float
    cout_estime: float
    taux_marge: Optional[float] = 0.0

    class Config:
        from_attributes = True

class HistoriqueChiffrageCreate(HistoriqueChiffrageBase):
    pass

class HistoriqueChiffrageUpdate(BaseModel):
    version: Optional[str]
    commentaire: Optional[str]
    duree_estimee: Optional[float]
    cout_estime: Optional[float]
    taux_marge: Optional[float]

class HistoriqueChiffrageRead(HistoriqueChiffrageBase):
    id: int
    date_version: datetime

class HistoriqueChiffrageSearch(BaseModel):
    chiffrage_id: Optional[int]
    utilisateur_id: Optional[int]
    version: Optional[str]

class HistoriqueChiffrageSearchResults(BaseModel):
    results: List[HistoriqueChiffrageRead]