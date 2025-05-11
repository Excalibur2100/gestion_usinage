from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from db.models.base import Base

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
        ForeignKey("pieces.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de la pièce associée",
    )

    designation = Column(String(100), nullable=False, comment="Nom ou désignation visible même si pièce supprimée")
    quantite = Column(Integer, nullable=False, comment="Quantité commandée")
    prix_unitaire = Column(Float, nullable=False, comment="Prix unitaire de la pièce")

    commande = relationship("Commande", back_populates="pieces", lazy="joined")
    piece = relationship("Piece", back_populates="commandes", lazy="joined")

    def __repr__(self):
        return f"<CommandePiece commande={self.commande_id} x{self.quantite} - {self.designation}>"
#             comment="Vérification du statut de la commande",
#         ),
#         CheckConstraint(
#             "date_validation >= date_creation",
#             name="check_date_validation",
#             comment="La date de validation doit être postérieure à la date de création",
#         ),
#     )
#