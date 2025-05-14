from pydantic import BaseModel, Field
from datetime import datetime

class LogsSecuriteBase(BaseModel):
    evenement: str = Field(..., description="Type d'événement de sécurité")
    description: str = Field(None, description="Description détaillée de l'événement")
    niveau: str = Field(..., description="Niveau de l'événement (INFO, WARNING, ERROR)")

class LogsSecuriteCreate(LogsSecuriteBase):
    pass

class LogsSecuriteRead(LogsSecuriteBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True