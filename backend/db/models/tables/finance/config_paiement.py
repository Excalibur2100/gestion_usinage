from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigPaiement(Base):
    __tablename__ = "config_paiements"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    libelle = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    delai_jours = Column(Integer, nullable=False, default=0)
    actif = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ConfigPaiement(libelle='{self.libelle}', delai={self.delai_jours})>"