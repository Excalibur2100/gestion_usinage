from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class HistoriquePrixClient(Base):
    __tablename__ = "historique_prix_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="CASCADE"), nullable=False)

    prix_unitaire = Column(Float, nullable=False)
    date_enregistrement = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relations
    client = relationship("Client", back_populates="historique_prix")
    piece = relationship("Piece", back_populates="historique_prix")

    def __repr__(self):
        return f"<HistoriquePrixClient(client={self.client_id}, piece={self.piece_id}, prix={self.prix_unitaire})>"
