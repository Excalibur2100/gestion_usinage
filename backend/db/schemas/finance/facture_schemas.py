from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FactureBase(BaseModel):
    code_facture: str
    commande_id: Optional[int]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    date_echeance: Optional[datetime]
    total_ht: float = 0.0
    total_ttc: float = 0.0
    statut: Optional[str] = "brouillon"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class FactureCreate(FactureBase):
    pass

class FactureUpdate(BaseModel):
    code_facture: Optional[str]
    commande_id: Optional[int]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    date_echeance: Optional[datetime]
    total_ht: Optional[float]
    total_ttc: Optional[float]
    statut: Optional[str]
    commentaire: Optional[str]

class FactureRead(FactureBase):
    id: int
    date_emission: datetime

class FactureSearch(BaseModel):
    code_facture: Optional[str]
    commande_id: Optional[int]
    entreprise_id: Optional[int]
    statut: Optional[str]

class FactureSearchResults(BaseModel):
    results: List[FactureRead]