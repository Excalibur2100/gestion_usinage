from sqlalchemy import Column, Integer, String, DateTime, Text, Float, ForeignKey, Index
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= IA LOGS =========================
class IALogs(Base):
    __tablename__ = "ia_logs"

    id = Column(Integer, primary_key=True)
    date_execution = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date et heure de l'exécution de l'IA",
    )
    module = Column(
        String(100), nullable=False, comment="Nom du module ou composant IA"
    )
    action = Column(
        String(255), nullable=False, comment="Action ou décision prise par l'IA"
    )
    resultat = Column(Text, nullable=True, comment="Résultat ou sortie de l'IA")
    score_confiance = Column(
        Float, nullable=True, comment="Score de confiance associé à la décision"
    )
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de l'utilisateur associé à l'action (si applicable)",
    )

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="ia_logs")

    # Index
    __table_args__ = (
        Index("idx_date_execution", "date_execution"),
        Index("idx_module", "module"),
    )
