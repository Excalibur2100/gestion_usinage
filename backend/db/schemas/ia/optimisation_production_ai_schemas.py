from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OptimisationAIBase(BaseModel):
    utilisateur_id: Optional[int]
    machine_id: Optional[int]
    piece_id: Optional[int]
    nom: str
    description: Optional[str]
    recommandation: Optional[str]
    gain_estime: Optional[str]
    source_ia: Optional[str] = "gpt-4"

    class Config:
        from_attributes = True

class OptimisationAICreate(OptimisationAIBase):
    pass

class OptimisationAIUpdate(BaseModel):
    description: Optional[str]
    recommandation: Optional[str]
    gain_estime: Optional[str]
    source_ia: Optional[str]
    nom: Optional[str]

class OptimisationAIRead(OptimisationAIBase):
    id: int
    date_optimisation: datetime

class OptimisationAISearch(BaseModel):
    utilisateur_id: Optional[int]
    machine_id: Optional[int]
    piece_id: Optional[int]
    nom: Optional[str]

class OptimisationAISearchResults(BaseModel):
    results: List[OptimisationAIRead]