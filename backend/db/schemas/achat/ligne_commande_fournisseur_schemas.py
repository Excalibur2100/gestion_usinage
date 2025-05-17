from pydantic import BaseModel
from typing import Optional, List

class LigneCommandeFournisseurBase(BaseModel):
    commande_id: int
    produit_id: int
    designation: str
    quantite: float
    unite: str
    prix_unitaire: float
    remise: Optional[float] = 0.0
    commentaire: Optional[str]
    statut_reception: Optional[str] = "non reçu"

    class Config:
        from_attributes = True

class LigneCommandeFournisseurCreate(LigneCommandeFournisseurBase):
    pass

class LigneCommandeFournisseurUpdate(BaseModel):
    commande_id: Optional[int]
    produit_id: Optional[int]
    designation: Optional[str]
    quantite: Optional[float]
    unite: Optional[str]
    prix_unitaire: Optional[float]
    remise: Optional[float]
    commentaire: Optional[str]
    statut_reception: Optional[str]

class LigneCommandeFournisseurRead(LigneCommandeFournisseurBase):
    id: int

class LigneCommandeFournisseurSearch(BaseModel):
    designation: Optional[str]
    commande_id: Optional[int]
    produit_id: Optional[int]

class LigneCommandeFournisseurSearchResults(BaseModel):
    results: List[LigneCommandeFournisseurRead]
