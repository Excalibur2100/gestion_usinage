from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AssistantIABase(BaseModel):
    utilisateur_id: Optional[int]
    entreprise_id: Optional[int]
    nom_session: str
    prompt: str
    reponse: Optional[str]
    moteur: Optional[str] = "gpt-4"
    temperature: Optional[str] = "0.7"

    class Config:
        from_attributes = True

class AssistantIACreate(AssistantIABase):
    pass

class AssistantIAUpdate(BaseModel):
    prompt: Optional[str]
    reponse: Optional[str]
    moteur: Optional[str]
    temperature: Optional[str]
    nom_session: Optional[str]

class AssistantIARead(AssistantIABase):
    id: int
    date_session: datetime

class AssistantIASearch(BaseModel):
    utilisateur_id: Optional[int]
    nom_session: Optional[str]

class AssistantIASearchResults(BaseModel):
    results: List[AssistantIARead]