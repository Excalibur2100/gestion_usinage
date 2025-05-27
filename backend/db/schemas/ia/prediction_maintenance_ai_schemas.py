from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PredictionAIBase(BaseModel):
    machine_id: Optional[int]
    utilisateur_id: Optional[int]
    type_prediction: str
    niveau_risque: Optional[str] = "modéré"
    delai_prediction: Optional[str]
    message: Optional[str]
    source_ia: Optional[str] = "gpt-4"

    class Config:
        from_attributes = True

class PredictionAICreate(PredictionAIBase):
    pass

class PredictionAIUpdate(BaseModel):
    niveau_risque: Optional[str]
    delai_prediction: Optional[str]
    message: Optional[str]
    source_ia: Optional[str]
    type_prediction: Optional[str]

class PredictionAIRead(PredictionAIBase):
    id: int
    date_prediction: datetime

class PredictionAISearch(BaseModel):
    machine_id: Optional[int]
    type_prediction: Optional[str]
    niveau_risque: Optional[str]

class PredictionAISearchResults(BaseModel):
    results: List[PredictionAIRead]