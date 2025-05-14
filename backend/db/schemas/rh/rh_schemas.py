from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class RHBase(BaseModel):
    """
    Schéma de base pour un employé RH.
    """
    nom: str = Field(..., description="Nom de l'employé")
    prenom: str = Field(..., description="Prénom de l'employé")
    poste: str = Field(..., description="Poste occupé par l'employé")
    date_embauche: datetime = Field(..., description="Date d'embauche de l'employé")
    salaire: float = Field(..., description="Salaire de l'employé")

class RHCreate(RHBase):
    """
    Schéma pour la création d'un employé RH.
    """
    pass

class RHRead(RHBase):
    """
    Schéma pour la lecture d'un employé RH.
    """
    id: int = Field(..., description="ID unique de l'employé")

    model_config = ConfigDict(from_attributes=True)

class RHUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un employé RH.
    """
    nom: Optional[str] = Field(None, description="Nom de l'employé")
    prenom: Optional[str] = Field(None, description="Prénom de l'employé")
    poste: Optional[str] = Field(None, description="Poste occupé par l'employé")
    date_embauche: Optional[datetime] = Field(None, description="Date d'embauche de l'employé")
    salaire: Optional[float] = Field(None, description="Salaire de l'employé")

    model_config = ConfigDict(from_attributes=True)