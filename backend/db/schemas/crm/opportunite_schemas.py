from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OpportuniteBase(BaseModel):
    client_id: int
    titre: str
    description: Optional[str]
    montant_potentiel: Optional[float]
    probabilite: Optional[float] = 0.0
    statut: Optional[str] = "ouverte"

    class Config:
        from_attributes = True

class OpportuniteCreate(OpportuniteBase):
    pass

class OpportuniteUpdate(BaseModel):
    titre: Optional[str]
    description: Optional[str]
    montant_potentiel: Optional[float]
    probabilite: Optional[float]
    statut: Optional[str]

class OpportuniteRead(OpportuniteBase):
    id: int
    date_creation: datetime

class OpportuniteSearch(BaseModel):
    client_id: Optional[int]
    statut: Optional[str]
    titre: Optional[str]

class OpportuniteSearchResults(BaseModel):
    results: List[OpportuniteRead]