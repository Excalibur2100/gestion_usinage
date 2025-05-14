from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class ControlePiece(Base):
    __tablename__ = "controle_piece"

    id = Column(Integer, primary_key=True)

    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="CASCADE"), nullable=False, comment="Pièce contrôlée")
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id", ondelete="SET NULL"), nullable=True, comment="Instrument utilisé")
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True, comment="Contrôleur")

    resultat = Column(String(100), nullable=False, comment="Résultat du contrôle : conforme, non conforme")
    date_controle = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date du contrôle")
    remarque = Column(Text, nullable=True, comment="Remarques ou observations")
    critere = Column(String(100), nullable=True, comment="Critère contrôlé : dimension, apparence, etc.")

    # Relations
    piece = relationship("Piece", back_populates="controles", lazy="joined")
    instrument = relationship("InstrumentControle", back_populates="controles", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="controles_piece", lazy="joined")

    # Contraintes
    __table_args__ = (
        CheckConstraint(
            "resultat IN ('conforme', 'non conforme')",
            name="check_resultat_controle_piece",
        ),
    )

    def __repr__(self):
        return f"<ControlePiece piece={self.piece_id} result={self.resultat}>"
