from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class ActionCommerciale(Base):
    __tablename__ = "actions_commerciales"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    type_action = Column(String(100), nullable=False, comment="Appel, visite, email...")
    date_action = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    resultat = Column(String(100), nullable=True)
    commentaire = Column(Text, nullable=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    campagne_id = Column(Integer, ForeignKey("campagnes_commerciales.id", ondelete="SET NULL"), nullable=True)



    # Relations
    client = relationship("Client", back_populates="actions_commerciales")
    utilisateur = relationship("Utilisateur", back_populates="actions_commerciales")
    campagne = relationship("CampagneCommerciale", back_populates="actions")

    def __repr__(self):
        return f"<ActionCommerciale(type='{self.type_action}', client={self.client_id})>"
