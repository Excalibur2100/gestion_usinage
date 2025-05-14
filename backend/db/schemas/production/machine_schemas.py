from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

class MachineBase(BaseModel):
    nom: str = Field(..., description="Nom ou code de la machine")
    type_machine: str = Field(..., description="Type de machine : CNC, tour, fraiseuse...")
    etat: Optional[str] = Field("opérationnelle", description="État de la machine")
    date_installation: Optional[date] = Field(None, description="Date d'installation")
    emplacement: Optional[str] = Field(None, description="Emplacement physique")
    statut: Optional[str] = Field("active", description="Statut : active, arrêt, maintenance")
    description: Optional[str] = Field(None, description="Détails techniques ou remarques")

class MachineCreate(MachineBase):
    pass

class MachineUpdate(BaseModel):
    nom: Optional[str] = None
    type_machine: Optional[str] = None
    etat: Optional[str] = None
    date_installation: Optional[date] = None
    emplacement: Optional[str] = None
    statut: Optional[str] = None
    description: Optional[str] = None

class MachineRead(MachineBase):
    id: int = Field(..., description="ID unique de la machine")

    class Config:
        model_config = ConfigDict(from_attributes=True)
