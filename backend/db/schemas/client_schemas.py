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
        

class ClientUpdate(ClientBase):
    nom: Optional[str] = Field(None, description="Nom du client")
    email: Optional[EmailStr] = Field(None, description="Email du client")
    telephone: Optional[str] = Field(None, description="Téléphone du client")
    adresse: Optional[str] = Field(None, description="Adresse du client")
    siret: Optional[str] = Field(None, description="Numéro SIRET du client")
    tva_intracom: Optional[str] = Field(None, description="Numéro de TVA intracommunautaire du client")
    secteur_activite: Optional[str] = Field(None, description="Secteur d'activité du client")
    site_web: Optional[str] = Field(None, description="Site web du client")
    commentaire: Optional[str] = Field(None, description="Commentaire sur le client")
    date_modification: Optional[datetime] = Field(None, description="Date de la dernière modification")