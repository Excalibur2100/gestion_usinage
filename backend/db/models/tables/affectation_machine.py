from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= AFFECTATION MACHINE =========================
class AffectationMachine(Base):
    __tablename__ = "affectations_machines"

    id = Column(Integer, primary_key=True)
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=False,
        comment="ID de la machine associée",
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id"),
        nullable=False,
        comment="ID de l'utilisateur associé",
    )
    date_affectation = Column(
        DateTime, default=datetime.utcnow, nullable=False, comment="Date d'affectation"
    )
    tache = Column(Text, nullable=True, comment="Tâche associée à l'affectation")
    statut = Column(
        String(50),
        default="Actif",
        nullable=False,
        comment="Statut de l'affectation (Actif, Terminé)",
    )

    machine = relationship("Machine", back_populates="affectations")
    utilisateur = relationship("Utilisateur", back_populates="affectations")
