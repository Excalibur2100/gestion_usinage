from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class ControleRobotCreate(BaseModel):
    robot_id: int
    action: str
    statut: str

class ControleRobotRead(BaseModel):
    id: int
    robot_id: int
    action: str
    statut: str

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2