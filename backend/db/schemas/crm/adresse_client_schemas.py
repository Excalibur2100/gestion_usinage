from pydantic import BaseModel
from typing import Optional, List

class AdresseClientBase(BaseModel):
    client_id: int
    type_adresse: str
    ligne_1: str
    ligne_2: Optional[str]
    code_postal: str
    ville: str
    pays: Optional[str] = "France"
    commentaire: Optional[str]
    principale: Optional[bool] = False

    class Config:
        from_attributes = True

class AdresseClientCreate(AdresseClientBase):
    pass

class AdresseClientUpdate(BaseModel):
    client_id: Optional[int]
    type_adresse: Optional[str]
    ligne_1: Optional[str]
    ligne_2: Optional[str]
    code_postal: Optional[str]
    ville: Optional[str]
    pays: Optional[str]
    commentaire: Optional[str]
    principale: Optional[bool]

class AdresseClientRead(AdresseClientBase):
    id: int

class AdresseClientSearch(BaseModel):
    client_id: Optional[int]
    type_adresse: Optional[str]
    ville: Optional[str]
    principale: Optional[bool]

class AdresseClientSearchResults(BaseModel):
    results: List[AdresseClientRead]