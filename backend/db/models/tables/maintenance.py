from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= MAINTENANCE =========================
class Maintenance(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True)
    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la machine associée",
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de l'utilisateur responsable",
    )
    type_maintenance = Column(
        String(50),
        nullable=False,
        comment="Type de maintenance (préventive, corrective, prédictive)",
    )
    date_planifiee = Column(
        DateTime, nullable=False, comment="Date planifiée pour la maintenance"
    )
    date_reelle = Column(
        DateTime, nullable=True, comment="Date réelle de réalisation de la maintenance"
    )
    statut = Column(
        String(50),
        nullable=False,
        default="planifiée",
        comment="Statut de la maintenance (planifiée, en cours, réalisée)",
    )
    description = Column(Text, nullable=True, comment="Description de la maintenance")
    remarques = Column(Text, nullable=True, comment="Remarques supplémentaires")

    # Timestamps
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création de l'enregistrement",
    )
    updated_at = Column(
        DateTime,
        onupdate=datetime.utcnow,
        comment="Date de dernière mise à jour de l'enregistrement",
    )

    # Relations
    machine = relationship("Machine", back_populates="maintenances")
    utilisateur = relationship("Utilisateur", back_populates="maintenances")

    __table_args__ = (
        CheckConstraint(
            "type_maintenance IN ('préventive', 'corrective', 'prédictive')",
            name="check_type_maintenance",
        ),
        CheckConstraint(
            "statut IN ('planifiée', 'en cours', 'réalisée')",
            name="check_statut_maintenance",
        ),
    )
