from pydantic import BaseModel
from typing import Optional, List

class CommandePieceBase(BaseModel):
    commande_id: int
    piece_id: Optional[int]
    designation: str
    quantite: int
    prix_unitaire: float

    class Config:
        from_attributes = True

class CommandePieceCreate(CommandePieceBase):
    pass

class CommandePieceUpdate(BaseModel):
    commande_id: Optional[int]
    piece_id: Optional[int]
    designation: Optional[str]
    quantite: Optional[int]
    prix_unitaire: Optional[float]

class CommandePieceRead(CommandePieceBase):
    id: int

class CommandePieceSearch(BaseModel):
    commande_id: Optional[int]
    piece_id: Optional[int]
    designation: Optional[str]

class CommandePieceSearchResults(BaseModel):
    results: List[CommandePieceRead]
