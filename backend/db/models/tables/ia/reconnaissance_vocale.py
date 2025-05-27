from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class ReconnaissanceVocale(Base):
    __tablename__ = "reconnaissances_vocales"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    langue = Column(String(20), nullable=False, default="fr")
    audio_fichier = Column(String(255), nullable=False, comment="Chemin fichier audio")
    transcription = Column(Text, nullable=True)
    intention = Column(String(255), nullable=True)
    resultat_action = Column(Text, nullable=True)
    moteur_utilise = Column(String(100), default="whisper")

    date_reconnaissance = Column(DateTime(timezone=True), server_default=func.now())

    utilisateur = relationship("Utilisateur", back_populates="reconnaissances_vocales")

    def __repr__(self):
        return f"<ReconnaissanceVocale(id={self.id}, utilisateur={self.utilisateur_id}, langue='{self.langue}')>"