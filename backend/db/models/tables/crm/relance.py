from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Relance(Base):
    __tablename__ = "relances"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)
    objet = Column(String(100), nullable=False)
    message = Column(Text, nullable=True)
    canal = Column(String(50), nullable=False, comment="email, téléphone, courrier...")
    statut = Column(String(50), default="en attente", comment="en attente, faite, annulée")
    date_relance = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    client = relationship("Client", back_populates="relances")
    entreprise = relationship("Entreprise", back_populates="relances_client")

    def __repr__(self):
        return f"<Relance(client={self.client_id}, objet='{self.objet}', statut='{self.statut}')>"