from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


# -------- ENUM --------

class StatutFactureFournisseur(str, Enum):
    brouillon = "brouillon"
    validee = "validee"
    payee = "payee"
    partiellement_payee = "partiellement_payee"
    annulee = "annulee"
    en_retard = "en_retard"


# -------- BASE --------

class FactureFournisseurBase(BaseModel):
    numero_facture: str = Field(..., json_schema_extra={"example": "FAC-2024-001"})
    reference_externe: Optional[str] = Field(None, json_schema_extra={"example": "EXT-REF-01"})
    fournisseur_id: int = Field(..., json_schema_extra={"example": 1})
    utilisateur_id: Optional[int] = Field(None, json_schema_extra={"example": 42})
    commande_id: Optional[int] = Field(None, json_schema_extra={"example": 5})

    date_facture: Optional[datetime] = None
    date_echeance: Optional[datetime] = None
    date_paiement: Optional[datetime] = None

    montant_ht: float = Field(..., ge=0, json_schema_extra={"example": 100.0})
    taux_tva: float = Field(default=20.0, ge=0, json_schema_extra={"example": 20.0})
    montant_ttc: float = Field(..., ge=0, json_schema_extra={"example": 120.0})

    devise: str = Field(default="EUR", json_schema_extra={"example": "EUR"})
    commentaire: Optional[str] = None

    statut: Optional[StatutFactureFournisseur] = StatutFactureFournisseur.brouillon

    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None

    version: Optional[int] = 1
    etat_synchronisation: Optional[str] = "non_synchro"
    is_archived: Optional[bool] = False

    class Config:
        orm_mode = True
        from_attributes = True
        title = "FactureFournisseurBase"


# -------- CREATE --------

class FactureFournisseurCreate(FactureFournisseurBase):
    @model_validator(mode="after")
    def check_total_amount(self):
        if (
            self.montant_ht is not None
            and self.taux_tva is not None
            and self.montant_ttc is not None
        ):
            expected = round(self.montant_ht * (1 + self.taux_tva / 100), 2)
            if abs(self.montant_ttc - expected) > 0.01:
                raise ValueError(f"Le montant TTC ne correspond pas à HT + TVA ({expected} attendu)")
        return self


# -------- UPDATE --------

class FactureFournisseurUpdate(BaseModel):
    commentaire: Optional[str] = None
    statut: Optional[StatutFactureFournisseur] = None
    date_paiement: Optional[datetime] = None
    is_archived: Optional[bool] = None
    modifie_par: Optional[int] = None

    @model_validator(mode="after")
    def check_statut(self):
        return self


# -------- READ --------

class FactureFournisseurRead(FactureFournisseurBase):
    id: int
    uuid: Optional[str] = None
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None


# -------- DETAIL --------

class FactureFournisseurDetail(FactureFournisseurRead):
    fournisseur_nom: Optional[str] = None
    utilisateur_nom: Optional[str] = None
    auteur_creation_nom: Optional[str] = None
    auteur_modification_nom: Optional[str] = None


# -------- LIST --------

class FactureFournisseurList(BaseModel):
    id: int
    numero_facture: str
    fournisseur_id: int
    montant_ttc: float
    statut: StatutFactureFournisseur
    date_facture: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True


# -------- SEARCH --------

class FactureFournisseurSearch(BaseModel):
    numero_facture: Optional[str] = None
    fournisseur_id: Optional[int] = None
    statut: Optional[StatutFactureFournisseur] = None
    date_min: Optional[datetime] = None
    date_max: Optional[datetime] = None
    is_archived: Optional[bool] = None


# -------- RESPONSE --------

class FactureFournisseurResponse(BaseModel):
    message: str
    facture: Optional[FactureFournisseurRead]


# -------- BULK --------

class FactureFournisseurBulkCreate(BaseModel):
    factures: List[FactureFournisseurCreate]


class FactureFournisseurBulkDelete(BaseModel):
    ids: List[int]


# -------- SEARCH RESULTS --------

class FactureFournisseurSearchResults(BaseModel):
    total: int
    results: List[FactureFournisseurRead]