from pydantic import BaseModel
from typing import Optional, List

class ConditionPaiementBase(BaseModel):
    libelle: str
    description: Optional[str]

    class Config:
        from_attributes = True

class ConditionPaiementCreate(ConditionPaiementBase):
    pass

class ConditionPaiementUpdate(BaseModel):
    libelle: Optional[str]
    description: Optional[str]

class ConditionPaiementRead(ConditionPaiementBase):
    id: int

class ConditionPaiementSearch(BaseModel):
    libelle: Optional[str]

class ConditionPaiementSearchResults(BaseModel):
    results: List[ConditionPaiementRead]
