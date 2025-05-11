from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint, Index
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class StatRH(Base):
    __tablename__ = "stat_rh"

    id = Column(Integer, primary_key=True)

    periode = Column(String(20), nullable=False, comment="Ex : 2025-04")
    type_stat = Column(String(50), nullable=False, comment="Ex : absences, formations, heures sup")
    valeur = Column(Float, nullable=False, comment="Valeur numérique de la stat")
    unite = Column(String(20), nullable=True, comment="Unité : h, jours, %, etc.")
    date_calcul = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de génération")

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    utilisateur = relationship("Utilisateur", back_populates="statistiques_rh", lazy="joined")

    __table_args__ = (
        CheckConstraint("valeur >= 0", name="check_valeur_stat_rh_positive"),
        Index("idx_stat_rh_periode_type", "periode", "type_stat"),
    )

    def __repr__(self):
        return f"<StatRH {self.type_stat}={self.valeur}{self.unite or ''} pour {self.periode}>"
