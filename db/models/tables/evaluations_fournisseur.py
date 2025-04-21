from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= EVALUATIONS FOURNISSEUR =========================
class EvaluationFournisseur(Base):
    __tablename__ = "evaluations_fournisseurs"

    id = Column(Integer, primary_key=True)
    fournisseur_id = Column(
        Integer,
        ForeignKey("fournisseurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID du fournisseur évalué",
    )
    date_evaluation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de l'évaluation",
    )
    note = Column(
        Float,
        nullable=False,
        comment="Note attribuée au fournisseur (ex: 4.5 sur 5)",
    )
    commentaire = Column(
        Text,
        nullable=True,
        comment="Commentaire ou retour sur le fournisseur",
    )
    critere = Column(
        String(100),
        nullable=False,
        comment="Critère d'évaluation (ex: qualité, délai, prix)",
    )

    # Relations
    fournisseur = relationship("Fournisseur", back_populates="evaluations")
