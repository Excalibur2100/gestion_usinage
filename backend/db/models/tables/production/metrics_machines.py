from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class MetricsMachine(Base):
    __tablename__ = "metrics_machine"

    id = Column(Integer, primary_key=True)

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Machine concernée"
    )
    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Horodatage des mesures"
    )

    temperature = Column(Float, nullable=True, comment="Température (°C)")
    vibration = Column(Float, nullable=True, comment="Vibration (en % ou Hz)")
    charge = Column(Float, nullable=True, comment="Charge CPU ou production (%)")

    machine = relationship("Machine", back_populates="metrics", lazy="joined")

    __table_args__ = (
        CheckConstraint("temperature >= -50 AND temperature <= 150", name="check_temperature_range"),
        CheckConstraint("vibration >= 0 AND vibration <= 100", name="check_vibration_range"),
        CheckConstraint("charge >= 0 AND charge <= 100", name="check_charge_range"),
    )

    def __repr__(self):
        return f"<MetricsMachine machine={self.machine_id} at {self.timestamp}>"

    def is_critical(self, temp_threshold=100, vibration_threshold=80, charge_threshold=90):
        return (
            (self.temperature and self.temperature > temp_threshold) or
            (self.vibration and self.vibration > vibration_threshold) or
            (self.charge and self.charge > charge_threshold)
        )
