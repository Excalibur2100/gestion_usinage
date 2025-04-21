from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= PROGRAMME PIECE =========================
class ProgrammePiece(Base):
    __tablename__ = "programme_pieces"

    id = Column(Integer, primary_key=True)
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id"),
        nullable=False,
        comment="ID de la pièce associée",
    )
    nom_programme = Column(String(150), nullable=False, comment="Nom du programme")
    fichier_path = Column(
        String(255), nullable=False, comment="Chemin du fichier sur disque"
    )
    postprocesseur_id = Column(
        Integer,
        ForeignKey("postprocesseurs.id"),
        nullable=False,
        comment="ID du post-processeur associé",
    )
    date_import = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date d'importation du programme",
    )

    # Relations
    piece = relationship("Piece", back_populates="programmes")
    postprocesseur = relationship("PostProcesseur", back_populates="programmes")
    analyses = relationship("AnalyseFichier", back_populates="programme")
