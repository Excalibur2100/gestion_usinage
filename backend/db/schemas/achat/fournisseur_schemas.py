from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class FournisseurBase(BaseModel):
    code_fournisseur: str
    nom: str
    contact: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    adresse: Optional[str]
    tva: Optional[str]
    site_web: Optional[str]
    catalogue_interactif: Optional[str]
    type_id: Optional[int]

    class Config:
        from_attributes = True

class FournisseurCreate(FournisseurBase):
    pass

class FournisseurUpdate(BaseModel):
    code_fournisseur: Optional[str]
    nom: Optional[str]
    contact: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    adresse: Optional[str]
    tva: Optional[str]
    site_web: Optional[str]
    catalogue_interactif: Optional[str]
    type_id: Optional[int]

class FournisseurRead(FournisseurBase):
    id: int
    date_creation: datetime

class FournisseurSearch(BaseModel):
    code_fournisseur: Optional[str]
    nom: Optional[str]
    tva: Optional[str]

class FournisseurSearchResults(BaseModel):
    results: List[FournisseurRead]
