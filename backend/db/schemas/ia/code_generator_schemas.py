from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CodeGeneratorBase(BaseModel):
    utilisateur_id: Optional[int]
    entreprise_id: Optional[int]
    nom_session: str
    langage: str
    prompt: str
    code_genere: Optional[str]
    version_modele: Optional[str] = "gpt-4"

    class Config:
        from_attributes = True

class CodeGeneratorCreate(CodeGeneratorBase):
    pass

class CodeGeneratorUpdate(BaseModel):
    langage: Optional[str]
    prompt: Optional[str]
    code_genere: Optional[str]
    version_modele: Optional[str]
    nom_session: Optional[str]

class CodeGeneratorRead(CodeGeneratorBase):
    id: int
    date_generation: datetime

class CodeGeneratorSearch(BaseModel):
    utilisateur_id: Optional[int]
    langage: Optional[str]
    nom_session: Optional[str]

class CodeGeneratorSearchResults(BaseModel):
    results: List[CodeGeneratorRead]