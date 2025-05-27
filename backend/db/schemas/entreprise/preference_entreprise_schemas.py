from pydantic import BaseModel
from typing import Optional, List

class PreferenceEntrepriseBase(BaseModel):
    entreprise_id: int
    langue: Optional[str] = "fr"
    fuseau_horaire: Optional[str] = "Europe/Paris"
    format_date: Optional[str] = "DD/MM/YYYY"
    affichage_24h: Optional[bool] = True
    theme: Optional[str] = "clair"

    class Config:
        from_attributes = True

class PreferenceEntrepriseCreate(PreferenceEntrepriseBase):
    pass

class PreferenceEntrepriseUpdate(BaseModel):
    langue: Optional[str]
    fuseau_horaire: Optional[str]
    format_date: Optional[str]
    affichage_24h: Optional[bool]
    theme: Optional[str]

class PreferenceEntrepriseRead(PreferenceEntrepriseBase):
    id: int

class PreferenceEntrepriseSearch(BaseModel):
    entreprise_id: Optional[int]
    langue: Optional[str]

class PreferenceEntrepriseSearchResults(BaseModel):
    results: List[PreferenceEntrepriseRead]