from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class DroitBase(BaseModel):
    module: str
    autorisation: bool = False

class DroitCreate(DroitBase):
    utilisateur_id: int

class DroitRead(DroitBase):
    id: int
    utilisateur_id: int

    
    model_config = ConfigDict(from_attributes=True)
        

