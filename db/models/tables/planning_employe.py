from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= PLANNING EMPLOYE =========================
class PlanningEmploye(Base):
    __tablename__ = "planning_employes"

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id"),
        nullable=False,
        comment="ID de l'utilisateur associé",
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=True,
        comment="ID de la machine associée",
    )
    date_debut = Column(DateTime, nullable=False, comment="Date de début de la tâche")
    date_fin = Column(DateTime, nullable=False, comment="Date de fin de la tâche")
    tache = Column(Text, nullable=False, comment="Description de la tâche")
    statut = Column(
        String(50),
        default="Prévu",
        nullable=False,
        comment="Statut de la tâche (Prévu, En cours, Terminé)",
    )
    affectation_auto = Column(
        Boolean, default=True, comment="Indique si l'affectation est automatique"
    )

    utilisateur = relationship("Utilisateur", back_populates="plannings")
    machine = relationship("Machine", back_populates="plannings_employes")
