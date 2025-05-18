from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ActionCommercialeBase(BaseModel):
    type_action: str
    date_action: Optional[datetime] = None
    resultat: Optional[str]
    commentaire: Optional[str]
    client_id: Optional[int]
    utilisateur_id: Optional[int]

    class Config:
        from_attributes = True

class ActionCommercialeCreate(ActionCommercialeBase):
    pass

class ActionCommercialeUpdate(BaseModel):
    type_action: Optional[str]
    date_action: Optional[datetime]
    resultat: Optional[str]
    commentaire: Optional[str]
    client_id: Optional[int]
    utilisateur_id: Optional[int]

class ActionCommercialeRead(ActionCommercialeBase):
    id: int
    date_action: Optional[datetime] = None

class ActionCommercialeSearch(BaseModel):
    type_action: Optional[str]
    client_id: Optional[int]
    utilisateur_id: Optional[int]

class ActionCommercialeSearchResults(BaseModel):
    results: List[ActionCommercialeRead]
