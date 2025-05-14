from sqlalchemy import Column, Integer, Float, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class NotationRH(Base):
    __tablename__ = "notations_rh"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur évalué"
    )

    date_evaluation = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        comment="Date de l'évaluation"
    )

    note = Column(Float, nullable=False, comment="Note attribuée (0 à 5)")
    commentaire = Column(Text, nullable=True, comment="Remarques de l’évaluateur")

    utilisateur = relationship("Utilisateur", back_populates="notations", lazy="joined")

    __table_args__ = (
        CheckConstraint("note >= 0 AND note <= 5", name="check_note_rh_range"),
    )

    def __repr__(self):
        return f"<NotationRH utilisateur={self.utilisateur_id} note={self.note} date={self.date_evaluation}>"
