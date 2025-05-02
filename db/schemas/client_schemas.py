from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class ClientBase(BaseModel):
    nom: str
    email: Optional[str]
    telephone: Optional[str]
    adresse: Optional[str]
    siret: Optional[str]
    tva_intracom: Optional[str]
    secteur_activite: Optional[str]
    site_web: Optional[str]
    commentaire: Optional[str]

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        

