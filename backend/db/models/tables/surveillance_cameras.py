from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class SurveillanceCamera(Base):
    __tablename__ = "surveillance_cameras"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom de la caméra")
    emplacement = Column(String(255), nullable=False, comment="Emplacement physique")
    ip_address = Column(String(50), nullable=False, unique=True, comment="Adresse IP")
    statut = Column(String(50), default="active", nullable=False, comment="Statut : active, inactive, en maintenance")
    date_installation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'installation")
    description = Column(Text, nullable=True, comment="Notes, précisions")
    enregistrement_actif = Column(Boolean, default=True, comment="Enregistrement en cours ?")

    incidents = relationship("IncidentSurveillance", back_populates="camera", cascade="all, delete-orphan", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('active', 'inactive', 'en maintenance')", name="check_statut_camera"),
    )

    def __repr__(self):
        return f"<SurveillanceCamera id={self.id} nom='{self.nom}' statut={self.statut}>"
