from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class PointageBase(BaseModel):
    """
    Schéma de base pour un pointage.
    """
    utilisateur_id: int = Field(..., description="ID de l'utilisateur associé")
    machine_id: Optional[int] = Field(None, description="ID de la machine associée")
    gamme_id: Optional[int] = Field(None, description="ID de la gamme de production associée")
    date_pointage: datetime = Field(..., description="Date du pointage")
    heure_debut: datetime = Field(..., description="Heure de début")
    heure_fin: Optional[datetime] = Field(None, description="Heure de fin")
    duree_effective: Optional[float] = Field(None, description="Durée effective (en heures)")
    remarques: Optional[str] = Field(None, description="Remarques sur le pointage")

class PointageCreate(PointageBase):
    """
    Schéma pour la création d'un pointage.
    """
    pass

class PointageRead(PointageBase):
    """
    Schéma pour la lecture d'un pointage.
    """
    id: int = Field(..., description="ID unique du pointage")

    model_config = ConfigDict(from_attributes=True)

class PointageUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un pointage.
    """
    utilisateur_id: Optional[int] = Field(None, description="ID de l'utilisateur associé")
    machine_id: Optional[int] = Field(None, description="ID de la machine associée")
    gamme_id: Optional[int] = Field(None, description="ID de la gamme de production associée")
    date_pointage: Optional[datetime] = Field(None, description="Date du pointage")
    heure_debut: Optional[datetime] = Field(None, description="Heure de début")
    heure_fin: Optional[datetime] = Field(None, description="Heure de fin")
    duree_effective: Optional[float] = Field(None, description="Durée effective (en heures)")
    remarques: Optional[str] = Field(None, description="Remarques sur le pointage")

    model_config = ConfigDict(from_attributes=True)