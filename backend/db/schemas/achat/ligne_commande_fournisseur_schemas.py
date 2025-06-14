from pydantic import BaseModel, Field, model_validator, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum


# -------- ENUM --------
class StatutLigneCommande(str, Enum):
    non_recue = "non_recue"
    partiellement_recue = "partiellement_recue"
    recue = "recue"
    annulee = "annulee"


# -------- BASE --------
class LigneCommandeFournisseurBase(BaseModel):
    commande_id: int = Field(..., description="ID de la commande fournisseur")
    article_id: Optional[int] = Field(None, description="ID de l'article (facultatif)")
    designation: str = Field(..., description="Exemple: Rond acier 42CrMo4 Ø50mm")
    description: Optional[str] = Field(None, description="Pièce brute pour usinage")
    quantite: float = Field(..., ge=0, json_schema_extra={"example": 10.0})
    prix_unitaire_ht: float = Field(..., ge=0, json_schema_extra={"example": 15.5})
    taux_tva: float = Field(default=20.0, ge=0, json_schema_extra={"example": 20.0})
    montant_ht: float = Field(..., ge=0, json_schema_extra={"example": 155.0})
    montant_ttc: float = Field(..., ge=0, json_schema_extra={"example": 186.0})
    unite: Optional[str] = Field(None, json_schema_extra={"example": "pièce"})
    statut: Optional[StatutLigneCommande] = Field(default=StatutLigneCommande.non_recue)
    commentaire: Optional[str] = Field(None, json_schema_extra={"example": "Livraison en attente de confirmation"})
    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True


# -------- CREATE --------
class LigneCommandeFournisseurCreate(LigneCommandeFournisseurBase):
    @model_validator(mode="after")
    def verifier_coherence_montant(self):
        attendu = round(self.quantite * self.prix_unitaire_ht * (1 + self.taux_tva / 100), 2)
        if abs(self.montant_ttc - attendu) > 0.01:
            raise ValueError(f"Incohérence montant TTC attendu : {attendu}")
        return self


# -------- UPDATE --------
class LigneCommandeFournisseurUpdate(BaseModel):
    quantite: Optional[float] = Field(None, ge=0)
    prix_unitaire_ht: Optional[float] = Field(None, ge=0)
    taux_tva: Optional[float] = Field(None, ge=0)
    commentaire: Optional[str] = None
    statut: Optional[StatutLigneCommande] = None
    modifie_par: Optional[int] = None


# -------- READ --------
class LigneCommandeFournisseurRead(LigneCommandeFournisseurBase):
    id: int
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None


# -------- DETAIL --------
class LigneCommandeFournisseurDetail(LigneCommandeFournisseurRead):
    article_nom: Optional[str] = None
    auteur_creation_nom: Optional[str] = None
    auteur_modification_nom: Optional[str] = None


# -------- LIST --------
class LigneCommandeFournisseurList(BaseModel):
    id: int
    designation: str
    quantite: float
    montant_ttc: float
    statut: StatutLigneCommande

    class Config:
        orm_mode = True
        from_attributes = True


# -------- SEARCH --------
class LigneCommandeFournisseurSearch(BaseModel):
    commande_id: Optional[int] = None
    article_id: Optional[int] = None
    designation: Optional[str] = None
    statut: Optional[StatutLigneCommande] = None


# -------- BULK --------
class LigneCommandeFournisseurBulkCreate(BaseModel):
    lignes: List[LigneCommandeFournisseurCreate]


class LigneCommandeFournisseurBulkDelete(BaseModel):
    ids: List[int]


# -------- RESPONSE --------
class LigneCommandeFournisseurResponse(BaseModel):
    message: str
    ligne: Optional[LigneCommandeFournisseurRead]


# -------- SEARCH RESULTS --------
class LigneCommandeFournisseurSearchResults(BaseModel):
    total: int
    results: List[LigneCommandeFournisseurRead]