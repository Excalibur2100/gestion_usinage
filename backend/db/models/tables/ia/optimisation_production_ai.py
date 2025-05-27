from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base

class OptimisationProductionAI(Base):
    __tablename__ = "optimisations_production_ai"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)

    nom = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    recommandation = Column(Text, nullable=True)
    gain_estime = Column(String(50), nullable=True, comment="Gain estimé (temps, coût, efficacité)")
    source_ia = Column(String(50), default="gpt-4")

    date_optimisation = Column(DateTime(timezone=True), server_default=func.now())

    utilisateur = relationship("Utilisateur", back_populates="optimisations_ai")
    machine = relationship("Machine", back_populates="optimisations_ai")
    piece = relationship("Piece", back_populates="optimisations_ai")

    def __repr__(self):
        return f"<OptimisationAI(nom='{self.nom}', gain='{self.gain_estime}')>"