from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= SURVEILLANCE CAMERA =========================
class SurveillanceCamera(Base):
    __tablename__ = "surveillance_cameras"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de la caméra")
    emplacement = Column(
        String(255), nullable=False, comment="Emplacement de la caméra"
    )
    ip_address = Column(
        String(50), nullable=False, unique=True, comment="Adresse IP de la caméra"
    )
    statut = Column(
        String(50),
        default="active",
        nullable=False,
        comment="Statut de la caméra (active, inactive, en maintenance)",
    )
    date_installation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date d'installation de la caméra",
    )
    description = Column(
        Text, nullable=True, comment="Description ou remarques sur la caméra"
    )
    enregistrement_actif = Column(
        Boolean, default=True, comment="Indique si l'enregistrement est actif"
    )

    # Relations
    incidents = relationship(
        "IncidentSurveillance", back_populates="camera", cascade="all, delete-orphan"
    )
