from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RemiseClientBase(BaseModel):
    client_id: int
    piece_id: Optional[int]
    pourcentage: float
    type_remise: Optional[str] = "globale"
    description: Optional[str]
    date_debut: Optional[datetime]
    date_fin: Optional[datetime]

    class Config:
        from_attributes = True

class RemiseClientCreate(RemiseClientBase):
    pass

class RemiseClientUpdate(BaseModel):
    client_id: Optional[int]
    piece_id: Optional[int]
    pourcentage: Optional[float]
    type_remise: Optional[str]
    description: Optional[str]
    date_debut: Optional[datetime]
    date_fin: Optional[datetime]

class RemiseClientRead(RemiseClientBase):
    id: int
    date_creation: datetime

class RemiseClientSearch(BaseModel):
    client_id: Optional[int]
    piece_id: Optional[int]
    type_remise: Optional[str]

class RemiseClientSearchResults(BaseModel):
    results: List[RemiseClientRead]
