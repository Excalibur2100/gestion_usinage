from pydantic import BaseModel
from typing import Optional, List

class ConfigMetierBase(BaseModel):
    nom: str
    description: Optional[str]
    actif: Optional[bool] = True

    class Config:
        from_attributes = True

class ConfigMetierCreate(ConfigMetierBase):
    pass

class ConfigMetierUpdate(BaseModel):
    nom: Optional[str]
    description: Optional[str]
    actif: Optional[bool]

class ConfigMetierRead(ConfigMetierBase):
    id: int

class ConfigMetierSearch(BaseModel):
    nom: Optional[str]
    actif: Optional[bool]

class ConfigMetierSearchResults(BaseModel):
    results: List[ConfigMetierRead]