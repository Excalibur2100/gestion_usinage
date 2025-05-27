from pydantic import BaseModel
from typing import Optional, List

class SegmentClientBase(BaseModel):
    libelle: str
    description: Optional[str]

    class Config:
        from_attributes = True

class SegmentClientCreate(SegmentClientBase):
    pass

class SegmentClientUpdate(BaseModel):
    libelle: Optional[str]
    description: Optional[str]

class SegmentClientRead(SegmentClientBase):
    id: int

class SegmentClientSearch(BaseModel):
    libelle: Optional[str]

class SegmentClientSearchResults(BaseModel):
    results: List[SegmentClientRead]
