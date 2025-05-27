from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# MACHINE
class ChiffrageMachineBase(BaseModel):
    nom: str
    type_machine: Optional[str]
    cout_horaire: float

    class Config:
        from_attributes = True

class ChiffrageMachineCreate(ChiffrageMachineBase): pass
class ChiffrageMachineUpdate(BaseModel):
    nom: Optional[str]
    type_machine: Optional[str]
    cout_horaire: Optional[float]

class ChiffrageMachineRead(ChiffrageMachineBase):
    id: int

# OPÉRATION
class ChiffrageOperationBase(BaseModel):
    nom: str
    temps_minute: float
    outil_utilise: Optional[str]
    machine_id: Optional[int]

    class Config:
        from_attributes = True

class ChiffrageOperationCreate(ChiffrageOperationBase): pass
class ChiffrageOperationUpdate(BaseModel):
    nom: Optional[str]
    temps_minute: Optional[float]
    outil_utilise: Optional[str]
    machine_id: Optional[int]

class ChiffrageOperationRead(ChiffrageOperationBase):
    id: int
    machine: Optional[ChiffrageMachineRead]

# PIÈCE
class ChiffragePieceBase(BaseModel):
    nom: str
    matière: str
    poids_kg: Optional[float]
    volume_cm3: Optional[float]
    quantite: int = 1
    client_id: Optional[int]

    class Config:
        from_attributes = True

class ChiffragePieceCreate(ChiffragePieceBase): pass
class ChiffragePieceUpdate(BaseModel):
    nom: Optional[str]
    matière: Optional[str]
    poids_kg: Optional[float]
    volume_cm3: Optional[float]
    quantite: Optional[int]
    client_id: Optional[int]

class ChiffragePieceRead(ChiffragePieceBase):
    id: int
    operations: List[ChiffrageOperationRead]