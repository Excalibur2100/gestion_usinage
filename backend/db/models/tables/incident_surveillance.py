from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class IncidentSurveillance(Base):
    __tablename__ = "incidents_surveillance"

    id = Column(Integer, primary_key=True)

    camera_id = Column(
        Integer,
        ForeignKey("surveillance_cameras.id", ondelete="CASCADE"),
        nullable=False,
        comment="Caméra concernée"
    )

    type_incident = Column(
        String(100),
        nullable=False,
        comment="Type : mouvement, perte signal, anomalie, intrusion..."
    )

    description = Column(Text, nullable=True, comment="Détail de l'incident ou constatation")

    date_incident = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        comment="Horodatage de l'incident"
    )

    niveau = Column(
        String(50),
        nullable=False,
        default="mineur",
        comment="Gravité : mineur, critique, informatif"
    )

    camera = relationship("SurveillanceCamera", back_populates="incidents", lazy="joined")

    __table_args__ = (
        CheckConstraint("niveau IN ('mineur', 'critique', 'informatif')", name="check_niveau_incident"),
    )

    def __repr__(self):
        return f"<IncidentSurveillance id={self.id} type='{self.type_incident}' niveau={self.niveau}>"
