from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class PosteBase(BaseModel):
    nom: str = Field(..., description="Nom du poste")
    type_poste: str = Field(..., description="Type de poste")
    emplacement: Optional[str] = Field(None, description="Emplacement dans l’atelier")
    machine_id: Optional[int] = Field(None, description="Machine liée")
    utilisateur_id: Optional[int] = Field(None, description="Employé assigné")
    statut: Optional[str] = Field("actif", description="Statut du poste")
    description: Optional[str] = Field(None, description="Notes ou remarques")

class PosteCreate(PosteBase):
    pass

class PosteUpdate(BaseModel):
    nom: Optional[str] = None
    type_poste: Optional[str] = None
    emplacement: Optional[str] = None
    machine_id: Optional[int] = None
    utilisateur_id: Optional[int] = None
    statut: Optional[str] = None
    description: Optional[str] = None

class PosteRead(PosteBase):
    id: int = Field(..., description="ID unique")

    class Config:
        model_config = ConfigDict(from_attributes=True)
