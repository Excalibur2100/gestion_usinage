from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class JournalComptableBase(BaseModel):
    entreprise_id: int
    utilisateur_id: Optional[int]
    type_ecriture: str
    reference: Optional[str]
    libelle: Optional[str]
    montant_debit: float
    montant_credit: float
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class JournalComptableCreate(JournalComptableBase):
    pass

class JournalComptableUpdate(BaseModel):
    type_ecriture: Optional[str]
    reference: Optional[str]
    libelle: Optional[str]
    montant_debit: Optional[float]
    montant_credit: Optional[float]
    commentaire: Optional[str]
    entreprise_id: Optional[int]
    utilisateur_id: Optional[int]

class JournalComptableRead(JournalComptableBase):
    id: int
    date_ecriture: datetime

class JournalComptableSearch(BaseModel):
    type_ecriture: Optional[str]
    entreprise_id: Optional[int]

class JournalComptableSearchResults(BaseModel):
    results: List[JournalComptableRead]