from pydantic import BaseModel
from typing import Optional, List

class ProfilAccesBase(BaseModel):
    entreprise_id: int
    nom: str
    description: Optional[str]

    class Config:
        from_attributes = True

class ProfilAccesCreate(ProfilAccesBase):
    pass

class ProfilAccesUpdate(BaseModel):
    nom: Optional[str]
    description: Optional[str]

class ProfilAccesRead(ProfilAccesBase):
    id: int

class ProfilAccesSearch(BaseModel):
    entreprise_id: Optional[int]
    nom: Optional[str]

class ProfilAccesSearchResults(BaseModel):
    results: List[ProfilAccesRead]