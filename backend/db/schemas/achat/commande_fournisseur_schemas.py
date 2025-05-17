from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CommandeFournisseurBase(BaseModel):
    code_commande: str
    statut: Optional[str] = "brouillon"
    date_validation: Optional[datetime]
    commentaire: Optional[str]
    conditions_paiement: Optional[str]
    fournisseur_id: int
    entreprise_id: int

    class Config:
        from_attributes = True

class CommandeFournisseurCreate(CommandeFournisseurBase):
    pass

class CommandeFournisseurUpdate(BaseModel):
    code_commande: Optional[str]
    statut: Optional[str]
    date_validation: Optional[datetime]
    commentaire: Optional[str]
    conditions_paiement: Optional[str]
    fournisseur_id: Optional[int]
    entreprise_id: Optional[int]

class CommandeFournisseurRead(CommandeFournisseurBase):
    id: int
    date_creation: datetime

class CommandeFournisseurSearch(BaseModel):
    code_commande: Optional[str]
    statut: Optional[str]
    fournisseur_id: Optional[int]

class CommandeFournisseurSearchResults(BaseModel):
    results: List[CommandeFournisseurRead]
