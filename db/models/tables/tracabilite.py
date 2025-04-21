from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= TRACABILITE =========================
class Tracabilite(Base):
    __tablename__ = "tracabilite"

    id = Column(Integer, primary_key=True)
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la pièce tracée",
    )
    operation = Column(
        String(255), nullable=False, comment="Opération effectuée sur la pièce"
    )
    date_operation = Column(
        DateTime, default=datetime.utcnow, nullable=False, comment="Date de l'opération"
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de l'utilisateur ayant effectué l'opération",
    )
    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id"),
        nullable=True,
        comment="ID de la gamme de production",
    )

    date = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=True,
        comment="Date de l'enregistrement",
    )

    remarque = Column(Text, comment="Remarque associée à l'enregistrement")

    # Relations
    piece = relationship("Piece", back_populates="tracabilites")
    utilisateur = relationship("Utilisateur", back_populates="tracabilites")
