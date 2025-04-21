from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= ANALYSE FICHIERS =========================
class AnalyseFichier(Base):
    __tablename__ = "analyse_fichiers"

    id = Column(Integer, primary_key=True)
    type_fichier = Column(
        String(100),
        nullable=False,
        comment="Type du fichier analysé (ex: CSV, JSON, XML)",
    )
    contenu = Column(
        Text,
        nullable=False,
        comment="Contenu brut ou résultat de l'analyse du fichier",
    )
    date_analyse = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de l'analyse",
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de la machine associée (si applicable)",
    )
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de la pièce associée (si applicable)",
    )
    programme_id = Column(
        Integer,
        ForeignKey("programme_pieces.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID du programme associé (si applicable)",
    )

    # Relations
    machine = relationship("Machine", back_populates="analyses")
    piece = relationship("Piece", back_populates="analyses")
    programme = relationship("ProgrammePiece", back_populates="analyses")
