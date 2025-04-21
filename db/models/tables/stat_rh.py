from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= STATISTIQUES RH =========================
class StatRH(Base):
    __tablename__ = "stat_rh"

    id = Column(Integer, primary_key=True)
    periode = Column(
        String(20), nullable=False, comment="Période de la statistique (ex: 2025-04)"
    )
    type_stat = Column(
        String(50),
        nullable=False,
        comment="Type de statistique (absences, formations, etc.)",
    )
    valeur = Column(Float, nullable=False, comment="Valeur de la statistique")
    unite = Column(
        String(20),
        nullable=True,
        comment="Unité de la statistique (ex: jours, heures, pourcentage)",
    )
    date_calcul = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de calcul de la statistique",
    )

    # Relations
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id"),
        nullable=True,
        comment="ID de l'utilisateur associé",
    )
    utilisateur = relationship("Utilisateur", back_populates="statistiques_rh")
