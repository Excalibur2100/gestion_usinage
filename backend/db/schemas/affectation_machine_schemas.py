from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AffectationMachineBase(BaseModel):
    machine_id: int
    utilisateur_id: int
    date_affectation: datetime
    tache: Optional[str] = None
    statut: str

class AffectationMachineCreate(AffectationMachineBase):
    pass

class AffectationMachineUpdate(BaseModel):
    machine_id: Optional[int] = None
    utilisateur_id: Optional[int] = None
    date_affectation: Optional[datetime] = None
    tache: Optional[str] = None
    statut: Optional[str] = None

class AffectationMachineResponse(AffectationMachineBase):
    id: int

    class Config:
        orm_mode = True