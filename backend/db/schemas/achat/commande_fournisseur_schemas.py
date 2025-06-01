from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


# -------- ENUM --------
class StatutCommandeFournisseur(str, Enum):
    brouillon = "brouillon"
    envoyee = "envoyee"
    partiellement_livree = "partiellement_livree"
    livree = "livree"
    annulee = "annulee"


# -------- BASE --------
class CommandeFournisseurBase(BaseModel):
    numero_commande: str = Field(..., min_length=5)
    reference_externe: Optional[str] = None
    fournisseur_id: int
    utilisateur_id: Optional[int] = None
    commentaire: Optional[str] = None
    statut: Optional[StatutCommandeFournisseur] = StatutCommandeFournisseur.brouillon

    date_commande: Optional[datetime] = None
    date_livraison_prevue: Optional[datetime] = None
    date_livraison_effective: Optional[datetime] = None

    montant_total: float = Field(..., ge=0)
    devise: Optional[str] = "EUR"

    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None
    version: Optional[int] = 1
    etat_synchronisation: Optional[str] = "non_synchro"
    is_archived: Optional[bool] = False
    uuid: Optional[str] = None

    class Config:
        from_attributes = True
        title = "CommandeFournisseurBase"
        schema_extra = {
            "example": {
                "numero_commande": "CMD-2024-001",
                "fournisseur_id": 1,
                "montant_total": 1250.50,
                "statut": "brouillon",
                "devise": "EUR"
            }
        }


# -------- CREATE --------
class CommandeFournisseurCreate(CommandeFournisseurBase):
    @model_validator(mode="after")
    def verifier_montant(self):
        if self.montant_total < 0:
            raise ValueError("Le montant total ne peut pas être négatif.")
        if not self.numero_commande.startswith("CMD-"):
            raise ValueError("Le numéro de commande doit commencer par 'CMD-'")
        return self


# -------- UPDATE --------
class CommandeFournisseurUpdate(BaseModel):
    commentaire: Optional[str] = None
    statut: Optional[StatutCommandeFournisseur] = None
    date_livraison_effective: Optional[datetime] = None
    is_archived: Optional[bool] = None
    modifie_par: Optional[int] = None
    montant_total: Optional[float] = Field(None, ge=0)
    etat_synchronisation: Optional[str] = None
    version: Optional[int] = None

    class Config:
        from_attributes = True


# -------- READ --------
class CommandeFournisseurRead(CommandeFournisseurBase):
    id: int
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None


# -------- DETAIL --------
class CommandeFournisseurDetail(CommandeFournisseurRead):
    fournisseur_nom: Optional[str] = None
    utilisateur_nom: Optional[str] = None
    auteur_creation_nom: Optional[str] = None
    auteur_modification_nom: Optional[str] = None


# -------- LIST --------
class CommandeFournisseurList(BaseModel):
    id: int
    numero_commande: str
    fournisseur_id: int
    montant_total: float
    statut: StatutCommandeFournisseur
    date_commande: datetime

    class Config:
        from_attributes = True


# -------- SEARCH --------
class CommandeFournisseurSearch(BaseModel):
    numero_commande: Optional[str] = None
    fournisseur_id: Optional[int] = None
    statut: Optional[StatutCommandeFournisseur] = None
    date_min: Optional[datetime] = None
    date_max: Optional[datetime] = None
    min_montant: Optional[float] = None
    max_montant: Optional[float] = None
    is_archived: Optional[bool] = None


# -------- SEARCH RESULTS --------
class CommandeFournisseurSearchResults(BaseModel):
    total: int
    results: List[CommandeFournisseurRead]


# -------- BULK --------
class CommandeFournisseurBulkCreate(BaseModel):
    commandes: List[CommandeFournisseurCreate]


class CommandeFournisseurBulkDelete(BaseModel):
    ids: List[int]


# -------- RESPONSE --------
class CommandeFournisseurResponse(BaseModel):
    message: str
    commande: Optional[CommandeFournisseurRead]