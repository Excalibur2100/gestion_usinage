from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= MACHINES ===========================
class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True, index=True, comment="Nom unique de la machine")
    type_machine = Column(
        String(50),
        nullable=False,
        index=True,
        comment="Type de la machine (ex: CNC, imprimante 3D)",
    )
    vitesse_max = Column(Float, nullable=True, comment="Vitesse maximale de la machine")
    puissance = Column(Float, nullable=True, comment="Puissance de la machine (en kW)")
    nb_axes = Column(Integer, nullable=True, comment="Nombre d'axes de la machine")
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création de la machine",
    )
    updated_at = Column(
        DateTime,
        onupdate=datetime.utcnow,
        comment="Date de dernière mise à jour de la machine",
    )

    # Relations
    postprocesseurs = relationship("PostProcesseur", back_populates="machine")
    maintenances = relationship("Maintenance", back_populates="machine")
    gammes = relationship("GammeProduction", back_populates="machine")
    plannings = relationship("PlanningMachine", back_populates="machine")
    plannings_employes = relationship("PlanningEmploye", back_populates="machine")
    affectations = relationship("AffectationMachine", back_populates="machine")
    pointages = relationship("Pointage", back_populates="machine")
    metrics = relationship("MetricsMachine", back_populates="machine")
    outils = relationship("Outil", secondary="machine_outil", back_populates="machines")
    postes = relationship("Poste", back_populates="machine", cascade="all, delete")
    utilisateurs = relationship("Utilisateur", back_populates="machine", cascade="all, delete")

    __table_args__ = (
        CheckConstraint(
            "type_machine IN ('CNC', 'Imprimante 3D', 'Tour', 'Fraiseuse')",
            name="check_type_machine",
        ),
    )

    # Méthodes utilitaires
    def __repr__(self):
        return f"<Machine(id={self.id}, nom='{self.nom}', type_machine='{self.type_machine}')>"

    def is_compatible_with_outil(self, outil):
        return outil in self.outils