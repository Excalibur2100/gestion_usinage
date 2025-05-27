from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class ClientBase(BaseModel):
    code_client: str
    nom: str
    email: Optional[EmailStr]
    telephone: Optional[str]
    site_web: Optional[str]
    tva: Optional[str]
    actif: Optional[bool] = True
    segment_id: Optional[int]
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    code_client: Optional[str]
    nom: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    site_web: Optional[str]
    tva: Optional[str]
    actif: Optional[bool]
    segment_id: Optional[int]
    commentaire: Optional[str]

class ClientRead(ClientBase):
    id: int
    date_creation: datetime

class ClientSearch(BaseModel):
    code_client: Optional[str]
    nom: Optional[str]
    tva: Optional[str]
    actif: Optional[bool]

class ClientSearchResults(BaseModel):
    results: List[ClientRead]