from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LogIABase(BaseModel):
    utilisateur_id: Optional[int]
    module: str
    action: str
    resultat: Optional[str]
    niveau: Optional[str] = "INFO"
    statut: Optional[str] = "ok"
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class LogIACreate(LogIABase):
    pass

class LogIAUpdate(BaseModel):
    resultat: Optional[str]
    commentaire: Optional[str]
    niveau: Optional[str]
    statut: Optional[str]

class LogIARead(LogIABase):
    id: int
    date_log: datetime

class LogIASearch(BaseModel):
    utilisateur_id: Optional[int]
    module: Optional[str]
    niveau: Optional[str]
    statut: Optional[str]

class LogIASearchResults(BaseModel):
    results: List[LogIARead]