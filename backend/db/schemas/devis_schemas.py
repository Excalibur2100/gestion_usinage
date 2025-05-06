from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class DevisBase(BaseModel):
    """
    Schéma de base pour un devis.
    """
    client_id: int = Field(..., description="ID du client associé au devis")
    date_devis: datetime = Field(..., description="Date de création du devis")
    montant_total: float = Field(..., description="Montant total du devis")
    statut: str = Field(..., description="Statut du devis (brouillon, validé, annulé)")
    scenarios: Optional[str] = Field(None, description="Scénarios associés au devis")

class DevisCreate(DevisBase):
    """
    Schéma pour la création d'un devis.
    """
    pass

class DevisRead(DevisBase):
    """
    Schéma pour la lecture d'un devis.
    """
    id: int = Field(..., description="ID unique du devis")

    model_config = ConfigDict(from_attributes=True)

class DevisUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un devis.
    """
    client_id: Optional[int] = Field(None, description="ID du client associé au devis")
    date_devis: Optional[datetime] = Field(None, description="Date de création du devis")
    montant_total: Optional[float] = Field(None, description="Montant total du devis")
    statut: Optional[str] = Field(None, description="Statut du devis (brouillon, validé, annulé)")
    scenarios: Optional[str] = Field(None, description="Scénarios associés au devis")

    model_config = ConfigDict(from_attributes=True)