from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

class OFBase(BaseModel):
    numero: str = Field(..., description="Numéro d'ordre de fabrication")
    produit_id: Optional[int] = Field(None, description="ID du produit")
    poste_id: Optional[int] = Field(None, description="Poste assigné")
    utilisateur_id: Optional[int] = Field(None, description="Opérateur assigné")
    date_lancement: date = Field(..., description="Date de lancement")
    date_fin: Optional[date] = Field(None, description="Date de fin estimée")
    statut: Optional[str] = Field("prévu", description="Statut de l'ordre")
    commentaire: Optional[str] = Field(None, description="Remarques complémentaires")

class OFCreate(OFBase):
    pass

class OFUpdate(BaseModel):
    produit_id: Optional[int] = None
    poste_id: Optional[int] = None
    utilisateur_id: Optional[int] = None
    date_lancement: Optional[date] = None
    date_fin: Optional[date] = None
    statut: Optional[str] = None
    commentaire: Optional[str] = None

class OFRead(OFBase):
    id: int = Field(..., description="ID unique")

    class Config:
        model_config = ConfigDict(from_attributes=True)
