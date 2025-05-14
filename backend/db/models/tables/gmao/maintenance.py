from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Maintenance(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True)

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        comment="Machine concernée"
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Responsable de la maintenance"
    )

    type_maintenance = Column(String(50), nullable=False, comment="Préventive, corrective, prédictive")
    statut = Column(String(50), default="planifiée", nullable=False, comment="Statut : planifiée, en cours, réalisée")
    
    date_planifiee = Column(DateTime, nullable=False, comment="Date prévue")
    date_reelle = Column(DateTime, nullable=True, comment="Date d'exécution réelle")

    description = Column(Text, nullable=True, comment="Contenu de l’intervention")
    remarques = Column(Text, nullable=True, comment="Remarques éventuelles")

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Créé le")
    updated_at = Column(DateTime, onupdate=datetime.utcnow, comment="Mis à jour le")

    machine = relationship("Machine", back_populates="maintenances", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="maintenances", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "type_maintenance IN ('préventive', 'corrective', 'prédictive')",
            name="check_type_maintenance"
        ),
        CheckConstraint(
            "statut IN ('planifiée', 'en cours', 'réalisée')",
            name="check_statut_maintenance"
        ),
    )

    def __repr__(self):
        return f"<Maintenance id={self.id} machine={self.machine_id} type={self.type_maintenance} statut={self.statut}>"
