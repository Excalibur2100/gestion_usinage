from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigMetier(Base):
    __tablename__ = "config_metiers"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    actif = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ConfigMetier(nom='{self.nom}')>"