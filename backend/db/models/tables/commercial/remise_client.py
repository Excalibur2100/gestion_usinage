from sqlalchemy import Column, Integer, Float, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class RemiseClient(Base):
    __tablename__ = "remises_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)

    pourcentage = Column(Float, nullable=False, comment="Ex: 5.0 pour 5%")
    type_remise = Column(String(50), default="globale", comment="globale / produit / temporaire")
    description = Column(Text, nullable=True)

    date_debut = Column(DateTime(timezone=True), nullable=True)
    date_fin = Column(DateTime(timezone=True), nullable=True)
    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relations
    client = relationship("Client", back_populates="remises")
    piece = relationship("Piece", back_populates="remises_client")

    def __repr__(self):
        return f"<RemiseClient(client={self.client_id}, {self.pourcentage}%)>"
