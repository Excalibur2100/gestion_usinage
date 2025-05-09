from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class OutilBase(BaseModel):
    """
    Schéma de base pour un outil.
    """
    nom: str = Field(..., description="Nom de l'outil")
    type_outil: str = Field(..., description="Type de l'outil (ex: fraise, foret)")
    description: Optional[str] = Field(None, description="Description de l'outil")

class OutilCreate(OutilBase):
    """
    Schéma pour la création d'un outil.
    """
    pass

class OutilRead(OutilBase):
    """
    Schéma pour la lecture d'un outil.
    """
    id: int = Field(..., description="ID unique de l'outil")

    model_config = ConfigDict(from_attributes=True)

class OutilUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un outil.
    """
    nom: Optional[str] = Field(None, description="Nom de l'outil")
    type_outil: Optional[str] = Field(None, description="Type de l'outil (ex: fraise, foret)")
    description: Optional[str] = Field(None, description="Description de l'outil")

    model_config = ConfigDict(from_attributes=True)