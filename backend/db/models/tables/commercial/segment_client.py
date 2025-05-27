from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class SegmentClient(Base):
    __tablename__ = "segments_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    libelle = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    clients = relationship("Client", back_populates="segment")

    def __repr__(self):
        return f"<SegmentClient(libelle='{self.libelle}')>"
