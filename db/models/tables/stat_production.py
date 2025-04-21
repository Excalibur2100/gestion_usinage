from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= STATISTIQUES DE PRODUCTION =========================
class StatProduction(Base):
    __tablename__ = "stat_production"

    id = Column(Integer, primary_key=True)
    periode = Column(
        String(20), nullable=False, comment="Période de la statistique (ex: 2025-04)"
    )
    type_stat = Column(
        String(50),
        nullable=False,
        comment="Type de statistique (efficacité, rendement, etc.)",
    )
    valeur = Column(Float, nullable=False, comment="Valeur de la statistique")
    unite = Column(
        String(20),
        nullable=True,
        comment="Unité de la statistique (ex: %, heures, pièces)",
    )
    date_calcul = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de calcul de la statistique",
    )

    # Relations
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=True,
        comment="ID de la machine associée",
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id"),
        nullable=True,
        comment="ID de l'utilisateur associé",
    )

    machine = relationship("Machine", back_populates="statistiques")
    utilisateur = relationship("Utilisateur", back_populates="statistiques")
