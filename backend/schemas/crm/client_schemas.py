from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ClientBase(BaseModel):
    nom_entreprise: str
    siret: Optional[str]
    adresse: Optional[str]
    code_postal: Optional[str]
    ville: Optional[str]
    pays: Optional[str] = "France"
    tva_intracom: Optional[str]
    notes: Optional[str]
    nom_contact: Optional[str]
    prenom_contact: Optional[str]
    email_contact: Optional[str]
    telephone_contact: Optional[str]

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    nom_entreprise: Optional[str] = None
    siret: Optional[str] = None
    adresse: Optional[str] = None
    code_postal: Optional[str] = None
    ville: Optional[str] = None
    pays: Optional[str] = "France"
    tva_intracom: Optional[str] = None
    notes: Optional[str] = None
    nom_contact: Optional[str] = None
    prenom_contact: Optional[str] = None
    email_contact: Optional[str] = None
    telephone_contact: Optional[str] = None

class ClientRead(ClientBase):
    id: int
    date_creation: datetime

    class Config:
        orm_mode = True

class ClientDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1
            }
        }

class ClientList(BaseModel):
    clients: List[ClientRead]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "clients": [
                    {
                        "id": 1,
                        "nom_entreprise": "Entreprise A",
                        "siret": "12345678901234",
                        "adresse": "123 Rue Exemple",
                        "code_postal": "75001",
                        "ville": "Paris",
                        "pays": "France",
                        "tva_intracom": "FR12345678901",
                        "notes": "Client historique",
                        "nom_contact": "Jean",
                        "prenom_contact": "Dupont",
                        "email_contact": "jean.dupont@example.com",
                        "telephone_contact": "0123456789",
                        "date_creation": "2024-01-01T00:00:00"
                    }
                ]
            }
        }

class ClientSearch(BaseModel):
    query: str

    class Config:
        schema_extra = {
            "example": {
                "query": "Entreprise A"
            }
        }

class ClientSearchResults(BaseModel):
    results: List[ClientRead]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "results": [
                    {
                        "id": 1,
                        "nom_entreprise": "Entreprise A",
                        "siret": "12345678901234",
                        "adresse": "123 Rue Exemple",
                        "code_postal": "75001",
                        "ville": "Paris",
                        "pays": "France",
                        "tva_intracom": "FR12345678901",
                        "notes": "Client historique",
                        "nom_contact": "Jean",
                        "prenom_contact": "Dupont",
                        "email_contact": "jean.dupont@example.com",
                        "telephone_contact": "0123456789",
                        "date_creation": "2024-01-01T00:00:00"
                    }
                ]
            }
        }
