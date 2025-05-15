from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VersionSystemeBase(BaseModel):
    version: str
    description: Optional[str] = None

class VersionSystemeCreate(VersionSystemeBase):
    pass

class VersionSystemeRead(VersionSystemeBase):
    id: int
    date_appliquee: datetime

    class Config:
        orm_mode = True
