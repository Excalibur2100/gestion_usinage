from pydantic import BaseModel
from typing import Optional, List

class ParametrageInterneBase(BaseModel):
    entreprise_id: int
    cle: str
    valeur: str
    description: Optional[str]
    actif: Optional[bool] = True

    class Config:
        from_attributes = True

class ParametrageInterneCreate(ParametrageInterneBase):
    pass

class ParametrageInterneUpdate(BaseModel):
    cle: Optional[str]
    valeur: Optional[str]
    description: Optional[str]
    actif: Optional[bool]

class ParametrageInterneRead(ParametrageInterneBase):
    id: int

class ParametrageInterneSearch(BaseModel):
    entreprise_id: Optional[int]
    cle: Optional[str]
    actif: Optional[bool]

class ParametrageInterneSearchResults(BaseModel):
    results: List[ParametrageInterneRead]