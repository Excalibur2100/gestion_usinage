from pydantic import BaseModel
from typing import Optional, List

class LigneFactureBase(BaseModel):
    facture_id: int
    piece_id: Optional[int]
    designation: str
    description: Optional[str]
    quantite: int
    prix_unitaire: float
    remise: Optional[float] = 0.0

    class Config:
        from_attributes = True

class LigneFactureCreate(LigneFactureBase):
    pass

class LigneFactureUpdate(BaseModel):
    piece_id: Optional[int]
    designation: Optional[str]
    description: Optional[str]
    quantite: Optional[int]
    prix_unitaire: Optional[float]
    remise: Optional[float]

class LigneFactureRead(LigneFactureBase):
    id: int

class LigneFactureSearch(BaseModel):
    facture_id: Optional[int]
    piece_id: Optional[int]
    designation: Optional[str]

class LigneFactureSearchResults(BaseModel):
    results: List[LigneFactureRead]