from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from datetime import datetime

class LigneReceptionBase(BaseModel):
    reception_id: int = Field(...)
    designation: str = Field(...)
    quantite_commandee: float = Field(..., ge=0.0, json_schema_extra={"example": 100.0})
    quantite_recue: float = Field(..., ge=0.0, json_schema_extra={"example": 80.0})
    unite: Optional[str] = Field(None, json_schema_extra={"example": "pcs"})
    commentaire: Optional[str] = Field(None, json_schema_extra={"example": "RAS"})
    statut: str = Field(default="brouillon", json_schema_extra={"example": "brouillon"})
    etat: str = Field(default="non_conforme", json_schema_extra={"example": "non_conforme"})
    devise: str = Field(default="EUR", json_schema_extra={"example": "EUR"})
    is_archived: bool = Field(default=False)
    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None
    version: int = Field(default=1)
    etat_synchronisation: str = Field(default="non_synchro")
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None

    @model_validator(mode="after")
    def check_quantites(cls, values):
        if values.quantite_recue is not None and values.quantite_commandee is not None:
            if values.quantite_recue > values.quantite_commandee:
                raise ValueError("La quantité reçue ne peut pas dépasser la quantité commandée.")
        return values

class LigneReceptionCreate(LigneReceptionBase):
    pass

class LigneReceptionUpdate(BaseModel):
    designation: Optional[str] = None
    quantite_commandee: Optional[float] = None
    quantite_recue: Optional[float] = None
    unite: Optional[str] = None
    commentaire: Optional[str] = None
    statut: Optional[str] = None
    etat: Optional[str] = None
    modifie_par: Optional[int] = None
    is_archived: Optional[bool] = None

class LigneReceptionRead(LigneReceptionBase):
    id: int
    uuid: str

    class Config:
        orm_mode = True

class LigneReceptionList(BaseModel):
    results: List[LigneReceptionRead]
    total: int

class LigneReceptionBulkCreate(BaseModel):
    objets: List[LigneReceptionCreate]

class LigneReceptionBulkDelete(BaseModel):
    ids: List[int]

class LigneReceptionSearch(BaseModel):
    designation: Optional[str] = None
    reception_id: Optional[int] = None
    statut: Optional[str] = None
    etat: Optional[str] = None
    date_debut: Optional[datetime] = None
    date_fin: Optional[datetime] = None