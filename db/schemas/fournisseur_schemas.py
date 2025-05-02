from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class FournisseurBase(BaseModel):
    nom: str
    contact: Optional[str]
    email: Optional[str]
    telephone: Optional[str]
    adresse: Optional[str]
    tva: Optional[str]
    site_web: Optional[str]
    catalogue_interactif: Optional[str]

class FournisseurCreate(FournisseurBase):
    pass

class FournisseurRead(FournisseurBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        

