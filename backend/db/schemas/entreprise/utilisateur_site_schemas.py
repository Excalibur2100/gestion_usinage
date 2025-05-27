from pydantic import BaseModel
from typing import Optional, List

class UtilisateurSiteBase(BaseModel):
    utilisateur_id: int
    site_id: int

    class Config:
        from_attributes = True

class UtilisateurSiteCreate(UtilisateurSiteBase):
    pass

class UtilisateurSiteUpdate(BaseModel):
    utilisateur_id: Optional[int]
    site_id: Optional[int]

class UtilisateurSiteRead(UtilisateurSiteBase):
    id: int

class UtilisateurSiteSearch(BaseModel):
    utilisateur_id: Optional[int]
    site_id: Optional[int]

class UtilisateurSiteSearchResults(BaseModel):
    results: List[UtilisateurSiteRead]