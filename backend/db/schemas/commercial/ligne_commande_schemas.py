from pydantic import BaseModel
from typing import Optional, List

class LigneCommandeBase(BaseModel):
    commande_id: int
    produit_id: int
    designation: str
    quantite: float
    unite: str
    prix_unitaire: float
    remise: Optional[float] = 0.0
    commentaire: Optional[str]
    statut_livraison: Optional[str] = "non livré"

    class Config:
        from_attributes = True

class LigneCommandeCreate(LigneCommandeBase):
    pass

class LigneCommandeUpdate(BaseModel):
    commande_id: Optional[int]
    produit_id: Optional[int]
    designation: Optional[str]
    quantite: Optional[float]
    unite: Optional[str]
    prix_unitaire: Optional[float]
    remise: Optional[float]
    commentaire: Optional[str]
    statut_livraison: Optional[str]

class LigneCommandeRead(LigneCommandeBase):
    id: int

class LigneCommandeSearch(BaseModel):
    designation: Optional[str]
    commande_id: Optional[int]
    produit_id: Optional[int]

class LigneCommandeSearchResults(BaseModel):
    results: List[LigneCommandeRead]
