from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ControlePieceBase(BaseModel):
    piece_id: int
    instrument_id: Optional[int] = None
    resultat: str
    date_controle: datetime
    remarque: Optional[str] = None

class ControlePieceCreate(ControlePieceBase):
    pass

class ControlePieceUpdate(BaseModel):
    piece_id: Optional[int] = None
    instrument_id: Optional[int] = None
    resultat: Optional[str] = None
    date_controle: Optional[datetime] = None
    remarque: Optional[str] = None

class ControlePieceResponse(ControlePieceBase):
    id: int

    class Config:
        orm_mode = True