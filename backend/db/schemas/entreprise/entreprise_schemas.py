from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class EntrepriseBase(BaseModel):
    nom: str
    raison_sociale: Optional[str]
    type_entreprise: Optional[str]
    siret: Optional[str]
    tva_intra: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    adresse: Optional[str]
    pays: Optional[str] = "France"
    site_web: Optional[str]
    logo: Optional[str]
    description: Optional[str]
    actif: Optional[bool] = True

    class Config:
        from_attributes = True

class EntrepriseCreate(EntrepriseBase):
    pass

class EntrepriseUpdate(EntrepriseBase):
    pass

class EntrepriseRead(EntrepriseBase):
    id: int
    date_creation: datetime

class EntrepriseDelete(BaseModel):
    id: int

class EntrepriseSearch(BaseModel):
    nom: Optional[str]
    siret: Optional[str]
    pays: Optional[str]

class EntrepriseSearchResults(BaseModel):
    results: list[EntrepriseRead]
