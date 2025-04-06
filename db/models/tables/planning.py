from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= PLANNING EMPLOYE =========================
class PlanningEmploye(Base):
    __tablename__ = "planning_employes"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    tache = Column(String(255), nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="plannings")

# ========================= PLANNING MACHINE =========================
class PlanningMachine(Base):
    __tablename__ = "planning_machines"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    operation = Column(String(255), nullable=False)

    machine = relationship("Machine", back_populates="plannings")

# ========================= AFFECTATION MACHINE =========================
class AffectationMachine(Base):
    __tablename__ = "affectations_machines"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_affectation = Column(DateTime, default=datetime.utcnow)

    machine = relationship("Machine", back_populates="affectations")
    utilisateur = relationship("Utilisateur", back_populates="affectations")

# ========================= POINTAGE =========================
class Pointage(Base):
    __tablename__ = "pointages"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_pointage = Column(DateTime, default=datetime.utcnow)
    commentaire = Column(String(255), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="pointages")