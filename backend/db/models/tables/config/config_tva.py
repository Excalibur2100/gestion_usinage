from sqlalchemy import Column, Integer, Float, String, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigTVA(Base):
    __tablename__ = "config_tva"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False, comment="TVA standard, réduite, export...")
    taux = Column(Float, nullable=False, comment="Ex: 20.0 pour 20%")
    pays = Column(String(50), nullable=True)
    actif = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ConfigTVA({self.nom} - {self.taux}%)>"