from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Entretien(Base):
    __tablename__ = "entretiens"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur concerné par l'entretien"
    )

    type_entretien = Column(String(100), nullable=False, comment="Type : annuel, sécurité, disciplinaire, etc.")
    date = Column(DateTime, nullable=False, comment="Date prévue ou réalisée")
    statut = Column(String(50), default="planifié", nullable=False, comment="Statut : planifié, réalisé, annulé")
    resume = Column(Text, nullable=True, comment="Résumé des échanges")
    actions_prevues = Column(Text, nullable=True, comment="Actions à mener après l'entretien")

    utilisateur = relationship("Utilisateur", back_populates="entretiens", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "statut IN ('planifié', 'réalisé', 'annulé')",
            name="check_statut_entretien"
        ),
    )

    def __repr__(self):
        return f"<Entretien id={self.id} utilisateur={self.utilisateur_id} type={self.type_entretien} statut={self.statut}>"
