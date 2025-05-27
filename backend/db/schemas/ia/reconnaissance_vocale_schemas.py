from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReconnaissanceVocaleBase(BaseModel):
    utilisateur_id: Optional[int]
    langue: str
    audio_fichier: str
    transcription: Optional[str]
    intention: Optional[str]
    resultat_action: Optional[str]
    moteur_utilise: Optional[str] = "whisper"

    class Config:
        from_attributes = True

class ReconnaissanceVocaleCreate(ReconnaissanceVocaleBase):
    pass

class ReconnaissanceVocaleUpdate(BaseModel):
    transcription: Optional[str]
    intention: Optional[str]
    resultat_action: Optional[str]
    moteur_utilise: Optional[str]

class ReconnaissanceVocaleRead(ReconnaissanceVocaleBase):
    id: int
    date_reconnaissance: datetime

class ReconnaissanceVocaleSearch(BaseModel):
    utilisateur_id: Optional[int]
    langue: Optional[str]
    intention: Optional[str]

class ReconnaissanceVocaleSearchResults(BaseModel):
    results: List[ReconnaissanceVocaleRead]