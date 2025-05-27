from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PortefeuilleClientBase(BaseModel):
    client_id: int
    utilisateur_id: int
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class PortefeuilleClientCreate(PortefeuilleClientBase):
    pass

class PortefeuilleClientUpdate(BaseModel):
    client_id: Optional[int]
    utilisateur_id: Optional[int]
    commentaire: Optional[str]

class PortefeuilleClientRead(PortefeuilleClientBase):
    id: int
    date_attribution: datetime

class PortefeuilleClientSearch(BaseModel):
    client_id: Optional[int]
    utilisateur_id: Optional[int]

class PortefeuilleClientSearchResults(BaseModel):
    results: List[PortefeuilleClientRead]
