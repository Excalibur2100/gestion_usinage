from pydantic import BaseModel
from typing import List, Optional

class TagClientBase(BaseModel):
    client_id: int
    tag_id: int

    class Config:
        from_attributes = True

class TagClientCreate(TagClientBase):
    pass

class TagClientUpdate(BaseModel):
    client_id: Optional[int]
    tag_id: Optional[int]

class TagClientRead(TagClientBase):
    id: int

class TagClientSearch(BaseModel):
    client_id: Optional[int]
    tag_id: Optional[int]

class TagClientSearchResults(BaseModel):
    results: List[TagClientRead]