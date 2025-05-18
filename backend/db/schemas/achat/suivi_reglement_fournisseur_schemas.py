from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SuiviReglementFournisseurBase(BaseModel):
    montant_paye: float
    mode_paiement: Optional[str]
    statut: Optional[str] = "en attente"
    commentaire: Optional[str]
    facture_id: int
    utilisateur_id: Optional[int]

    class Config:
        from_attributes = True

class SuiviReglementFournisseurCreate(SuiviReglementFournisseurBase):
    pass

class SuiviReglementFournisseurUpdate(BaseModel):
    montant_paye: Optional[float]
    mode_paiement: Optional[str]
    statut: Optional[str]
    commentaire: Optional[str]
    facture_id: Optional[int]
    utilisateur_id: Optional[int]

class SuiviReglementFournisseurRead(SuiviReglementFournisseurBase):
    id: int
    date_reglement: datetime

class SuiviReglementFournisseurSearch(BaseModel):
    facture_id: Optional[int]
    statut: Optional[str]

class SuiviReglementFournisseurSearchResults(BaseModel):
    results: List[SuiviReglementFournisseurRead]
