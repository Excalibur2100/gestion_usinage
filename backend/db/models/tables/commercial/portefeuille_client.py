from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class PortefeuilleClient(Base):
    __tablename__ = "portefeuille_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)

    commentaire = Column(Text, nullable=True)
    date_attribution = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    client = relationship("Client", back_populates="portefeuilles")
    utilisateur = relationship("Utilisateur", back_populates="portefeuilles_clients")

    def __repr__(self):
        return f"<PortefeuilleClient(client={self.client_id}, utilisateur={self.utilisateur_id})>"
