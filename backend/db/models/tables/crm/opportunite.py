from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Opportunite(Base):
    __tablename__ = "opportunites"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)


    titre = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    montant_potentiel = Column(Float, nullable=True)
    probabilite = Column(Float, default=0.0, comment="Pourcentage de succès (ex: 0.6 = 60%)")
    statut = Column(String(50), nullable=False, default="ouverte", comment="ouverte, gagnée, perdue")
    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    client = relationship("Client", back_populates="opportunites")
    entreprise = relationship("Entreprise", back_populates="opportunites")

    def __repr__(self):
        return f"<Opportunite(client={self.client_id}, titre='{self.titre}', statut='{self.statut}')>"