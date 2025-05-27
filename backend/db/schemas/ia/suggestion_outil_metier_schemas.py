from pydantic import BaseModel
from typing import Optional

class SuggestionOutilIARequest(BaseModel):
    piece_id: int
    operation: Optional[str] = None
    matiere: Optional[str] = "acier"