from pydantic import BaseModel, ConfigDict, Field

class GestionFiltrageBase(BaseModel):
    """
    Schéma de base pour un filtrage.
    """
    filtre: str = Field(..., description="Nom du filtre")
    valeur: str = Field(..., description="Valeur associée au filtre")

class GestionFiltrageCreate(GestionFiltrageBase):
    """
    Schéma pour la création d'un filtrage.
    """
    pass

class GestionFiltrageRead(GestionFiltrageBase):
    """
    Schéma pour la lecture d'un filtrage.
    """
    id: int = Field(..., description="ID unique du filtrage")

    model_config = ConfigDict(from_attributes=True)