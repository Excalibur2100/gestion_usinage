from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base

class AssistantIA(Base):
    __tablename__ = "assistants_ia"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)

    nom_session = Column(String(100), nullable=False)
    prompt = Column(Text, nullable=False)
    reponse = Column(Text, nullable=True)
    moteur = Column(String(100), default="gpt-4")
    temperature = Column(String(10), default="0.7")

    date_session = Column(DateTime(timezone=True), server_default=func.now())

    utilisateur = relationship("Utilisateur", back_populates="assistants_ia")
    entreprise = relationship("Entreprise", back_populates="assistants_ia")

    def __repr__(self):
        return f"<AssistantIA(session='{self.nom_session}', utilisateur={self.utilisateur_id})>"