from pydantic import BaseModel, Field, model_validator
from typing import Optional, List, Generic, TypeVar
from datetime import datetime
from enum import Enum


# -------- ENUMS --------
class StatutAvoir(str, Enum):
    brouillon = "brouillon"
    valide = "valide"
    rembourse = "rembourse"
    annule = "annule"

class TypeAvoir(str, Enum):
    retour = "retour_marchandise"
    remise = "remise_commerciale"
    geste = "geste_commercial"
    autre = "autre"


# -------- BASE --------
class AvoirFournisseurBase(BaseModel):
    reference: str = Field(..., alias="reference")
    reference_externe: Optional[str] = None
    fournisseur_id: int
    utilisateur_id: Optional[int] = None
    commande_id: Optional[int] = None
    facture_id: Optional[int] = None
    document_lie_id: Optional[int] = None

    type_avoir: Optional[TypeAvoir] = TypeAvoir.autre
    motif: Optional[str] = Field(None, json_schema_extra={"example": "Erreur de livraison"})
    commentaire: Optional[str] = None
    categorie: Optional[str] = None
    tag: Optional[str] = None

    montant_ht: float = Field(..., ge=0)
    taux_tva: float = Field(default=20.0, ge=0)
    montant_ttc: float = Field(..., ge=0)
    ecart_montant: Optional[float] = None

    devise: str = Field(default="EUR")
    montant_devise_origine: Optional[float] = None
    taux_conversion: Optional[float] = None

    statut: Optional[StatutAvoir] = StatutAvoir.brouillon
    date_emission: Optional[datetime] = None
    date_remboursement: Optional[datetime] = None

    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None
    version: Optional[int] = 1
    etat_synchronisation: Optional[str] = "non_synchro"
    is_archived: Optional[bool] = False

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True
        title = "AvoirFournisseurBase"
        schema_extra = {
            "example": {
                "reference": "AVF-2024-001",
                "fournisseur_id": 2,
                "montant_ht": 100.0,
                "taux_tva": 20.0,
                "montant_ttc": 120.0,
                "statut": "brouillon",
                "type_avoir": "remise_commerciale",
                "devise": "EUR",
                "cree_par": 1
            }
        }


# -------- CREATE --------
class AvoirFournisseurCreate(AvoirFournisseurBase):
    @model_validator(mode="after")
    def check_total_amount(self):
        if self.montant_ht is not None and self.taux_tva is not None and self.montant_ttc is not None:
            expected = round(self.montant_ht * (1 + self.taux_tva / 100), 2)
            if abs(self.montant_ttc - expected) > 0.01:
                raise ValueError(f"Le montant TTC ne correspond pas à HT + TVA ({expected} attendu)")
        return self


# -------- UPDATE --------
class AvoirFournisseurUpdate(BaseModel):
    commentaire: Optional[str] = None
    motif: Optional[str] = None
    statut: Optional[StatutAvoir] = None
    tag: Optional[str] = None
    categorie: Optional[str] = None
    is_archived: Optional[bool] = None
    modifie_par: Optional[int] = None


# -------- READ --------
class AvoirFournisseurRead(AvoirFournisseurBase):
    id: int
    uuid: Optional[str] = None
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None


# -------- DETAIL --------
class AvoirFournisseurDetail(AvoirFournisseurRead):
    fournisseur_nom: Optional[str] = None
    utilisateur_nom: Optional[str] = None
    auteur_creation_nom: Optional[str] = None
    auteur_modification_nom: Optional[str] = None


# -------- LIST --------
class AvoirFournisseurList(BaseModel):
    id: int
    reference: str
    fournisseur_id: int
    montant_ttc: float
    statut: StatutAvoir
    date_emission: datetime

    class Config:
        orm_mode = True
        from_attributes = True


# -------- SEARCH --------
class AvoirFournisseurSearch(BaseModel):
    reference: Optional[str] = None
    fournisseur_id: Optional[int] = None
    statut: Optional[StatutAvoir] = None
    type_avoir: Optional[TypeAvoir] = None
    date_min: Optional[datetime] = None
    date_max: Optional[datetime] = None
    is_archived: Optional[bool] = None


# -------- PAGINATED RESPONSE --------
T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    total: int
    results: List[T]


# -------- SEARCH RESULTS --------
class AvoirFournisseurSearchResults(PaginatedResponse[AvoirFournisseurList]):
    pass


# -------- RESPONSE --------
class AvoirFournisseurResponse(BaseModel):
    message: str
    avoir: Optional[AvoirFournisseurRead]


# -------- BULK --------
class AvoirFournisseurBulkCreate(BaseModel):
    avoirs: List[AvoirFournisseurCreate]

class AvoirFournisseurBulkDelete(BaseModel):
    ids: List[int]