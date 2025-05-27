from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class SuggestionOutil(Base):
    __tablename__ = "suggestions_outils"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="CASCADE"), nullable=False, index=True)
    outil_id = Column(Integer, ForeignKey("outils.id", ondelete="SET NULL"), nullable=True, index=True)

    programme_id = Column(Integer, ForeignKey("programmes_pieces.id", ondelete="SET NULL"), nullable=True)
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    log_ia_id = Column(Integer, ForeignKey("logs_ia.id", ondelete="SET NULL"), nullable=True)

    score = Column(Float, nullable=True, comment="Score de pertinence de la suggestion")
    commentaire = Column(Text, nullable=True, comment="Justification IA ou métier")

    valide_par_humain = Column(Boolean, default=False)
    decision_commentaire = Column(Text, nullable=True)
    date_validation = Column(DateTime, nullable=True)

    date_suggestion = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relations
    piece = relationship("Piece", back_populates="suggestions_ia", lazy="joined")
    outil = relationship("Outil", back_populates="suggestions_ia", lazy="joined")

    programme = relationship("ProgrammePiece", lazy="joined")  # à créer si pas encore existant
    machine = relationship("Machine", lazy="joined")  # idem
    log_ia = relationship("LogIA", lazy="joined")  # à synchroniser