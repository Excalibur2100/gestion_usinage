from pydantic import BaseModel
from typing import Optional, List

class AutorisationDocumentBase(BaseModel):
    document_id: int
    utilisateur_id: int
    peut_lire: Optional[bool] = True
    peut_modifier: Optional[bool] = False
    peut_supprimer: Optional[bool] = False
    peut_signer: Optional[bool] = False

    class Config:
        from_attributes = True

class AutorisationDocumentCreate(AutorisationDocumentBase):
    pass

class AutorisationDocumentUpdate(BaseModel):
    peut_lire: Optional[bool]
    peut_modifier: Optional[bool]
    peut_supprimer: Optional[bool]
    peut_signer: Optional[bool]

class AutorisationDocumentRead(AutorisationDocumentBase):
    id: int

class AutorisationDocumentSearch(BaseModel):
    document_id: Optional[int]
    utilisateur_id: Optional[int]

class AutorisationDocumentSearchResults(BaseModel):
    results: List[AutorisationDocumentRead]