from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AideCalculTVABase(BaseModel):
    montant_ht: float
    taux_tva: float
    montant_tva: float
    montant_ttc: float
    calcul_type: str = "HT→TTC"

    class Config:
        from_attributes = True

class AideCalculTVACreate(AideCalculTVABase):
    pass

class AideCalculTVAUpdate(BaseModel):
    montant_ht: Optional[float]
    taux_tva: Optional[float]
    montant_tva: Optional[float]
    montant_ttc: Optional[float]
    calcul_type: Optional[str]

class AideCalculTVARead(AideCalculTVABase):
    id: int
    date_calcul: datetime

class AideCalculTVASearch(BaseModel):
    calcul_type: Optional[str]

class AideCalculTVASearchResults(BaseModel):
    results: List[AideCalculTVARead]