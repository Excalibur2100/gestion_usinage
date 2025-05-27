from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# ------------------------------
# Base
# ------------------------------
class AvoirFournisseurBase(BaseModel):
    numero_avoir: str = Field(..., max_length=100)
    date_avoir: Optional[datetime] = None
    montant: float = Field(..., ge=0)
    motif: Optional[str]
    statut: Optional[str] = "non imputé"
    facture_id: Optional[int]
    fournisseur_id: int

    class Config:
        from_attributes = True
        orm_mode = True

# ------------------------------
# CRUD
# ------------------------------
class AvoirFournisseurCreate(AvoirFournisseurBase):
    """ Schéma de création d'un avoir fournisseur """
    pass

class AvoirFournisseurUpdate(BaseModel):
    """ Schéma de mise à jour partielle d'un avoir fournisseur """
    numero_avoir: Optional[str]
    date_avoir: Optional[datetime]
    montant: Optional[float] = Field(default=None, ge=0)
    motif: Optional[str]
    statut: Optional[str]
    facture_id: Optional[int]
    fournisseur_id: Optional[int]

    class Config:
        from_attributes = True
        orm_mode = True

class AvoirFournisseurRead(AvoirFournisseurBase):
    """ Schéma de lecture simple d’un avoir """
    id: int

# ------------------------------
# Réponses enrichies
# ------------------------------
class AvoirFournisseurDetail(AvoirFournisseurRead):
    """ Détail complet d’un avoir """
    facture_id: Optional[int]
    fournisseur_id: int

class AvoirFournisseurCreateResponse(AvoirFournisseurRead):
    """ Réponse enrichie après création """
    message: str = "Avoir fournisseur créé avec succès"

class AvoirFournisseurUpdateResponse(AvoirFournisseurRead):
    """ Réponse enrichie après mise à jour """
    message: str = "Avoir fournisseur mis à jour avec succès"

class AvoirFournisseurDeleteResponse(BaseModel):
    """ Réponse après suppression """
    id: int
    message: str = "Avoir fournisseur supprimé avec succès"

# ------------------------------
# Liste / Recherche
# ------------------------------
class AvoirFournisseurSearch(BaseModel):
    """ Critères de recherche """
    numero_avoir: Optional[str]
    fournisseur_id: Optional[int]
    statut: Optional[str]

class AvoirFournisseurSearchResults(BaseModel):
    """ Résultats de recherche avec total """
    results: List[AvoirFournisseurRead]
    total: int

class AvoirFournisseurList(BaseModel):
    """ Liste paginée des avoirs """
    items: List[AvoirFournisseurRead]
    total: int