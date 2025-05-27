from pydantic import BaseModel
from typing import Optional, List

class ConfigLangueBase(BaseModel):
    code: str
    libelle: str
    active: Optional[bool] = True

    class Config:
        from_attributes = True

class ConfigLangueCreate(ConfigLangueBase):
    pass

class ConfigLangueUpdate(BaseModel):
    code: Optional[str]
    libelle: Optional[str]
    active: Optional[bool]

class ConfigLangueRead(ConfigLangueBase):
    id: int

class ConfigLangueSearch(BaseModel):
    code: Optional[str]
    libelle: Optional[str]
    active: Optional[bool]

class ConfigLangueSearchResults(BaseModel):
    results: List[ConfigLangueRead]