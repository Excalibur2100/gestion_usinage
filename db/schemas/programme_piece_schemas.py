from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class ProgrammePieceBase(BaseModel):
    piece_id: int
    nom_programme: str
    fichier_path: str
    postprocesseur_id: Optional[int]
    date_import: datetime

class ProgrammePieceCreate(ProgrammePieceBase):
    pass

class ProgrammePieceRead(ProgrammePieceBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)
        

class CommandePieceCreate(BaseModel):
    nom: str
    description: str

class CommandePieceRead(BaseModel):
    id: int
    nom: str
    description: str

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2

class GestionAccesCreate(BaseModel):
    utilisateur_id: int
    role: str

class GestionAccesRead(BaseModel):
    id: int
    utilisateur_id: int
    role: str

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2

class PlanningMachineCreate(BaseModel):
    debut: datetime
    fin: datetime
    machine_id: int

class PlanningMachineRead(BaseModel):
    id: int
    debut: datetime
    fin: datetime
    machine_id: int

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2

class GestionFiltrageCreate(BaseModel):
    filtre: str
    valeur: str

class GestionFiltrageRead(BaseModel):
    id: int
    filtre: str
    valeur: str

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2
        
class ChargeMachineCreate(BaseModel):
    machine_id: int
    charge: float
    date: datetime

class ChargeMachineRead(BaseModel):
    id: int
    machine_id: int
    charge: float
    date: datetime

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2

class SurveillanceCameraCreate(BaseModel):
    camera_id: int
    emplacement: str
    statut: str

class SurveillanceCameraRead(BaseModel):
    id: int
    camera_id: int
    emplacement: str
    statut: str

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2

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

class MachineRead(BaseModel):
    id: int
    nom: str

    
    model_config = ConfigDict(from_attributes=True)


