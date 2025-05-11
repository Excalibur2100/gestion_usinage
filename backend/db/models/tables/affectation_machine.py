from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from db.models.base import Base

class AffectationMachine(Base):
    __tablename__ = "affectations_machines"

    id = Column(Integer, primary_key=True)

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la machine associée",
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de l'utilisateur associé",
    )

    date_affectation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date d'affectation de l'utilisateur à la machine",
    )
    tache = Column(Text, nullable=True, comment="Tâche affectée à l'opérateur")
    statut = Column(
        String(50),
        default="Actif",
        nullable=False,
        comment="Statut : Actif, Terminé, Suspendu...",
    )

    machine = relationship("Machine", back_populates="affectations", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="affectations", lazy="joined")

    def __repr__(self):
        return f"<AffectationMachine utilisateur={self.utilisateur_id} machine={self.machine_id} statut={self.statut}>"
