from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class MachineBase(BaseModel):
    """
    Schéma de base pour une machine.
    """
    nom: str = Field(..., description="Nom unique de la machine")
    type_machine: str = Field(..., description="Type de la machine (ex: CNC, imprimante 3D)")
    vitesse_max: Optional[float] = Field(None, description="Vitesse maximale de la machine")
    puissance: Optional[float] = Field(None, description="Puissance de la machine (en kW)")
    nb_axes: Optional[int] = Field(None, description="Nombre d'axes de la machine")

class MachineCreate(MachineBase):
    """
    Schéma pour la création d'une machine.
    """
    pass

class MachineRead(MachineBase):
    """
    Schéma pour la lecture d'une machine.
    """
    id: int = Field(..., description="ID unique de la machine")
    created_at: datetime = Field(..., description="Date de création de la machine")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière mise à jour de la machine")

    model_config = ConfigDict(from_attributes=True)

class MachineUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'une machine.
    """
    nom: Optional[str] = Field(None, description="Nom unique de la machine")
    type_machine: Optional[str] = Field(None, description="Type de la machine (ex: CNC, imprimante 3D)")
    vitesse_max: Optional[float] = Field(None, description="Vitesse maximale de la machine")
    puissance: Optional[float] = Field(None, description="Puissance de la machine (en kW)")
    nb_axes: Optional[int] = Field(None, description="Nombre d'axes de la machine")

    model_config = ConfigDict(from_attributes=True)