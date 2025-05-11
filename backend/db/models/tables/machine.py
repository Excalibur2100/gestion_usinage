from sqlalchemy import Column, Integer, String, Float, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, unique=True, index=True, comment="Nom unique de la machine")
    type_machine = Column(String(50), nullable=False, index=True, comment="Type : CNC, Tour, etc.")
    vitesse_max = Column(Float, nullable=True, comment="Vitesse max (en tr/min)")
    puissance = Column(Float, nullable=True, comment="Puissance (en kW)")
    nb_axes = Column(Integer, nullable=True, comment="Nombre d'axes")

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Créée le")
    updated_at = Column(DateTime, onupdate=datetime.utcnow, comment="Dernière MAJ")

    # Relations
    postprocesseurs = relationship("PostProcesseur", back_populates="machine", cascade="all, delete-orphan", lazy="joined")
    maintenances = relationship("Maintenance", back_populates="machine", lazy="joined")
    gammes = relationship("GammeProduction", back_populates="machine", lazy="joined")
    plannings = relationship("PlanningMachine", back_populates="machine", cascade="all, delete-orphan", lazy="joined")
    commandes = relationship("CommandeMachine", back_populates="machine", lazy="joined")
    plannings_employes = relationship("PlanningEmploye", back_populates="machine", cascade="all, delete-orphan")
    affectations = relationship("AffectationMachine", back_populates="machine", lazy="joined")
    pointages = relationship("Pointage", back_populates="machine", cascade="all, delete-orphan")
    metrics = relationship("MetricsMachine", back_populates="machine", cascade="all, delete-orphan", lazy="joined")
    outils = relationship("Outil", secondary="machine_outil", back_populates="machines", lazy="joined")
    postes = relationship("Poste", back_populates="machine", cascade="all, delete", lazy="joined")
    utilisateurs = relationship("Utilisateur", back_populates="machine", cascade="all, delete", lazy="joined")
    non_conformites = relationship("NonConformite", back_populates="machine/materiau/outil/instrument", cascade="all, delete-orphan")
    materiaux = relationship("Materiau", back_populates="machine", cascade="all, delete-orphan")
    instruments = relationship("InstrumentControle", back_populates="machine", cascade="all, delete-orphan")
    fournisseurs = relationship("Fournisseur", back_populates="machines", cascade="all, delete-orphan")
    emplacements = relationship("EmplacementStock", back_populates="machines", cascade="all, delete-orphan")
    gammes_production = relationship("GammeProduction", back_populates="machine", cascade="all, delete-orphan")
    finance = relationship("Finance", back_populates="machine", lazy="joined")
    qhse = relationship("QHSE", back_populates="machine", lazy="joined")
    postes = relationship("Poste", back_populates="machine", cascade="all, delete-orphan")
    productions = relationship("Production", back_populates="machine", cascade="all, delete-orphan")
    statistiques = relationship("StatProduction", back_populates="machine", cascade="all, delete-orphan", lazy="joined")




    __table_args__ = (
        CheckConstraint(
            "type_machine IN ('CNC', 'Imprimante 3D', 'Tour', 'Fraiseuse')",
            name="check_type_machine"
        ),
    )

    def __repr__(self):
        return f"<Machine(id={self.id}, nom='{self.nom}', type_machine='{self.type_machine}')>"

    def is_compatible_with_outil(self, outil):
        return outil in self.outils
