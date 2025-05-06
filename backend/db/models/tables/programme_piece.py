from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= PROGRAMME PIECE =========================
class ProgrammePiece(Base):
    __tablename__ = "programme_pieces"

    # Colonnes
    id = Column(Integer, primary_key=True, index=True, comment="Identifiant unique du programme")
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id"),
        nullable=False,
        index=True,
        comment="ID de la pièce associée",
    )
    nom_programme = Column(
        String(150),
        nullable=False,
        comment="Nom du programme",
    )
    fichier_path = Column(
        String(255),
        nullable=False,
        comment="Chemin du fichier sur disque",
    )
    postprocesseur_id = Column(
        Integer,
        ForeignKey("postprocesseurs.id"),
        nullable=False,
        index=True,
        comment="ID du post-processeur associé",
    )
    date_import = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date d'importation du programme",
    )

    # Contraintes
    __table_args__ = (
        UniqueConstraint("piece_id", "nom_programme", name="uq_piece_nom_programme"),
    )

    # Relations
    piece = relationship("Piece", back_populates="programmes")
    postprocesseur = relationship("PostProcesseur", back_populates="programmes")
    analyses = relationship("AnalyseFichier", back_populates="programme")

    # Méthodes utilitaires
    def __repr__(self):
        return (
            f"<ProgrammePiece(id={self.id}, nom_programme='{self.nom_programme}', "
            f"piece_id={self.piece_id}, postprocesseur_id={self.postprocesseur_id}, "
            f"date_import={self.date_import})>"
        )