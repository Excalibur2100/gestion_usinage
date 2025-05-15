from sqlalchemy import Column, Integer, String, DateTime, Text, Float, ForeignKey, Index
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class IALogs(Base):
    __tablename__ = "ia_logs"

    id = Column(Integer, primary_key=True)

    date_execution = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date/heure d'exécution de l'IA"
    )
    module = Column(String(100), nullable=False, comment="Module ou fonctionnalité IA utilisée")
    action = Column(String(255), nullable=False, comment="Action ou logique exécutée")
    resultat = Column(Text, nullable=True, comment="Sortie ou réponse de l'IA")
    score_confiance = Column(Float, nullable=True, comment="Score de confiance (0 à 1)")

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Utilisateur lié à cette exécution"
    )

    utilisateur = relationship("Utilisateur", back_populates="ia_logs", lazy="joined")

    __table_args__ = (
        Index("idx_date_execution", "date_execution"),
        Index("idx_module", "module"),
    )

    def __repr__(self):
        return f"<IALogs module={self.module} action={self.action} utilisateur={self.utilisateur_id}>"
