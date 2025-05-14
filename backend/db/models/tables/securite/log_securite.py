from sqlalchemy import Column, Integer, String, DateTime, Text, CheckConstraint, Index
from datetime import datetime
from db.models.base import Base

class LogsSecurite(Base):
    __tablename__ = "logs_securite"

    id = Column(Integer, primary_key=True, index=True)

    evenement = Column(String(100), nullable=False, comment="Type d'événement de sécurité")
    description = Column(Text, nullable=True, comment="Description complète de l'événement")
    niveau = Column(String(50), nullable=False, default="INFO", comment="Niveau : INFO, WARNING, ERROR, CRITICAL")
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Horodatage de l'événement")

    __table_args__ = (
        CheckConstraint("niveau IN ('INFO', 'WARNING', 'ERROR', 'CRITICAL')", name="check_niveau_logs_securite"),
        Index("idx_niveau", "niveau"),
        Index("idx_timestamp", "timestamp"),
    )

    def __repr__(self):
        return f"<LogsSecurite id={self.id} evenement={self.evenement} niveau={self.niveau} timestamp={self.timestamp}>"
