from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base

class SimulationChiffrage(Base):
    __tablename__ = "simulations_chiffrage"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    scenario = Column(String(100), nullable=False)
    duree_estimee = Column(Float, nullable=False)
    cout_estime = Column(Float, nullable=False)
    commentaire = Column(Text, nullable=True)
    marge_simulee = Column(Float, default=0.0)
    source = Column(String(100), default="simulation-engine")

    date_simulation = Column(DateTime(timezone=True), server_default=func.now())

    piece = relationship("Piece", back_populates="simulations_chiffrage")
    utilisateur = relationship("Utilisateur", back_populates="simulations_chiffrage")

    def __repr__(self):
        return f"<SimulationChiffrage(scenario='{self.scenario}', cout={self.cout_estime})>"