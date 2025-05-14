from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Text, CheckConstraint
from datetime import datetime
from sqlalchemy.orm import relationship
from db.models.base import Base

class Pointage(Base):
    __tablename__ = "pointages"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Opérateur concerné"
    )

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="SET NULL"),
        nullable=True,
        comment="Machine utilisée"
    )

    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id", ondelete="SET NULL"),
        nullable=True,
        comment="Gamme liée à l'opération"
    )

    date_pointage = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de pointage")
    heure_debut = Column(DateTime, nullable=False, comment="Début du travail")
    heure_fin = Column(DateTime, nullable=True, comment="Fin du travail")
    duree_effective = Column(Float, nullable=True, comment="Temps réel en heures")
    remarques = Column(Text, nullable=True, comment="Remarques ou incidents")

    utilisateur = relationship("Utilisateur", back_populates="pointages", lazy="joined")
    machine = relationship("Machine", back_populates="pointages", lazy="joined")
    gamme = relationship("GammeProduction", back_populates="pointages", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "heure_fin IS NULL OR heure_fin >= heure_debut",
            name="check_pointage_heure"
        ),
    )

    def __repr__(self):
        return f"<Pointage utilisateur={self.utilisateur_id} machine={self.machine_id} début={self.heure_debut}>"
