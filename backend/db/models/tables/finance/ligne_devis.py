from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class LigneDevis(Base):
    __tablename__ = "lignes_devis"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    devis_id = Column(Integer, ForeignKey("devis.id", ondelete="CASCADE"), nullable=False)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)

    designation = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    quantite = Column(Integer, nullable=False, default=1)
    prix_unitaire = Column(Float, nullable=False)
    remise = Column(Float, nullable=True, default=0.0)

    devis = relationship("Devis", back_populates="lignes")
    piece = relationship("Piece", back_populates="lignes_devis")

    def __repr__(self):
        return f"<LigneDevis(devis={self.devis_id}, designation='{self.designation}')>"