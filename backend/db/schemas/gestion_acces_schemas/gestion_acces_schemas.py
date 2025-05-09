from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class GestionAccesBase(BaseModel):
    """
    Schéma de base pour la gestion des accès.
    """
    utilisateur_id: int = Field(..., description="ID de l'utilisateur associé")
    niveau_acces: str = Field(..., description="Niveau d'accès attribué à l'utilisateur")

class GestionAccesCreate(GestionAccesBase):
    """
    Schéma pour la création d'une gestion d'accès.
    """
    pass

class GestionAccesRead(GestionAccesBase):
    """
    Schéma pour la lecture d'une gestion d'accès.
    """
    id: int = Field(..., description="ID unique de la gestion d'accès")

    model_config = ConfigDict(from_attributes=True)

class GestionAccesUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'une gestion d'accès.
    """
    utilisateur_id: Optional[int] = Field(None, description="ID de l'utilisateur associé")
    niveau_acces: Optional[str] = Field(None, description="Niveau d'accès attribué à l'utilisateur")

    model_config = ConfigDict(from_attributes=True)