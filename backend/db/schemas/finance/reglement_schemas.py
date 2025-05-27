from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReglementBase(BaseModel):
    facture_id: Optional[int]
    entreprise_id: int
    utilisateur_id: Optional[int]
    montant: float
    mode: str
    statut: Optional[str] = "enregistré"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class ReglementCreate(ReglementBase):
    pass

class ReglementUpdate(BaseModel):
    facture_id: Optional[int]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    montant: Optional[float]
    mode: Optional[str]
    statut: Optional[str]
    commentaire: Optional[str]

class ReglementRead(ReglementBase):
    id: int
    date_reglement: datetime

class ReglementSearch(BaseModel):
    facture_id: Optional[int]
    entreprise_id: Optional[int]
    mode: Optional[str]
    statut: Optional[str]

class ReglementSearchResults(BaseModel):
    results: List[ReglementRead]