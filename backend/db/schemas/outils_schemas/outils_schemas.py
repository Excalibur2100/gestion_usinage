from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

class OutilBase(BaseModel):
    nom: str = Field(..., description="Nom de l'outil")
    type: str = Field(..., description="Type d'outil (foret, fraise, clé...)")
    etat: Optional[str] = Field("bon", description="État : bon, usé, cassé")
    emplacement: Optional[str] = Field(None, description="Emplacement de l'outil dans l’atelier")
    date_maintenance: Optional[date] = Field(None, description="Date de dernière maintenance")
    statut: Optional[str] = Field("actif", description="Statut : actif, inactif, en maintenance")
    description: Optional[str] = Field(None, description="Description complémentaire")

class OutilCreate(OutilBase):
    pass

class OutilUpdate(BaseModel):
    nom: Optional[str] = None
    type: Optional[str] = None
    etat: Optional[str] = None
    emplacement: Optional[str] = None
    date_maintenance: Optional[date] = None
    statut: Optional[str] = None
    description: Optional[str] = None

class OutilRead(OutilBase):
    id: int = Field(..., description="ID unique de l'outil")

    class Config:
        model_config = ConfigDict(from_attributes=True)
