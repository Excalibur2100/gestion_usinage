from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AvoirFournisseurBase(BaseModel):
    numero_avoir: str
    date_avoir: Optional[datetime] = None
    montant: float
    motif: Optional[str]
    statut: Optional[str] = "non imputé"
    facture_id: Optional[int]
    fournisseur_id: int

    class Config:
        from_attributes = True

class AvoirFournisseurCreate(AvoirFournisseurBase):
    pass

class AvoirFournisseurUpdate(BaseModel):
    numero_avoir: Optional[str]
    date_avoir: Optional[datetime]
    montant: Optional[float]
    motif: Optional[str]
    statut: Optional[str]
    facture_id: Optional[int]
    fournisseur_id: Optional[int]

class AvoirFournisseurRead(AvoirFournisseurBase):
    id: int

class AvoirFournisseurSearch(BaseModel):
    numero_avoir: Optional[str]
    fournisseur_id: Optional[int]
    statut: Optional[str]

class AvoirFournisseurSearchResults(BaseModel):
    results: List[AvoirFournisseurRead]
