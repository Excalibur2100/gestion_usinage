from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ChargeMachineBase(BaseModel):
    machine_id: int = Field(..., description="ID de la machine associée")
    gamme_id: Optional[int] = Field(None, description="ID de la gamme de production associée")
    date_debut: datetime = Field(..., description="Date de début de la charge")
    date_fin: datetime = Field(..., description="Date de fin de la charge")
    statut: str = Field(..., description="Statut de la charge (planifié, en cours, terminé)")
    temperature: Optional[float] = Field(None, description="Température mesurée")
    vibration: Optional[float] = Field(None, description="Vibration mesurée")


class ChargeMachineCreate(ChargeMachineBase):
    pass


class ChargeMachineRead(ChargeMachineBase):
    id: int = Field(..., description="ID unique de la charge machine")

    class Config:
        ConfigDict(from_attributes=True)