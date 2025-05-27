from pydantic import BaseModel
from typing import Optional, List

class ConfigMonnaieBase(BaseModel):
    code: str
    libelle: str
    symbole: str
    taux_conversion: Optional[float] = 1.0
    active: Optional[bool] = True

    class Config:
        from_attributes = True

class ConfigMonnaieCreate(ConfigMonnaieBase):
    pass

class ConfigMonnaieUpdate(BaseModel):
    code: Optional[str]
    libelle: Optional[str]
    symbole: Optional[str]
    taux_conversion: Optional[float]
    active: Optional[bool]

class ConfigMonnaieRead(ConfigMonnaieBase):
    id: int

class ConfigMonnaieSearch(BaseModel):
    code: Optional[str]
    libelle: Optional[str]
    active: Optional[bool]

class ConfigMonnaieSearchResults(BaseModel):
    results: List[ConfigMonnaieRead]