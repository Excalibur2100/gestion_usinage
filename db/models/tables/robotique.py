from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= ROBOTIQUE =========================
class Robotique(Base):
    __tablename__ = "robotique"

    id = Column(Integer, primary_key=True)
    nom_robot = Column(String(100), nullable=False, comment="Nom du robot")
    fonction = Column(String(100), nullable=False, comment="Fonction du robot")
    statut = Column(
        String(50), nullable=False, comment="Statut du robot (actif, inactif, etc.)"
    )
    affectation = Column(String(255), nullable=True, comment="Affectation du robot")
    date_ajout = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date d'ajout du robot",
    )

    # Relations
    controles = relationship(
        "ControleRobot", back_populates="robot", cascade="all, delete-orphan"
    )
