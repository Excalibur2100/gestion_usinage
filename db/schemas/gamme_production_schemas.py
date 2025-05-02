from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class GammeProductionBase(BaseModel):
    piece_id: int
    ordre: int
    machine_id: Optional[int]
    outil_id: Optional[int]
    materiau_id: Optional[int]
    operation: str
    temps_prevu: Optional[float]
    temps_reel: Optional[float]
    statut: str = "En attente"

class GammeProductionCreate(GammeProductionBase):
    pass

class GammeProductionRead(GammeProductionBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        

