from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class HistoriqueClientBase(BaseModel):
    client_id: int
    type_action: str
    description: Optional[str]
    auteur: Optional[str]

    class Config:
        from_attributes = True

class HistoriqueClientCreate(HistoriqueClientBase):
    pass

class HistoriqueClientUpdate(BaseModel):
    type_action: Optional[str]
    description: Optional[str]
    auteur: Optional[str]

class HistoriqueClientRead(HistoriqueClientBase):
    id: int
    date_action: datetime

class HistoriqueClientSearch(BaseModel):
    client_id: Optional[int]
    type_action: Optional[str]
    auteur: Optional[str]

class HistoriqueClientSearchResults(BaseModel):
    results: List[HistoriqueClientRead]