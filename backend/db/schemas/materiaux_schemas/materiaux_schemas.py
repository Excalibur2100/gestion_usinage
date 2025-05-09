from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class MateriauBase(BaseModel):
    """
    Schéma de base pour un matériau.
    """
    nom: str = Field(..., description="Nom du matériau")
    type: str = Field(..., description="Type de matériau (ex: Acier, Aluminium)")
    stock: float = Field(..., description="Quantité en stock (en kg)")
    durete: Optional[str] = Field(None, description="Dureté du matériau")
    certificat: Optional[str] = Field(None, description="Certificat du matériau")
    est_aeronautique: bool = Field(False, description="Indique si le matériau est certifié pour l'aéronautique")

class MateriauCreate(MateriauBase):
    """
    Schéma pour la création d'un matériau.
    """
    fournisseur_id: Optional[int] = Field(None, description="ID du fournisseur associé")
    emplacement_id: Optional[int] = Field(None, description="ID de l'emplacement associé")

class MateriauRead(MateriauBase):
    """
    Schéma pour la lecture d'un matériau.
    """
    id: int = Field(..., description="ID unique du matériau")

    model_config = ConfigDict(from_attributes=True)

class MateriauUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un matériau.
    """
    nom: Optional[str] = Field(None, description="Nom du matériau")
    type: Optional[str] = Field(None, description="Type de matériau (ex: Acier, Aluminium)")
    stock: Optional[float] = Field(None, description="Quantité en stock (en kg)")
    durete: Optional[str] = Field(None, description="Dureté du matériau")
    certificat: Optional[str] = Field(None, description="Certificat du matériau")
    est_aeronautique: Optional[bool] = Field(None, description="Indique si le matériau est certifié pour l'aéronautique")
    fournisseur_id: Optional[int] = Field(None, description="ID du fournisseur associé")
    emplacement_id: Optional[int] = Field(None, description="ID de l'emplacement associé")

    model_config = ConfigDict(from_attributes=True)