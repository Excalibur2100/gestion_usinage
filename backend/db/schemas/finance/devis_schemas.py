from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DevisBase(BaseModel):
    code_devis: str
    client_id: int
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    date_validite: Optional[datetime]
    statut: Optional[str] = "brouillon"
    commentaire: Optional[str]
    total_ht: float = 0.0
    total_ttc: float = 0.0

    class Config:
        from_attributes = True

class DevisCreate(DevisBase):
    pass

class DevisUpdate(BaseModel):
    code_devis: Optional[str]
    client_id: Optional[int]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    date_validite: Optional[datetime]
    statut: Optional[str]
    commentaire: Optional[str]
    total_ht: Optional[float]
    total_ttc: Optional[float]

class DevisRead(DevisBase):
    id: int
    date_creation: datetime

class DevisSearch(BaseModel):
    code_devis: Optional[str]
    client_id: Optional[int]
    entreprise_id: Optional[int]
    statut: Optional[str]

class DevisSearchResults(BaseModel):
    results: List[DevisRead]