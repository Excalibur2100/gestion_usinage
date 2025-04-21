from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Text
from sqlalchemy import CheckConstraint
from datetime import datetime
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= POINTAGE =========================
class Pointage(Base):
    __tablename__ = "pointages"

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
    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id"),
        nullable=True,
        comment="ID de la gamme de production associée",
    )
    date_pointage = Column(
        DateTime, default=datetime.utcnow, nullable=False, comment="Date du pointage"
    )
    heure_debut = Column(DateTime, nullable=False, comment="Heure de début")
    heure_fin = Column(DateTime, nullable=True, comment="Heure de fin")
    duree_effective = Column(
        Float, nullable=True, comment="Durée effective (en heures)"
    )
    remarques = Column(Text, nullable=True, comment="Remarques sur le pointage")

    utilisateur = relationship("Utilisateur", back_populates="pointages")
    machine = relationship("Machine", back_populates="pointages")
    gamme = relationship("GammeProduction", back_populates="pointages")

    __table_args__ = (
        CheckConstraint(
            "heure_fin IS NULL OR heure_fin >= heure_debut", name="check_pointage_heure"
        ),
    )
