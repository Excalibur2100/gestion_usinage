from pydantic import BaseModel, EmailStr
from typing import Optional, List

class ContactClientBase(BaseModel):
    client_id: int
    nom: str
    prenom: Optional[str]
    fonction: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    principal: Optional[bool] = False

    class Config:
        from_attributes = True

class ContactClientCreate(ContactClientBase):
    pass

class ContactClientUpdate(BaseModel):
    client_id: Optional[int]
    nom: Optional[str]
    prenom: Optional[str]
    fonction: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    principal: Optional[bool]

class ContactClientRead(ContactClientBase):
    id: int

class ContactClientSearch(BaseModel):
    client_id: Optional[int]
    nom: Optional[str]
    principal: Optional[bool]

class ContactClientSearchResults(BaseModel):
    results: List[ContactClientRead]