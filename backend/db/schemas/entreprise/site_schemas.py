from pydantic import BaseModel
from typing import Optional, List

class SiteBase(BaseModel):
    entreprise_id: int
    nom: str
    adresse: Optional[str]
    code_postal: Optional[str]
    ville: Optional[str]
    pays: Optional[str] = "France"
    actif: Optional[bool] = True

    class Config:
        from_attributes = True

class SiteCreate(SiteBase):
    pass

class SiteUpdate(BaseModel):
    nom: Optional[str]
    adresse: Optional[str]
    code_postal: Optional[str]
    ville: Optional[str]
    pays: Optional[str]
    actif: Optional[bool]

class SiteRead(SiteBase):
    id: int

class SiteSearch(BaseModel):
    entreprise_id: Optional[int]
    nom: Optional[str]

class SiteSearchResults(BaseModel):
    results: List[SiteRead]