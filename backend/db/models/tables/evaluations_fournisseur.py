from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class EvaluationFournisseur(Base):
    __tablename__ = "evaluations_fournisseurs"

    id = Column(Integer, primary_key=True)

    fournisseur_id = Column(
        Integer,
        ForeignKey("fournisseurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Fournisseur évalué"
    )

    responsable_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Évaluateur interne"
    )

    date_evaluation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de l'évaluation")
    note = Column(Float, nullable=False, comment="Note de 0 à 5")
    critere = Column(String(100), nullable=False, comment="Critère : qualité, délai, prix, etc.")
    commentaire = Column(Text, nullable=True, comment="Remarques ou explication de la note")

    fournisseur = relationship("Fournisseur", back_populates="evaluations", lazy="joined")
    responsable = relationship("Utilisateur", back_populates="evaluations_fournisseurs", lazy="joined")

    __table_args__ = (
        CheckConstraint("note >= 0 AND note <= 5", name="check_note_evaluation"),
    )

    def __repr__(self):
        return f"<EvaluationFournisseur fournisseur={self.fournisseur_id} note={self.note} critere={self.critere}>"
