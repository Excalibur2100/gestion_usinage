from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Text, String, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= PLANNING MACHINE =========================
class PlanningMachine(Base):
    __tablename__ = "planning_machines"

    id = Column(Integer, primary_key=True)
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=False,
        comment="ID de la machine associée",
    )
    date_debut = Column(
        DateTime, nullable=False, comment="Date de début de l'opération"
    )
    date_fin = Column(DateTime, nullable=False, comment="Date de fin de l'opération")
    operation = Column(Text, nullable=False, comment="Description de l'opération")
    statut = Column(
        String(50),
        default="Prévu",
        nullable=False,
        comment="Statut de l'opération (Prévu, En cours, Terminé)",
    )
    charge_estimee = Column(
        Float, nullable=True, comment="Charge estimée pour l'opération (en heures)"
    )
    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id"),
        nullable=True,
        comment="ID de la gamme de production associée",
    )
    optimise_par_ia = Column(
        Boolean, default=False, comment="Indique si l'opération est optimisée par IA"
    )

    machine = relationship("Machine", back_populates="plannings")
    gamme = relationship("GammeProduction", back_populates="plannings")
