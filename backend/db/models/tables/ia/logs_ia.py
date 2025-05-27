from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base

class LogIA(Base):
    __tablename__ = "logs_ia"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    module = Column(String(100), nullable=False, comment="Nom du module ou fonction IA")
    action = Column(String(100), nullable=False)
    resultat = Column(Text, nullable=True)
    niveau = Column(String(50), default="INFO")
    statut = Column(String(50), default="ok")
    commentaire = Column(Text, nullable=True)

    date_log = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="logs_ia")

    def __repr__(self):
        return f"<LogIA(module='{self.module}', action='{self.action}', niveau='{self.niveau}')>"