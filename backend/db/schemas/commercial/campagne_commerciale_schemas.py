from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CampagneCommercialeBase(BaseModel):
    nom: str
    objectif: Optional[str]
    date_debut: Optional[datetime]
    date_fin: Optional[datetime]
    statut: Optional[str] = "planifiée"

    class Config:
        from_attributes = True

class CampagneCommercialeCreate(CampagneCommercialeBase):
    pass

class CampagneCommercialeUpdate(BaseModel):
    nom: Optional[str]
    objectif: Optional[str]
    date_debut: Optional[datetime]
    date_fin: Optional[datetime]
    statut: Optional[str]

class CampagneCommercialeRead(CampagneCommercialeBase):
    id: int

class CampagneCommercialeSearch(BaseModel):
    nom: Optional[str]
    statut: Optional[str]

class CampagneCommercialeSearchResults(BaseModel):
    results: List[CampagneCommercialeRead]
