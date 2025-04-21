from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= CONTRÔLE PIECE =========================
class ControlePiece(Base):
    __tablename__ = "controle_piece"

    id = Column(Integer, primary_key=True)
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la pièce contrôlée",
    )
    instrument_id = Column(
        Integer,
        ForeignKey("instruments_controle.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de l'instrument utilisé pour le contrôle",
    )
    resultat = Column(
        String(100),
        nullable=False,
        comment="Résultat du contrôle (ex: conforme, non conforme)",
    )
    date_controle = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date et heure du contrôle",
    )
    remarque = Column(
        Text,
        nullable=True,
        comment="Remarques ou observations sur le contrôle",
    )

    # Relations
    piece = relationship("Piece", back_populates="controles")
    instrument = relationship("InstrumentControle", back_populates="controles")

    # Contraintes
    __table_args__ = (
        CheckConstraint(
            "resultat IN ('conforme', 'non conforme')",
            name="check_resultat_controle_piece",
        ),
    )
