from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from db.models.base import Base

class CommandePiece(Base):
    __tablename__ = "commande_pieces"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    commande_id = Column(
        Integer,
        ForeignKey("commandes.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la commande associée",
    )
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de la pièce associée",
    )

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)  
    
    designation = Column(String(100), nullable=False, comment="Nom ou désignation même si pièce supprimée")
    quantite = Column(Integer, nullable=False, comment="Quantité commandée")
    prix_unitaire = Column(Float, nullable=False, comment="Prix unitaire de la pièce")

    commande = relationship("Commande", back_populates="pieces")
    piece = relationship("Piece", back_populates="commandes")
    entreprise = relationship("Entreprise", back_populates="commande_pieces")

    def __repr__(self):
        return f"<CommandePiece commande={self.commande_id} x{self.quantite} - {self.designation}>"
