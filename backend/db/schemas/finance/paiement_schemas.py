from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PaiementBase(BaseModel):
    facture_id: int
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    montant: float
    mode_paiement: str
    reference: Optional[str]
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class PaiementCreate(PaiementBase):
    pass

class PaiementUpdate(BaseModel):
    montant: Optional[float]
    mode_paiement: Optional[str]
    reference: Optional[str]
    commentaire: Optional[str]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    facture_id: Optional[int]

class PaiementRead(PaiementBase):
    id: int
    date_paiement: datetime

class PaiementSearch(BaseModel):
    facture_id: Optional[int]
    entreprise_id: Optional[int]
    mode_paiement: Optional[str]

class PaiementSearchResults(BaseModel):
    results: List[PaiementRead]