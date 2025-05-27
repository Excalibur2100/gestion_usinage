from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigLangue(Base):
    __tablename__ = "config_langues"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True, nullable=False, comment="Code ISO ex: fr, en, de")
    libelle = Column(String(100), nullable=False, comment="Nom de la langue ex: Français, Anglais")
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ConfigLangue({self.code} - {self.libelle})>"