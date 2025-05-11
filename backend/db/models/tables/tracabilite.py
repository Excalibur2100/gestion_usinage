from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Tracabilite(Base):
    __tablename__ = "tracabilite"

    id = Column(Integer, primary_key=True)

    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        comment="Pièce concernée"
    )

    operation = Column(String(255), nullable=False, comment="Opération effectuée")
    
    date_operation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de l'action tracée"
    )

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Utilisateur ayant réalisé l'opération"
    )

    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id", ondelete="SET NULL"),
        nullable=True,
        comment="Gamme utilisée si applicable"
    )

    remarque = Column(Text, nullable=True, comment="Commentaires ou observations")

    # Relations
    piece = relationship("Piece", back_populates="tracabilites", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="tracabilites", lazy="joined")
    gamme = relationship("GammeProduction", back_populates="tracabilites", lazy="joined")
    gamme = relationship("GammeProduction", back_populates="tracabilites", lazy="joined")


    def __repr__(self):
        return f"<Tracabilite piece={self.piece_id} operation='{self.operation}' date={self.date_operation}>"
