from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class AnalyseFichier(Base):
    __tablename__ = "analyses_fichiers"

    id = Column(Integer, primary_key=True)
    type_fichier = Column(String(100), nullable=False)
    contenu = Column(Text, nullable=False)
    date_analyse = Column(DateTime, default=datetime.utcnow, nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    programme_id = Column(Integer, ForeignKey("programme_pieces.id", ondelete="SET NULL"), nullable=True)
    commentaire = Column(Text, nullable=True)
    statut = Column(String(50), default="en attente", nullable=False, comment="Statut : en attente, validée, refusée")
    date_modif = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)
    date_ajout = Column(DateTime, default=datetime.utcnow, nullable=False)
    # Foreign keys
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    programme_id = Column(Integer, ForeignKey("programme_pieces.id", ondelete="SET NULL"), nullable=True)
    # Relationships

    machine = relationship("Machine", back_populates="analyses", lazy="joined")
    piece = relationship("Piece", back_populates="analyses", lazy="joined")
    programme = relationship("ProgrammePiece", back_populates="analyses", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="analyses", lazy="joined")

    def __repr__(self):
        return f"<AnalyseFichier type={self.type_fichier} programme_id={self.programme_id} utilisateur_id={self.utilisateur.id}>"
    
