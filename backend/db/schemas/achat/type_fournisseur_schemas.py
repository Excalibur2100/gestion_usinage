from pydantic import BaseModel
from typing import Optional, List

class TypeFournisseurBase(BaseModel):
    nom: str
    description: Optional[str]

    class Config:
        from_attributes = True

class TypeFournisseurCreate(TypeFournisseurBase):
    pass

class TypeFournisseurUpdate(BaseModel):
    nom: Optional[str]
    description: Optional[str]

class TypeFournisseurRead(TypeFournisseurBase):
    id: int

class TypeFournisseurSearch(BaseModel):
    nom: Optional[str]

class TypeFournisseurSearchResults(BaseModel):
    results: List[TypeFournisseurRead]
