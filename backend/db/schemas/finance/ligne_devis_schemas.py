from pydantic import BaseModel
from typing import Optional, List

class LigneDevisBase(BaseModel):
    devis_id: int
    piece_id: Optional[int]
    designation: str
    description: Optional[str]
    quantite: int
    prix_unitaire: float
    remise: Optional[float] = 0.0

    class Config:
        from_attributes = True

class LigneDevisCreate(LigneDevisBase):
    pass

class LigneDevisUpdate(BaseModel):
    piece_id: Optional[int]
    designation: Optional[str]
    description: Optional[str]
    quantite: Optional[int]
    prix_unitaire: Optional[float]
    remise: Optional[float]

class LigneDevisRead(LigneDevisBase):
    id: int

class LigneDevisSearch(BaseModel):
    devis_id: Optional[int]
    piece_id: Optional[int]
    designation: Optional[str]

class LigneDevisSearchResults(BaseModel):
    results: List[LigneDevisRead]