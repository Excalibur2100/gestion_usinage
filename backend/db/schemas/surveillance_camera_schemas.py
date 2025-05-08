from pydantic import BaseModel

# Schéma de base (champs communs)
class SurveillanceCameraBase(BaseModel):
    nom: str
    resolution: str
    emplacement: str

# Schéma pour la création
class SurveillanceCameraCreate(SurveillanceCameraBase):
    pass

# Schéma pour la lecture (avec ID)
class SurveillanceCameraRead(SurveillanceCameraBase):
    id: int

    class Config:
        orm_mode = True
