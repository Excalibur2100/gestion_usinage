from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SuiviReglementFournisseurBase(BaseModel):
    facture_fournisseur_id: int
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    montant: float
    mode_paiement: str
    statut: Optional[str] = "prévu"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class SuiviReglementFournisseurCreate(SuiviReglementFournisseurBase):
    pass

class SuiviReglementFournisseurUpdate(BaseModel):
    facture_fournisseur_id: Optional[int]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]
    montant: Optional[float]
    mode_paiement: Optional[str]
    statut: Optional[str]
    commentaire: Optional[str]

class SuiviReglementFournisseurRead(SuiviReglementFournisseurBase):
    id: int
    date_reglement: datetime

class SuiviReglementFournisseurSearch(BaseModel):
    facture_fournisseur_id: Optional[int]
    entreprise_id: Optional[int]
    statut: Optional[str]

class SuiviReglementFournisseurSearchResults(BaseModel):
    results: List[SuiviReglementFournisseurRead]