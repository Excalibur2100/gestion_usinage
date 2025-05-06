from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field 

class PlanningMachineBase(BaseModel):
    machine_id: int
    date: datetime
    plage_horaire: str
    tache: Optional[str]

class PlanningMachineCreate(PlanningMachineBase):
    pass

class PlanningMachineRead(PlanningMachineBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        


