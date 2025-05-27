from pydantic import BaseModel
from typing import Optional, List

class ConfigMargeBase(BaseModel):
    client_id: Optional[int]
    entreprise_id: int
    type_marge: Optional[str] = "globale"
    valeur: float
    unite: Optional[str] = "%"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class ConfigMargeCreate(ConfigMargeBase):
    pass

class ConfigMargeUpdate(BaseModel):
    client_id: Optional[int]
    entreprise_id: Optional[int]
    type_marge: Optional[str]
    valeur: Optional[float]
    unite: Optional[str]
    commentaire: Optional[str]

class ConfigMargeRead(ConfigMargeBase):
    id: int

class ConfigMargeSearch(BaseModel):
    client_id: Optional[int]
    entreprise_id: Optional[int]
    type_marge: Optional[str]

class ConfigMargeSearchResults(BaseModel):
    results: List[ConfigMargeRead]