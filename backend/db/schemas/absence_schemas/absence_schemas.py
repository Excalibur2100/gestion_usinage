from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AbsenceBase(BaseModel):
    utilisateur_id: int
    date_debut: datetime
    date_fin: datetime
    type_absence: str
    commentaire: Optional[str] = None

class AbsenceCreate(AbsenceBase):
    pass

class AbsenceUpdate(BaseModel):
    date_debut: Optional[datetime] = None
    date_fin: Optional[datetime] = None
    type_absence: Optional[str] = None
    commentaire: Optional[str] = None

class AbsenceResponse(AbsenceBase):
    id: int

    class Config:
        orm_mode = True