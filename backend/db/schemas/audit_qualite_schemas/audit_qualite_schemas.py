from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuditQualiteBase(BaseModel):
    responsable_utilisateur_id: int
    date_audit: datetime
    type_audit: str
    resultat: str
    commentaire: Optional[str] = None

class AuditQualiteCreate(AuditQualiteBase):
    pass

class AuditQualiteUpdate(BaseModel):
    responsable_utilisateur_id: Optional[int] = None
    date_audit: Optional[datetime] = None
    type_audit: Optional[str] = None
    resultat: Optional[str] = None
    commentaire: Optional[str] = None

class AuditQualiteResponse(AuditQualiteBase):
    id: int

    class Config:
        orm_mode = True