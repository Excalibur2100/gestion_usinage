from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class PredictionMaintenanceAI(Base):
    __tablename__ = "predictions_maintenance_ai"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    type_prediction = Column(String(100), nullable=False, comment="usure outil, panne, calibration, etc.")
    niveau_risque = Column(String(50), default="modéré")
    delai_prediction = Column(String(50), comment="Ex: 7 jours, 3h...")
    message = Column(Text, nullable=True)
    source_ia = Column(String(50), default="gpt-4")
    date_prediction = Column(DateTime(timezone=True), server_default=func.now())

    machine = relationship("Machine", back_populates="predictions_ia")
    utilisateur = relationship("Utilisateur", back_populates="predictions_ia")

    def __repr__(self):
        return f"<PredictionAI(machine={self.machine_id}, type='{self.type_prediction}', risque='{self.niveau_risque}')>"