from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

class EPIBase(BaseModel):
    nom: str = Field(..., description="Nom de l'équipement de protection")
    categorie: str = Field(..., description="Catégorie : casque, gants, lunettes, etc.")
    taille: Optional[str] = Field(None, description="Taille ou format")
    fournisseur: Optional[str] = Field(None, description="Nom du fournisseur")
    date_validite: Optional[date] = Field(None, description="Date de validité ou d'expiration")
    statut: Optional[str] = Field("actif", description="Statut : actif, périmé, remplacé")

class EPICreate(EPIBase):
    pass

class EPIUpdate(BaseModel):
    nom: Optional[str] = None
    categorie: Optional[str] = None
    taille: Optional[str] = None
    fournisseur: Optional[str] = None
    date_validite: Optional[date] = None
    statut: Optional[str] = None

class EPIRead(EPIBase):
    id: int = Field(..., description="ID unique de l'EPI")

    class Config:
        model_config = ConfigDict(from_attributes=True)
