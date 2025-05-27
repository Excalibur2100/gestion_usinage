from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigNotification(Base):
    __tablename__ = "config_notifications"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    evenement = Column(String(100), unique=True, nullable=False, comment="Nom de l'événement déclencheur")
    canal = Column(String(50), nullable=False, comment="email, sms, interne, webhook, etc.")
    actif = Column(Boolean, default=True)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f"<ConfigNotification(evenement='{self.evenement}', canal='{self.canal}')>"