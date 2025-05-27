from pydantic import BaseModel
from typing import Optional, List

class ConfigNotificationBase(BaseModel):
    evenement: str
    canal: str
    actif: Optional[bool] = True
    description: Optional[str]

    class Config:
        from_attributes = True

class ConfigNotificationCreate(ConfigNotificationBase):
    pass

class ConfigNotificationUpdate(BaseModel):
    evenement: Optional[str]
    canal: Optional[str]
    actif: Optional[bool]
    description: Optional[str]

class ConfigNotificationRead(ConfigNotificationBase):
    id: int

class ConfigNotificationSearch(BaseModel):
    evenement: Optional[str]
    canal: Optional[str]
    actif: Optional[bool]

class ConfigNotificationSearchResults(BaseModel):
    results: List[ConfigNotificationRead]