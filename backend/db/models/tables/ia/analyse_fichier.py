from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class AnalyseFichier(Base):
    __tablename__ = "analyses_fichiers"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    nom_fichier = Column(String(255), nullable=False)
    type_fichier = Column(String(50), nullable=False, comment="csv, dxf, step, etc.")
    resultat_analyse = Column(Text, nullable=True)
    chemin_fichier = Column(Text, nullable=False)

    date_analyse = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    piece = relationship("Piece", back_populates="analyses")
    utilisateur = relationship("Utilisateur", back_populates="analyses_fichiers")

    def __repr__(self):
        return f"<AnalyseFichier(piece_id={self.piece_id}, fichier='{self.nom_fichier}')>"