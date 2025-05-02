from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class CommandePieceBase(BaseModel):
    commande_id: int = Field(..., description="ID de la commande associée")
    piece_id: int = Field(..., description="ID de la pièce associée")
    quantite: int = Field(..., description="Quantité de pièces commandées")
    date_livraison: Optional[datetime] = Field(None, description="Date prévue de livraison")

class CommandePieceCreate(CommandePieceBase):
    """
    Schéma pour la création d'une commande pièce.
    """
    pass

class CommandePieceRead(CommandePieceBase):
    """
    Schéma pour la lecture d'une commande pièce.
    """
    id: int = Field(..., description="ID unique de la commande pièce")

    class Config:
        from_attributes = True  # Remplace `orm_mode` dans Pydantic v2

class CommandePieceUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'une commande pièce.
    """
    commande_id: Optional[int] = Field(None, description="ID de la commande associée")
    piece_id: Optional[int] = Field(None, description="ID de la pièce associée")
    quantite: Optional[int] = Field(None, description="Quantité de pièces commandées")
    date_livraison: Optional[datetime] = Field(None, description="Date prévue de livraison")

    class Config:
        from_attributes = True  # Remplace `orm_mode` dans Pydantic v2
        json_schema_extra = {  # Remplace `schema_extra` dans Pydantic v2
            "example": {
                "commande_id": 1,
                "piece_id": 2,
                "quantite": 10,
                "date_livraison": "2023-10-15T12:00:00Z",
            }
        }