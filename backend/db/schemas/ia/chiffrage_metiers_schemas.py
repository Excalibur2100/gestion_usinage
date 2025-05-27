from pydantic import BaseModel, Field

class ChiffrageSimpleRequest(BaseModel):
    cout_unitaire: float = Field(gt=0)
    temps_h: float = Field(gt=0)
    marge: float = Field(default=0.0, ge=0, le=100)

class ChiffrageCompletRequest(BaseModel):
    nb_operations: int = Field(gt=0)
    temps_moyen_op: float = Field(gt=0)
    cout_horaire: float = Field(gt=0)
    marge: float = Field(default=0.0, ge=0, le=100)
    description: str = Field(default="Sans description")

class ChiffrageIntelligentRequest(BaseModel):
    piece_id: int = Field(..., description="ID de la pièce à chiffrer")
    marge: float = Field(default=15.0, ge=0, le=100)