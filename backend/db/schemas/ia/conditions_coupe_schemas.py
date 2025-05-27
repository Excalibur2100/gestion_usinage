from pydantic import BaseModel
from typing import Optional, List

class ConditionsCoupeBase(BaseModel):
    piece_id: Optional[int]
    outil_id: Optional[int]
    materiau_id: Optional[int]
    operation: str
    vitesse_coupe: float
    avance: float
    profondeur_passage: float
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class ConditionsCoupeCreate(ConditionsCoupeBase):
    pass

class ConditionsCoupeUpdate(BaseModel):
    operation: Optional[str]
    vitesse_coupe: Optional[float]
    avance: Optional[float]
    profondeur_passage: Optional[float]
    commentaire: Optional[str]

class ConditionsCoupeRead(ConditionsCoupeBase):
    id: int

class ConditionsCoupeSearch(BaseModel):
    piece_id: Optional[int]
    outil_id: Optional[int]
    materiau_id: Optional[int]
    operation: Optional[str]

class ConditionsCoupeSearchResults(BaseModel):
    results: List[ConditionsCoupeRead]