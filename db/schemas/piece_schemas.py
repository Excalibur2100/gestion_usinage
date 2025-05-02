from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, Field 

class PieceBase(BaseModel):
    nom: str
    numero_plan: str
    description: Optional[str]

class PieceCreate(PieceBase):
    pass

class PieceRead(PieceBase):
    id: int

    
    model_config = ConfigDict(from_attributes=True)


class PieceUsinage(BaseModel):
    longueur: float
    largeur: float
    hauteur: float
    materiau: str
    operations: List[str]
    outils: List[str]
    outils_disponibles: List[str]  # Ajout de ce champ
    machines_disponibles: List[str]  # Ajout de ce champ

    model_config = ConfigDict(from_attributes=True)
        

