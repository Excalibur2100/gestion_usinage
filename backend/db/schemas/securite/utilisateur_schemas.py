
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

# ========================= UTILISATEUR =========================

class UtilisateurBase(BaseModel):
    nom: str
    email: EmailStr
    role: str

class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str = Field(..., min_length=8)

class UtilisateurUpdate(BaseModel):
    nom: Optional[str] = None
    email: Optional[EmailStr] = None
    mot_de_passe: Optional[str] = Field(None, min_length=8)
    role: Optional[str] = None
    actif: Optional[bool] = None

class UtilisateurRead(BaseModel):
    id: int
    nom: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)
        
        

