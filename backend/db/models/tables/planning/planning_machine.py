from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Text, String, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class PlanningMachine(Base):
    __tablename__ = "planning_machines"

    id = Column(Integer, primary_key=True)

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        comment="Machine concernée"
    )

    date_debut = Column(DateTime, nullable=False, comment="Début de l'opération")
    date_fin = Column(DateTime, nullable=False, comment="Fin de l'opération")
    operation = Column(Text, nullable=False, comment="Opération planifiée")

    statut = Column(
        String(50),
        default="Prévu",
        nullable=False,
        comment="Statut : Prévu, En cours, Terminé"
    )

    charge_estimee = Column(Float, nullable=True, comment="Temps estimé (heures)")
    optimise_par_ia = Column(Boolean, default=False, comment="Optimisation IA activée ?")

    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id", ondelete="SET NULL"),
        nullable=True,
        comment="Gamme liée"
    )

    machine = relationship("Machine", back_populates="plannings", lazy="joined")
    gamme = relationship("GammeProduction", back_populates="plannings", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('Prévu', 'En cours', 'Terminé')", name="check_statut_planning_machine"),
    )

    def __repr__(self):
        return f"<PlanningMachine machine={self.machine_id} statut={self.statut} date={self.date_debut}>"
