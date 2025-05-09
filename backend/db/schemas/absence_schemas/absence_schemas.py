from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

class AbsenceBase(BaseModel):
    employe_id: int = Field(..., description="ID de l'employé concerné")
    date_debut: date = Field(..., description="Date de début de l'absence")
    date_fin: date = Field(..., description="Date de fin de l'absence")
    type_absence: str = Field(..., description="Type d'absence (RTT, congé, maladie...)")
    justificatif_url: Optional[str] = Field(None, description="Lien vers le justificatif")
    is_paid: Optional[bool] = Field(True, description="Absence rémunérée ou non")
    statut: Optional[str] = Field("en attente", description="Statut de l'absence (en attente, validée, refusée)")
    commentaire: Optional[str] = Field(None, description="Commentaire RH")

class AbsenceCreate(AbsenceBase):
    pass

class AbsenceUpdate(BaseModel):
    date_debut: Optional[date] = None
    date_fin: Optional[date] = None
    type_absence: Optional[str] = None
    justificatif_url: Optional[str] = None
    is_paid: Optional[bool] = None
    statut: Optional[str] = None
    commentaire: Optional[str] = None

class AbsenceRead(AbsenceBase):
    id: int = Field(..., description="ID unique de l'absence")

    class Config:
        model_config = ConfigDict(from_attributes=True)
