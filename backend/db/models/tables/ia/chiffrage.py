from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Chiffrage(Base):
    __tablename__ = "chiffrages"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)

    description = Column(Text, nullable=True)
    duree_estimee = Column(Float, nullable=False, comment="Durée estimée en heures")
    cout_estime = Column(Float, nullable=False)
    taux_marge = Column(Float, default=0.0, comment="Marge appliquée (en %)")

    origine = Column(String(100), nullable=False, default="manuel", comment="manuel, automatique, IA")
    nom_version = Column(String(100), nullable=True)
    date_chiffrage = Column(DateTime(timezone=True), server_default=func.now())

    piece = relationship("Piece", back_populates="chiffrages")
    utilisateur = relationship("Utilisateur", back_populates="chiffrages")
    entreprise = relationship("Entreprise", back_populates="chiffrages")
    historiques = relationship("HistoriqueChiffrage", back_populates="chiffrage", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Chiffrage(id={self.id}, piece={self.piece_id}, origine='{self.origine}')>"