from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, validator

class MaintenanceBase(BaseModel):
    """
    Schéma de base pour une maintenance.
    """
    machine_id: int = Field(..., description="ID de la machine associée")
    utilisateur_id: Optional[int] = Field(None, description="ID de l'utilisateur responsable")
    type_maintenance: str = Field(..., description="Type de maintenance (préventive, corrective, prédictive)")
    date_planifiee: datetime = Field(..., description="Date planifiée pour la maintenance")
    date_reelle: Optional[datetime] = Field(None, description="Date réelle de réalisation de la maintenance")
    statut: str = Field(..., description="Statut de la maintenance (planifiée, en cours, réalisée)")
    description: Optional[str] = Field(None, description="Description de la maintenance")
    remarques: Optional[str] = Field(None, description="Remarques supplémentaires")

class MaintenanceCreate(MaintenanceBase):
    """
    Schéma pour la création d'une maintenance.
    """
    pass

class MaintenanceRead(MaintenanceBase):
    """
    Schéma pour la lecture d'une maintenance.
    """
    id: int = Field(..., description="ID unique de la maintenance")
    created_at: datetime = Field(..., description="Date de création de l'enregistrement")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière mise à jour de l'enregistrement")

    model_config = ConfigDict(from_attributes=True)

class MaintenanceUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'une maintenance.
    """
    machine_id: Optional[int] = Field(None, description="ID de la machine associée")
    utilisateur_id: Optional[int] = Field(None, description="ID de l'utilisateur responsable")
    type_maintenance: Optional[str] = Field(None, description="Type de maintenance (préventive, corrective, prédictive)")
    date_planifiee: Optional[datetime] = Field(None, description="Date planifiée pour la maintenance")
    date_reelle: Optional[datetime] = Field(None, description="Date réelle de réalisation de la maintenance")
    statut: Optional[str] = Field(None, description="Statut de la maintenance (planifiée, en cours, réalisée)")
    description: Optional[str] = Field(None, description="Description de la maintenance")
    remarques: Optional[str] = Field(None, description="Remarques supplémentaires")

    @validator('statut')
    def validate_statut(cls, value):
        """
        Valide que le statut est l'un des suivants : planifiée, en cours, réalisée.
        """
        if value not in ['planifiée', 'en cours', 'réalisée']:
            raise ValueError("Statut doit être l'un des suivants: planifiée, en cours, réalisée")
        return value

    model_config = ConfigDict(from_attributes=True)