from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


# -------- ENUM --------

class StatutEvaluation(str, Enum):
    excellent = "excellent"
    bon = "bon"
    moyen = "moyen"
    faible = "faible"
    critique = "critique"


class TypeEvaluation(str, Enum):
    ponctuelle = "ponctuelle"
    periodique = "periodique"
    automatique = "automatique"
    audit = "audit"


# -------- BASE --------

class EvaluationFournisseurBase(BaseModel):
    fournisseur_id: int
    utilisateur_id: Optional[int] = None
    evalue_par: Optional[int] = None

    commande_id: Optional[int] = None
    facture_id: Optional[int] = None
    reception_id: Optional[int] = None
    document_associe_id: Optional[int] = None

    date_evaluation: Optional[datetime] = None
    periode: Optional[str] = None

    note_qualite: Optional[float] = None
    note_delai: Optional[float] = None
    note_prix: Optional[float] = None
    note_globale: float

    statut: StatutEvaluation
    type_evaluation: Optional[TypeEvaluation] = TypeEvaluation.ponctuelle
    origine: Optional[str] = None

    commentaire: Optional[str] = None
    recommandation: Optional[str] = None
    indice_confiance: Optional[float] = None

    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None
    version: Optional[int] = 1
    is_archived: Optional[bool] = False
    etat_synchronisation: Optional[str] = "non_synchro"

    class Config:
        orm_mode = True
        from_attributes = True
        title = "EvaluationFournisseurBase"
        schema_extra = {
            "example": {
                "fournisseur_id": 1,
                "note_globale": 85.0,
                "statut": "bon",
                "type_evaluation": "ponctuelle"
            }
        }


# -------- CREATE --------

class EvaluationFournisseurCreate(EvaluationFournisseurBase):
    @model_validator(mode="after")
    def check_notes(self):
        if self.note_globale < 0 or self.note_globale > 100:
            raise ValueError("La note globale doit être entre 0 et 100.")
        return self


# -------- UPDATE --------

class EvaluationFournisseurUpdate(BaseModel):
    commentaire: Optional[str] = None
    recommandation: Optional[str] = None
    note_qualite: Optional[float] = None
    note_delai: Optional[float] = None
    note_prix: Optional[float] = None
    note_globale: Optional[float] = None
    statut: Optional[StatutEvaluation] = None
    type_evaluation: Optional[TypeEvaluation] = None
    origine: Optional[str] = None
    is_archived: Optional[bool] = None
    modifie_par: Optional[int] = None

    @model_validator(mode="after")
    def check_globale_if_present(self):
        if self.note_globale is not None and (self.note_globale < 0 or self.note_globale > 100):
            raise ValueError("La note globale mise à jour doit être entre 0 et 100.")
        return self

    class Config:
        from_attributes = True


# -------- READ --------

class EvaluationFournisseurRead(EvaluationFournisseurBase):
    id: int
    uuid: Optional[str] = None
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None


# -------- DETAIL --------

class EvaluationFournisseurDetail(EvaluationFournisseurRead):
    fournisseur_nom: Optional[str] = None
    auteur_nom: Optional[str] = None
    document_associe_nom: Optional[str] = None


# -------- LIST --------

class EvaluationFournisseurList(BaseModel):
    id: int
    fournisseur_id: int
    note_globale: float
    statut: StatutEvaluation
    date_evaluation: datetime

    class Config:
        orm_mode = True
        from_attributes = True


# -------- READ MINIMAL --------

class EvaluationFournisseurReadMinimal(BaseModel):
    id: int
    fournisseur_id: int
    note_globale: float
    statut: StatutEvaluation

    class Config:
        orm_mode = True
        from_attributes = True


# -------- SEARCH --------

class EvaluationFournisseurSearch(BaseModel):
    fournisseur_id: Optional[int] = None
    statut: Optional[StatutEvaluation] = None
    type_evaluation: Optional[TypeEvaluation] = None
    date_min: Optional[datetime] = None
    date_max: Optional[datetime] = None
    is_archived: Optional[bool] = None


# -------- RESPONSE --------

class EvaluationFournisseurResponse(BaseModel):
    message: str
    evaluation: Optional[EvaluationFournisseurRead]


# -------- BULK --------

class EvaluationFournisseurBulkCreate(BaseModel):
    evaluations: List[EvaluationFournisseurCreate]


class EvaluationFournisseurBulkDelete(BaseModel):
    ids: List[int]


# -------- SEARCH RESULTS --------

class EvaluationFournisseurSearchResults(BaseModel):
    total: int
    results: List[EvaluationFournisseurRead]