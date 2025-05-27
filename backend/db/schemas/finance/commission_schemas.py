from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CommissionBase(BaseModel):
    utilisateur_id: int
    devis_id: Optional[int]
    entreprise_id: Optional[int]
    montant_base: float
    taux_commission: float
    montant_commission: float
    statut: Optional[str] = "à valider"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class CommissionCreate(CommissionBase):
    pass

class CommissionUpdate(BaseModel):
    utilisateur_id: Optional[int]
    devis_id: Optional[int]
    entreprise_id: Optional[int]
    montant_base: Optional[float]
    taux_commission: Optional[float]
    montant_commission: Optional[float]
    statut: Optional[str]
    commentaire: Optional[str]

class CommissionRead(CommissionBase):
    id: int
    date_creation: datetime

class CommissionSearch(BaseModel):
    utilisateur_id: Optional[int]
    entreprise_id: Optional[int]
    statut: Optional[str]

class CommissionSearchResults(BaseModel):
    results: List[CommissionRead]