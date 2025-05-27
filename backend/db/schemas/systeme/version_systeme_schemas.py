from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from db.models.base import Base

class VersionSysteme(Base):
    __tablename__ = "version_systeme"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(String(20), nullable=False, unique=True, comment="Numéro de version ex: 1.0.0")
    description = Column(Text, nullable=True, comment="Résumé des changements")
    date_appliquee = Column(DateTime(timezone=True), server_default=func.now(), comment="Date d'application")
