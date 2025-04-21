from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= COMMANDE PIECE =========================
class CommandePiece(Base):
    __tablename__ = "commande_pieces"

    id = Column(Integer, primary_key=True)
    commande_id = Column(
        Integer,
        ForeignKey("commandes.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la commande associée",
    )
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la pièce associée",
    )
    quantite = Column(Integer, nullable=False, comment="Quantité commandée")
    prix_unitaire = Column(Float, nullable=False, comment="Prix unitaire de la pièce")

    # Relations
    commande = relationship("Commande", back_populates="pieces")
    piece = relationship("Piece", back_populates="commandes")
