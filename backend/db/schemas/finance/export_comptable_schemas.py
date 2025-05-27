from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ExportComptableBase(BaseModel):
    entreprise_id: int
    utilisateur_id: Optional[int]
    type_export: str
    format_export: str = "CSV"
    chemin_fichier: str
    commentaire: Optional[str]

    class Config:
        from_attributes = True

class ExportComptableCreate(ExportComptableBase):
    pass

class ExportComptableUpdate(BaseModel):
    type_export: Optional[str]
    format_export: Optional[str]
    chemin_fichier: Optional[str]
    commentaire: Optional[str]

class ExportComptableRead(ExportComptableBase):
    id: int
    date_export: datetime

class ExportComptableSearch(BaseModel):
    entreprise_id: Optional[int]
    type_export: Optional[str]
    format_export: Optional[str]

class ExportComptableSearchResults(BaseModel):
    results: List[ExportComptableRead]