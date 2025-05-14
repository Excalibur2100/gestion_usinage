from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class PlanningEmploye(Base):
    __tablename__ = "planning_employes"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Opérateur assigné"
    )

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="SET NULL"),
        nullable=True,
        comment="Machine utilisée"
    )

    date_debut = Column(DateTime, nullable=False, comment="Début de l'affectation")
    date_fin = Column(DateTime, nullable=False, comment="Fin de l'affectation")
    tache = Column(Text, nullable=False, comment="Travail ou mission à effectuer")

    statut = Column(
        String(50),
        default="Prévu",
        nullable=False,
        comment="Prévu, En cours, Terminé"
    )

    affectation_auto = Column(Boolean, default=True, comment="Affectation IA automatique ?")

    utilisateur = relationship("Utilisateur", back_populates="plannings", lazy="joined")
    machine = relationship("Machine", back_populates="plannings_employes", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('Prévu', 'En cours', 'Terminé')", name="check_statut_planning"),
    )

    def __repr__(self):
        return f"<PlanningEmploye utilisateur={self.utilisateur_id} statut={self.statut} tâche={self.tache[:20]}...>"
