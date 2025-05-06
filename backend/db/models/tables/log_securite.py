from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from db.models.base import Base

class LogsSecurite(Base):
    __tablename__ = "logs_securite"

    id = Column(Integer, primary_key=True, index=True)
    evenement = Column(String(100), nullable=False, comment="Type d'événement de sécurité")
    description = Column(Text, nullable=True, comment="Description détaillée de l'événement")
    niveau = Column(String(50), nullable=False, default="INFO", comment="Niveau de l'événement (INFO, WARNING, ERROR)")
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date et heure de l'événement")

    def __repr__(self):
        return f"<LogsSecurite(id={self.id}, evenement={self.evenement}, niveau={self.niveau}, timestamp={self.timestamp})>"