from pydantic import BaseModel
from typing import Optional, List

class ConfigTVABase(BaseModel):
    nom: str
    taux: float
    pays: Optional[str]
    actif: Optional[bool] = True

    class Config:
        from_attributes = True

class ConfigTVACreate(ConfigTVABase):
    pass

class ConfigTVAUpdate(BaseModel):
    nom: Optional[str]
    taux: Optional[float]
    pays: Optional[str]
    actif: Optional[bool]

class ConfigTVARead(ConfigTVABase):
    id: int

class ConfigTVASearch(BaseModel):
    nom: Optional[str]
    pays: Optional[str]
    actif: Optional[bool]

class ConfigTVASearchResults(BaseModel):
    results: List[ConfigTVARead]