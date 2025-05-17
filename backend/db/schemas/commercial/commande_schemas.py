from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CommandeBase(BaseModel):
    code_commande: str
    statut: Optional[str] = "en cours"
    date_validation: Optional[datetime] = None
    commentaire: Optional[str]
    client_id: int
    devis_id: Optional[int]

    class Config:
        from_attributes = True

class CommandeCreate(CommandeBase):
    pass

class CommandeUpdate(BaseModel):
    code_commande: Optional[str]
    statut: Optional[str]
    date_validation: Optional[datetime]
    commentaire: Optional[str]
    client_id: Optional[int]
    devis_id: Optional[int]

class CommandeRead(CommandeBase):
    id: int
    date_creation: datetime

class CommandeSearch(BaseModel):
    code_commande: Optional[str]
    client_id: Optional[int]
    statut: Optional[str]

class CommandeSearchResults(BaseModel):
    results: List[CommandeRead]
