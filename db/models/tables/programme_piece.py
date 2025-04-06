from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= PROGRAMME PIECE =========================
class ProgrammePiece(Base):
    __tablename__ = "programmes_piece"
    id = Column(Integer, primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    nom_programme = Column(String(150))
    fichier_path = Column(String(255))  # Chemin du fichier sur disque
    postprocesseur_id = Column(Integer, ForeignKey("postprocesseurs.id"))
    date_import = Column(DateTime, default=datetime.utcnow)

    piece = relationship("Piece", back_populates="programmes")
    postprocesseur = relationship("PostProcesseur", back_populates="programmes")