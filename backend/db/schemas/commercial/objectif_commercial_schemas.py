from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ObjectifCommercialBase(BaseModel):
    utilisateur_id: int
    periode: str
    objectif_chiffre: float
    objectif_marge: Optional[float]
    objectif_clients: Optional[int]

    class Config:
        from_attributes = True

class ObjectifCommercialCreate(ObjectifCommercialBase):
    pass

class ObjectifCommercialUpdate(BaseModel):
    utilisateur_id: Optional[int]
    periode: Optional[str]
    objectif_chiffre: Optional[float]
    objectif_marge: Optional[float]
    objectif_clients: Optional[int]

class ObjectifCommercialRead(ObjectifCommercialBase):
    id: int
    date_creation: datetime

class ObjectifCommercialSearch(BaseModel):
    utilisateur_id: Optional[int]
    periode: Optional[str]

class ObjectifCommercialSearchResults(BaseModel):
    results: List[ObjectifCommercialRead]
