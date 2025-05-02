from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class PlanningEmployeBase(BaseModel):
    utilisateur_id: int
    machine_id: Optional[int]
    date: datetime
    plage_horaire: Optional[str]
    tache: Optional[str]
    statut: str = "Prévu"

class PlanningEmployeCreate(PlanningEmployeBase):
    pass

class PlanningEmployeRead(PlanningEmployeBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        

