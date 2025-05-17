from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReceptionBase(BaseModel):
    quantite_recue: float
    commentaire: Optional[str]
    statut: Optional[str] = "en attente"
    ligne_commande_id: int
    commande_id: Optional[int]
    utilisateur_id: Optional[int]

    class Config:
        from_attributes = True

class ReceptionCreate(ReceptionBase):
    pass

class ReceptionUpdate(BaseModel):
    quantite_recue: Optional[float]
    commentaire: Optional[str]
    statut: Optional[str]
    ligne_commande_id: Optional[int]
    commande_id: Optional[int]
    utilisateur_id: Optional[int]

class ReceptionRead(ReceptionBase):
    id: int
    date_reception: datetime

class ReceptionSearch(BaseModel):
    statut: Optional[str]
    ligne_commande_id: Optional[int]
    utilisateur_id: Optional[int]

class ReceptionSearchResults(BaseModel):
    results: List[ReceptionRead]
