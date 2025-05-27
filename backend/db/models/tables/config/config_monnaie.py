from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigMonnaie(Base):
    __tablename__ = "config_monnaies"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True, nullable=False, comment="Ex: EUR, USD")
    libelle = Column(String(100), nullable=False, comment="Ex: Euro, Dollar")
    symbole = Column(String(10), nullable=False, comment="Ex: €, $")
    taux_conversion = Column(Float, default=1.0, comment="Taux par rapport à la devise par défaut")
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ConfigMonnaie(code={self.code}, symbole={self.symbole})>"