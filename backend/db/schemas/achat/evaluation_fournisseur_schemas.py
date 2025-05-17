from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class EvaluationFournisseurBase(BaseModel):
    qualite: float
    delai: float
    communication: float
    conformite: float
    commentaire: Optional[str]
    commande_id: Optional[int]
    fournisseur_id: int
    utilisateur_id: Optional[int]

    class Config:
        from_attributes = True

class EvaluationFournisseurCreate(EvaluationFournisseurBase):
    pass

class EvaluationFournisseurUpdate(BaseModel):
    qualite: Optional[float]
    delai: Optional[float]
    communication: Optional[float]
    conformite: Optional[float]
    commentaire: Optional[str]
    commande_id: Optional[int]
    fournisseur_id: Optional[int]
    utilisateur_id: Optional[int]

class EvaluationFournisseurRead(EvaluationFournisseurBase):
    id: int
    date_evaluation: datetime

class EvaluationFournisseurSearch(BaseModel):
    fournisseur_id: Optional[int]
    utilisateur_id: Optional[int]

class EvaluationFournisseurSearchResults(BaseModel):
    results: List[EvaluationFournisseurRead]
