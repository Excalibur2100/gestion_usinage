from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class ControleRobot(Base):
    __tablename__ = "controle_robot"

    id = Column(Integer, primary_key=True)

    robot_id = Column(
        Integer,
        ForeignKey("robotique.id", ondelete="CASCADE"),
        nullable=False,
        comment="Robot ayant exécuté l'action"
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Opérateur ou superviseur ayant déclenché l'action"
    )

    action = Column(String(255), nullable=False, comment="Action exécutée (soudage, assemblage...)")
    statut = Column(String(100), nullable=False, default="en cours", comment="Statut : réussie, échouée, en cours")
    date_execution = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date et heure d'exécution")
    remarque = Column(Text, nullable=True, comment="Remarques ou observations sur l'action")

    robot = relationship("Robotique", back_populates="controles", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="controles_robot", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "statut IN ('réussie', 'échouée', 'en cours')",
            name="check_statut_controle_robot"
        ),
    )

    def __repr__(self):
        return f"<ControleRobot robot={self.robot_id} action={self.action} statut={self.statut}>"
