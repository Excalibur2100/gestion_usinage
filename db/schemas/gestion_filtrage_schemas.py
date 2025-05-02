from pydantic import BaseModel, ConfigDict, Field 

class GestionFiltrageCreate(BaseModel):
    filtre: str
    valeur: str

class GestionFiltrageRead(BaseModel):
    id: int
    filtre: str
    valeur: str

    
    model_config = ConfigDict(from_attributes=True)  # Remplace `orm_mode` dans Pydantic v2