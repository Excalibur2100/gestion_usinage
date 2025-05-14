from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field

class PieceBase(BaseModel):
    """
    Schéma de base pour une pièce.
    """
    nom: str = Field(..., description="Nom de la pièce")
    numero_plan: str = Field(..., description="Numéro de plan de la pièce")
    description: Optional[str] = Field(None, description="Description de la pièce")

class PieceCreate(PieceBase):
    """
    Schéma pour la création d'une pièce.
    """
    pass

class PieceRead(PieceBase):
    """
    Schéma pour la lecture d'une pièce.
    """
    id: int = Field(..., description="ID unique de la pièce")

    model_config = ConfigDict(from_attributes=True)

class PieceUsinage(BaseModel):
    """
    Schéma pour les détails d'usinage d'une pièce.
    """
    longueur: float = Field(..., description="Longueur de la pièce")
    largeur: float = Field(..., description="Largeur de la pièce")
    hauteur: float = Field(..., description="Hauteur de la pièce")
    materiau: str = Field(..., description="Matériau de la pièce")
    operations: List[str] = Field(..., description="Liste des opérations nécessaires")
    outils: List[str] = Field(..., description="Liste des outils nécessaires")
    outils_disponibles: List[str] = Field(..., description="Outils disponibles")
    machines_disponibles: List[str] = Field(..., description="Machines disponibles")

    model_config = ConfigDict(from_attributes=True)