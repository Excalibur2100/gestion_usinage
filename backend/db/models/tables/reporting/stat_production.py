from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint, Index
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class StatProduction(Base):
    __tablename__ = "stat_production"

    id = Column(Integer, primary_key=True)

    periode = Column(String(20), nullable=False, comment="Ex : 2025-04")
    type_stat = Column(String(50), nullable=False, comment="Ex : rendement, efficacité")
    valeur = Column(Float, nullable=False, comment="Valeur mesurée")
    unite = Column(String(20), nullable=True, comment="Unité (% / h / pièces)")
    date_calcul = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de génération")

    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    machine = relationship("Machine", back_populates="statistiques", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="statistiques", lazy="joined")

    __table_args__ = (
        CheckConstraint("valeur >= 0", name="check_valeur_stat_prod_positive"),
        Index("idx_stat_prod_periode_type", "periode", "type_stat"),
    )

    def __repr__(self):
        return f"<StatProduction {self.type_stat}={self.valeur}{self.unite or ''} pour {self.periode}>"
