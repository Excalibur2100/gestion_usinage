from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class FactureBase(BaseModel):
    numero_facture: str
    client_id: int
    commande_id: Optional[int]
    date_emission: datetime
    date_echeance: Optional[datetime]
    montant_total: float
    statut: str = "En attente"
    observations: Optional[str]

class FactureCreate(FactureBase):
    pass

class FactureRead(FactureBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        

