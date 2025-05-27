from pydantic import BaseModel
from typing import Optional, List

class TagBase(BaseModel):
    nom: str
    description: Optional[str]

    class Config:
        from_attributes = True

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    nom: Optional[str]
    description: Optional[str]

class TagRead(TagBase):
    id: int

class TagSearch(BaseModel):
    nom: Optional[str]

class TagSearchResults(BaseModel):
    results: List[TagRead]