from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class Tag(Base):
    __tablename__ = "tags"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    clients = relationship("TagClient", back_populates="tag", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Tag(nom='{self.nom}')>"