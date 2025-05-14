from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

class FormationBase(BaseModel):
    intitule: str = Field(..., description="Intitulé de la formation")
    organisme: str = Field(..., description="Organisme de formation")
    date_debut: date = Field(..., description="Date de début de la formation")
    date_fin: date = Field(..., description="Date de fin de la formation")
    statut: Optional[str] = Field("prévue", description="Statut : prévue, en cours, terminée")

class FormationCreate(FormationBase):
    pass

class FormationUpdate(BaseModel):
    intitule: Optional[str] = None
    organisme: Optional[str] = None
    date_debut: Optional[date] = None
    date_fin: Optional[date] = None
    statut: Optional[str] = None

class FormationRead(FormationBase):
    id: int = Field(..., description="ID unique de la formation")

    class Config:
        model_config = ConfigDict(from_attributes=True)
