from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class ChargeMachine(Base):
    __tablename__ = "charges_machine"

    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"), nullable=True)
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    statut = Column(
        String(50), default="planifié", nullable=False
    )  # planifié, en cours, terminé
    temperature = Column(Float, nullable=True, comment="Température mesurée")
    vibration = Column(Float, nullable=True, comment="Vibration mesurée")

    # Relations
    machine = relationship("Machine", back_populates="charges")
    gamme = relationship("GammeProduction")
