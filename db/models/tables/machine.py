from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= MACHINES =========================
class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type_machine = Column(String(50), nullable=False)
    vitesse_max = Column(Float, nullable=True)
    puissance = Column(Float, nullable=True)
    nb_axes = Column(Integer, nullable=True)

    postprocesseurs = relationship("PostProcesseur", back_populates="machine")
    maintenances = relationship("Maintenance", back_populates="machine")
    gammes = relationship("GammeProduction", back_populates="machine")
    plannings = relationship("PlanningMachine", back_populates="machine")
    affectations = relationship("AffectationMachine", back_populates="machine")
    metrics = relationship("MetricsMachine", back_populates="machine")

# ========================= METRICS MACHINES =========================
class MetricsMachine(Base):
    __tablename__ = "metrics_machine"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    temperature = Column(Float, nullable=True)
    vibration = Column(Float, nullable=True)
    charge = Column(Float, nullable=True)

    machine = relationship("Machine", back_populates="metrics")