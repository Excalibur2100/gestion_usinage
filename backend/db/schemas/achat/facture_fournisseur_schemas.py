from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FactureFournisseurBase(BaseModel):
    code_facture: str
    commande_fournisseur_id: Optional[int]
    fournisseur_id: int
    entreprise_id: Optional[int]
    date_facture: Optional[datetime]
    date_echeance: Optional[datetime]
    total_ht: float
    total_ttc: float
    statut: Optional[str] = "en attente"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class FactureFournisseurCreate(FactureFournisseurBase):
    pass

class FactureFournisseurUpdate(BaseModel):
    code_facture: Optional[str]
    commande_fournisseur_id: Optional[int]
    fournisseur_id: Optional[int]
    entreprise_id: Optional[int]
    date_facture: Optional[datetime]
    date_echeance: Optional[datetime]
    total_ht: Optional[float]
    total_ttc: Optional[float]
    statut: Optional[str]
    commentaire: Optional[str]

class FactureFournisseurRead(FactureFournisseurBase):
    id: int

class FactureFournisseurSearch(BaseModel):
    code_facture: Optional[str]
    fournisseur_id: Optional[int]
    entreprise_id: Optional[int]
    statut: Optional[str]

class FactureFournisseurSearchResults(BaseModel):
    results: List[FactureFournisseurRead]