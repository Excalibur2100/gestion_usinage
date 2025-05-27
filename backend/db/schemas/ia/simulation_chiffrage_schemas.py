from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SimulationChiffrageBase(BaseModel):
    piece_id: Optional[int]
    utilisateur_id: Optional[int]
    scenario: str
    duree_estimee: float
    cout_estime: float
    commentaire: Optional[str]
    marge_simulee: Optional[float] = 0.0
    source: Optional[str] = "simulation-engine"

    class Config:
        from_attributes = True

class SimulationChiffrageCreate(SimulationChiffrageBase):
    pass

class SimulationChiffrageUpdate(BaseModel):
    scenario: Optional[str]
    duree_estimee: Optional[float]
    cout_estime: Optional[float]
    commentaire: Optional[str]
    marge_simulee: Optional[float]
    source: Optional[str]

class SimulationChiffrageRead(SimulationChiffrageBase):
    id: int
    date_simulation: datetime

class SimulationChiffrageSearch(BaseModel):
    piece_id: Optional[int]
    utilisateur_id: Optional[int]
    scenario: Optional[str]

class SimulationChiffrageSearchResults(BaseModel):
    results: List[SimulationChiffrageRead]