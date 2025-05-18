from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class HistoriquePrixClientBase(BaseModel):
    client_id: int
    piece_id: int
    prix_unitaire: float

    class Config:
        from_attributes = True

class HistoriquePrixClientCreate(HistoriquePrixClientBase):
    pass

class HistoriquePrixClientUpdate(BaseModel):
    client_id: Optional[int]
    piece_id: Optional[int]
    prix_unitaire: Optional[float]

class HistoriquePrixClientRead(HistoriquePrixClientBase):
    id: int
    date_enregistrement: datetime

class HistoriquePrixClientSearch(BaseModel):
    client_id: Optional[int]
    piece_id: Optional[int]

class HistoriquePrixClientSearchResults(BaseModel):
    results: List[HistoriquePrixClientRead]
