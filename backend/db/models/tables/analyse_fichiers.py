from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class AnalyseFichier(Base):
    __tablename__ = "analyse_fichiers"

    id = Column(Integer, primary_key=True)

    type_fichier = Column(String(100), nullable=False, comment="Type du fichier analysé (CSV, JSON, XML, etc.)")
    contenu = Column(Text, nullable=False, comment="Contenu brut ou transformé du fichier")
    date_analyse = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de l'analyse")

    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    programme_id = Column(Integer, ForeignKey("programme_pieces.id", ondelete="SET NULL"), nullable=True)

    # Relations
    machine = relationship("Machine", back_populates="analyses", lazy="joined")
    piece = relationship("Piece", back_populates="analyses", lazy="joined")
    programme = relationship("ProgrammePiece", back_populates="analyses", lazy="joined")

    def __repr__(self):
        return f"<AnalyseFichier type={self.type_fichier} date={self.date_analyse}>"
