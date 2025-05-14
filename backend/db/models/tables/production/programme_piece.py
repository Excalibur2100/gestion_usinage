from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class ProgrammePiece(Base):
    __tablename__ = "programme_pieces"

    id = Column(Integer, primary_key=True, index=True, comment="ID unique du programme")

    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Pièce associée"
    )

    nom_programme = Column(String(150), nullable=False, comment="Nom du fichier FAO/CNC")
    fichier_path = Column(String(255), nullable=False, comment="Chemin du fichier généré")

    postprocesseur_id = Column(
        Integer,
        ForeignKey("postprocesseurs.id", ondelete="SET NULL"),
        nullable=False,
        index=True,
        comment="Post-processeur utilisé"
    )

    date_import = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'import")

    # Contraintes uniques
    __table_args__ = (
        UniqueConstraint("piece_id", "nom_programme", name="uq_piece_nom_programme"),
    )

    # Relations
    piece = relationship("Piece", back_populates="programmes", lazy="joined")
    postprocesseur = relationship("PostProcesseur", back_populates="programmes", lazy="joined")
    analyses = relationship("AnalyseFichier", back_populates="programme", cascade="all, delete-orphan", lazy="joined")

    def __repr__(self):
        return (
            f"<ProgrammePiece(id={self.id}, nom_programme='{self.nom_programme}', "
            f"piece_id={self.piece_id}, postprocesseur_id={self.postprocesseur_id}, "
            f"date_import={self.date_import})>"
        )
