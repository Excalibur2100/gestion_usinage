from sqlalchemy import Column, Integer, String, ForeignKey, Float, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class GammeProduction(Base):
    __tablename__ = "gammes_production"

    id = Column(Integer, primary_key=True)

    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        comment="Pièce concernée par l'opération"
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="SET NULL"),
        nullable=True,
        comment="Machine utilisée"
    )

    materiau_id = Column(Integer, ForeignKey("materiaux.id", ondelete="SET NULL"))
    operation = Column(String(100), nullable=False, comment="Nom de l'opération")
    ordre = Column(Integer, nullable=True, comment="Ordre de l'opération dans la gamme")
    temps_estime = Column(Float, nullable=False, comment="Durée estimée (en heures)")
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="CASCADE"))
    temps_reel = Column(Float, nullable=True, comment="Durée réelle (en heures)")
    temps_reel_ia = Column(Float, nullable=True, comment="Durée réelle estimée par IA (en heures)")
    temps_reel_ia_optimise = Column(Float, nullable=True, comment="Durée réelle optimisée par IA (en heures)")
    pointages = relationship("Pointage", back_populates="gamme", cascade="all, delete-orphan")
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    utilisateur = relationship("Utilisateur", back_populates="gammes", lazy="joined")

    

    piece = relationship("Piece", back_populates="gammes", lazy="joined")
    machine = relationship("Machine", back_populates="gammes", lazy="joined")
    materiau = relationship("Materiau", back_populates="gammes")
    plannings = relationship("PlanningMachine", back_populates="gamme", cascade="all, delete-orphan", lazy="joined")
    tracabilites = relationship("Tracabilite", back_populates="gamme", cascade="all, delete-orphan")



    __table_args__ = (
        CheckConstraint("temps_estime >= 0", name="check_temps_estime_gamme"),
    )

    def __repr__(self):
        return f"<GammeProduction piece={self.piece_id} op={self.operation} t={self.temps_estime}h>"
    
