from pydantic import BaseModel
from typing import Optional, List

class ConfigPaiementBase(BaseModel):
    libelle: str
    description: Optional[str]
    delai_jours: int
    actif: Optional[bool] = True

    class Config:
        from_attributes = True

class ConfigPaiementCreate(ConfigPaiementBase):
    pass

class ConfigPaiementUpdate(BaseModel):
    libelle: Optional[str]
    description: Optional[str]
    delai_jours: Optional[int]
    actif: Optional[bool]

class ConfigPaiementRead(ConfigPaiementBase):
    id: int

class ConfigPaiementSearch(BaseModel):
    libelle: Optional[str]
    actif: Optional[bool]

class ConfigPaiementSearchResults(BaseModel):
    results: List[ConfigPaiementRead]