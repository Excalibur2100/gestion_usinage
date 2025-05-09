from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class SurveillanceCameraBase(BaseModel):
    nom: str = Field(..., description="Nom de la caméra")
    resolution: str = Field(..., description="Résolution de la caméra")
    emplacement: Optional[str] = Field(None, description="Emplacement physique")
    etat: Optional[str] = Field("active", description="État de la caméra (active/inactive)")

class SurveillanceCameraCreate(SurveillanceCameraBase):
    pass

class SurveillanceCameraUpdate(BaseModel):
    nom: Optional[str] = None
    resolution: Optional[str] = None
    emplacement: Optional[str] = None
    etat: Optional[str] = None

class SurveillanceCameraRead(SurveillanceCameraBase):
    id: int = Field(..., description="Identifiant unique de la caméra")

    class Config:
        model_config = ConfigDict(from_attributes=True)
