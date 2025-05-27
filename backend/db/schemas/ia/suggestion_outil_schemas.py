from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SuggestionOutilBase(BaseModel):
    piece_id: int
    outil_id: Optional[int]
    programme_id: Optional[int]
    machine_id: Optional[int]
    log_ia_id: Optional[int]

    score: Optional[float]
    commentaire: Optional[str]

    valide_par_humain: Optional[bool] = False
    decision_commentaire: Optional[str]
    date_validation: Optional[datetime]

    class Config:
        from_attributes = True

class SuggestionOutilCreate(SuggestionOutilBase): pass

class SuggestionOutilUpdate(BaseModel):
    outil_id: Optional[int]
    programme_id: Optional[int]
    machine_id: Optional[int]
    log_ia_id: Optional[int]
    score: Optional[float]
    commentaire: Optional[str]
    valide_par_humain: Optional[bool]
    decision_commentaire: Optional[str]
    date_validation: Optional[datetime]

class SuggestionOutilRead(SuggestionOutilBase):
    id: int
    date_suggestion: datetime