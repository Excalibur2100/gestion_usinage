from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class CommandeBase(BaseModel):
    client_id: int = Field(..., description="ID du client associé à la commande")
    statut: str = Field(default="en attente", description="Statut de la commande")
    date_commande: datetime = Field(..., description="Date de la commande")
    bon_commande_client: Optional[str] = Field(None, description="Bon de commande du client")

class CommandeCreate(CommandeBase):
    """
    Schéma pour la création d'une commande.
    """
    pass

class CommandeRead(CommandeBase):
    """
    Schéma pour la lecture d'une commande.
    """
    id: int = Field(..., description="ID unique de la commande")

    class Config:
        from_attributes = True  # Remplace `orm_mode` dans Pydantic v2

class CommandeUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'une commande.
    """
    client_id: Optional[int] = Field(None, description="ID du client associé à la commande")
    statut: Optional[str] = Field(None, description="Statut de la commande")
    date_commande: Optional[datetime] = Field(None, description="Date de la commande")
    bon_commande_client: Optional[str] = Field(None, description="Bon de commande du client")

    class Config:
        from_attributes = True  # Remplace `orm_mode` dans Pydantic v2
        json_schema_extra = {  # Remplace `schema_extra` dans Pydantic v2
            "example": {
                "client_id": 1,
                "statut": "confirmée",
                "date_commande": "2023-10-01T12:00:00Z",
                "bon_commande_client": "BC12345",
            }
        }