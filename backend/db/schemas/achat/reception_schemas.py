from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, model_validator
from enum import Enum


# Enum conforme au modèle ORM
class StatutReceptionEnum(str, Enum):
    en_attente = "en_attente"
    partiellement_recue = "partiellement_recue"
    recue = "recue"
    refusee = "refusee"
    archivee = "archivee"


# Base commune
class ReceptionBase(BaseModel):
    numero_reception: str = Field(...)
    commande_id: int = Field(..., ge=1, description="ID de la commande (ex: 12)")
    date_reception: datetime = Field(..., json_schema_extra={"example": "2025-06-04T14:30:00"})
    statut: StatutReceptionEnum = Field(..., json_schema_extra={"example": "en_attente"})
    commentaire: Optional[str] = Field(None, json_schema_extra={"example": "Livraison partielle - palette 2 manquante"})
    document_associe: Optional[str] = Field(None, json_schema_extra={"example": "bons/reception_2025_001.pdf"})
    cree_par: Optional[int] = Field(None, ge=1, json_schema_extra={"example": 3})
    modifie_par: Optional[int] = Field(None, ge=1, json_schema_extra={"example": 3})

    class Config:
        orm_mode = True
        from_attributes = True


# Schéma de création
class ReceptionCreate(ReceptionBase):
    pass


# Schéma de mise à jour
class ReceptionUpdate(BaseModel):
    numero_reception: Optional[str] = Field(None, json_schema_extra={"example": "REC-2025-001"})
    commande_id: Optional[int] = Field(None, ge=1, json_schema_extra={"example": 12})
    date_reception: Optional[datetime] = Field(None, json_schema_extra={"example": "2025-06-04T14:30:00"})
    statut: Optional[StatutReceptionEnum] = Field(None, json_schema_extra={"example": "refusee"})
    commentaire: Optional[str] = Field(None, json_schema_extra={"example": "Réception annulée suite à non-conformité"})
    document_associe: Optional[str] = Field(None, json_schema_extra={"example": "bons/annulation_reception.pdf"})
    modifie_par: Optional[int] = Field(None, ge=1, json_schema_extra={"example": 5})

    class Config:
        orm_mode = True
        from_attributes = True


# Schéma de lecture
class ReceptionRead(ReceptionBase):
    id: int = Field(...)
    uuid: Optional[str] = Field(None, json_schema_extra={"example": "a1b2c3d4e5f6"})
    timestamp_creation: datetime = Field(..., json_schema_extra={"example": "2025-06-04T14:35:00"})
    timestamp_modification: datetime = Field(..., json_schema_extra={"example": "2025-06-04T15:00:00"})


# Schéma détaillé
class ReceptionDetail(ReceptionRead):
    auteur_creation_nom: Optional[str] = Field(None, json_schema_extra={"example": "Jean Dupont"})
    auteur_modification_nom: Optional[str] = Field(None, json_schema_extra={"example": "Paul Moreau"})
    commande_reference: Optional[str] = Field(None, json_schema_extra={"example": "CMD-2025-001"})
    lignes_reception: Optional[List[dict]] = None  # À remplacer plus tard par LigneReceptionRead


# Liste
class ReceptionList(BaseModel):
    total: int = Field(..., json_schema_extra={"example": 42})
    receptions: List[ReceptionRead]


# Recherche
class ReceptionSearch(BaseModel):
    numero_reception: Optional[str] = Field(None, json_schema_extra={"example": "REC-2025"})
    commande_id: Optional[int] = Field(None, json_schema_extra={"example": 12})
    statut: Optional[StatutReceptionEnum] = None
    date_debut: Optional[datetime] = Field(None, json_schema_extra={"example": "2025-06-01T00:00:00"})
    date_fin: Optional[datetime] = Field(None, json_schema_extra={"example": "2025-06-30T23:59:59"})


# Résultats de recherche
class ReceptionSearchResults(BaseModel):
    total: int = Field(..., json_schema_extra={"example": 10})
    results: List[ReceptionRead]


# Réponse générique API
class ReceptionResponse(BaseModel):
    message: str = Field(..., json_schema_extra={"example": "Réception créée avec succès."})
    data: Optional[ReceptionRead]


# Création en masse
class ReceptionBulkCreate(BaseModel):
    receptions: List[ReceptionCreate]


# Schéma avec validation avancée
class ReceptionValidated(ReceptionBase):

    @model_validator(mode="after")
    def check_commentaire_if_refusee(self) -> "ReceptionValidated":
        if self.statut == StatutReceptionEnum.refusee and not self.commentaire:
            raise ValueError("Un commentaire est requis pour une réception refusée.")
        return self