from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= CONTRÔLE ROBOT =========================
class ControleRobot(Base):
    __tablename__ = "controle_robot"

    id = Column(Integer, primary_key=True)
    robot_id = Column(
        Integer,
        ForeignKey("robotique.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID du robot contrôlé",
    )
    action = Column(
        String(255),
        nullable=False,
        comment="Action effectuée par le robot (ex: soudage, assemblage)",
    )
    statut = Column(
        String(100),
        nullable=True,
        comment="Statut de l'action (ex: réussie, échouée, en cours)",
    )
    date_execution = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date et heure d'exécution de l'action",
    )
    remarque = Column(
        Text,
        nullable=True,
        comment="Remarques ou observations sur l'action effectuée",
    )

    # Relations
    robot = relationship("Robotique", back_populates="controles")
