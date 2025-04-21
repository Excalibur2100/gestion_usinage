from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    DateTime,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= METRICS MACHINES =========================
class MetricsMachine(Base):
    """
    Classe MetricsMachine représentant les métriques associées à une machine.

    Attributs :
        - machine_id : ID de la machine associée.
        - timestamp : Horodatage des métriques.
        - temperature : Température de la machine (en °C).
        - vibration : Niveau de vibration de la machine.
        - charge : Charge de la machine (en %).
    """
    __tablename__ = "metrics_machine"

    id = Column(Integer, primary_key=True)
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=False,
        index=True,
        comment="ID de la machine associée",
    )
    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Horodatage des métriques",
    )
    temperature = Column(
        Float, nullable=True, comment="Température de la machine (en °C)"
    )
    vibration = Column(
        Float, nullable=True, comment="Niveau de vibration de la machine"
    )
    charge = Column(Float, nullable=True, comment="Charge de la machine (en %)")

    # Relation avec Machine
    machine = relationship("Machine", back_populates="metrics")

    __table_args__ = (
        CheckConstraint("temperature >= -50 AND temperature <= 150", name="check_temperature_range"),
        CheckConstraint("vibration >= 0 AND vibration <= 100", name="check_vibration_range"),
        CheckConstraint("charge >= 0 AND charge <= 100", name="check_charge_range"),
    )

    # Méthodes utilitaires
    def __repr__(self):
        return f"<MetricsMachine(id={self.id}, machine_id={self.machine_id}, timestamp={self.timestamp})>"

    def is_critical(self, temp_threshold=100, vibration_threshold=80, charge_threshold=90):
        return (
            (self.temperature and self.temperature > temp_threshold) or
            (self.vibration and self.vibration > vibration_threshold) or
            (self.charge and self.charge > charge_threshold)
        )