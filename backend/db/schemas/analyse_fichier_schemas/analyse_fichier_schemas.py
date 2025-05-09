from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalyseFichierBase(BaseModel):
    nom_fichier: str
    type_fichier: str
    resultat: Optional[str] = None
    date_analyse: datetime

class AnalyseFichierCreate(AnalyseFichierBase):
    pass

class AnalyseFichierUpdate(BaseModel):
    nom_fichier: Optional[str] = None
    type_fichier: Optional[str] = None
    resultat: Optional[str] = None
    date_analyse: Optional[datetime] = None

class AnalyseFichierResponse(AnalyseFichierBase):
    id: int

    class Config:
        orm_mode = True