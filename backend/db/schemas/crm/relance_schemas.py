from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RelanceBase(BaseModel):
    client_id: int
    objet: str
    message: Optional[str]
    canal: str
    statut: Optional[str] = "en attente"

    class Config:
        from_attributes = True

class RelanceCreate(RelanceBase):
    pass

class RelanceUpdate(BaseModel):
    objet: Optional[str]
    message: Optional[str]
    canal: Optional[str]
    statut: Optional[str]

class RelanceRead(RelanceBase):
    id: int
    date_relance: datetime

class RelanceSearch(BaseModel):
    client_id: Optional[int]
    statut: Optional[str]
    canal: Optional[str]

class RelanceSearchResults(BaseModel):
    results: List[RelanceRead]