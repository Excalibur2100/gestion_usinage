from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= MAINTENANCE =========================
class Maintenance(Base):
    __tablename__ = "maintenances"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_maintenance = Column(String(50), nullable=False)  # préventive, corrective, prédictive
    date_planifiee = Column(DateTime, nullable=False)
    date_reelle = Column(DateTime, nullable=True)
    statut = Column(String(50), nullable=False)  # planifiée, en cours, réalisée
    description = Column(Text, nullable=True)
    remarques = Column(Text, nullable=True)

    machine = relationship("Machine", back_populates="maintenances")
    utilisateur = relationship("Utilisateur", back_populates="maintenances")