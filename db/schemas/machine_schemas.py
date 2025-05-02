from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class MachineBase(BaseModel):
    nom: str
    type: str
    vitesse_max: Optional[float]
    puissance: Optional[float]

class MachineCreate(MachineBase):
    pass

