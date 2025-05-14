from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Robotique(Base):
    __tablename__ = "robotique"

    id = Column(Integer, primary_key=True)

    nom_robot = Column(String(100), nullable=False, comment="Nom du robot")
    fonction = Column(String(100), nullable=False, comment="Fonction principale")
    statut = Column(String(50), nullable=False, comment="Statut : actif, inactif, en panne, maintenance")
    affectation = Column(String(255), nullable=True, comment="Affectation dans l'atelier")
    date_ajout = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'enregistrement")

    controles = relationship("ControleRobot", back_populates="robot", cascade="all, delete-orphan", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "statut IN ('actif', 'inactif', 'en panne', 'maintenance')",
            name="check_statut_robotique"
        ),
    )

    def __repr__(self):
        return f"<Robotique id={self.id} nom='{self.nom_robot}' statut={self.statut}>"
