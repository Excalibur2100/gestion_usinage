from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FactureFournisseurBase(BaseModel):
    numero_facture: str
    date_facture: Optional[datetime] = None
    date_echeance: Optional[datetime]
    montant_ht: float
    montant_tva: float
    montant_ttc: float
    statut: Optional[str] = "non payé"
    commentaire: Optional[str]
    commande_id: Optional[int]
    fournisseur_id: int

    class Config:
        from_attributes = True

class FactureFournisseurCreate(FactureFournisseurBase):
    pass

class FactureFournisseurUpdate(BaseModel):
    numero_facture: Optional[str]
    date_facture: Optional[datetime]
    date_echeance: Optional[datetime]
    montant_ht: Optional[float]
    montant_tva: Optional[float]
    montant_ttc: Optional[float]
    statut: Optional[str]
    commentaire: Optional[str]
    commande_id: Optional[int]
    fournisseur_id: Optional[int]

class FactureFournisseurRead(FactureFournisseurBase):
    id: int

class FactureFournisseurSearch(BaseModel):
    numero_facture: Optional[str]
    fournisseur_id: Optional[int]
    statut: Optional[str]

class FactureFournisseurSearchResults(BaseModel):
    results: List[FactureFournisseurRead]
