from fastapi import APIRouter
from pydantic import BaseModel
from core.ia.voice_engine import VoiceEngine

router = APIRouter(prefix="/reconnaissances-vocales-metier", tags=["Reconnaissance Vocale Métier"])

class ReconnaissanceVocaleRequest(BaseModel):
    audio_fichier: str
    langue: str = "fr"

@router.post("/simuler")
def simuler(data: ReconnaissanceVocaleRequest):
    return VoiceEngine.simuler_transcription(audio_fichier=data.audio_fichier, langue=data.langue)