from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Formation(Base):
    __tablename__ = "formations"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur formé"
    )

    nom = Column(String(150), nullable=False, comment="Intitulé de la formation")
    organisme = Column(String(150), nullable=True, comment="Nom de l'organisme formateur")
    date_debut = Column(DateTime, nullable=False, comment="Date de début de la formation")
    date_fin = Column(DateTime, nullable=False, comment="Date de fin de la formation")
    certification = Column(String(150), nullable=True, comment="Diplôme ou certificat obtenu")
    commentaire = Column(Text, nullable=True, comment="Observations ou retours")
    statut = Column(String(50), default="terminée", nullable=False, comment="Statut : planifiée, terminée, abandonnée")

    utilisateur = relationship("Utilisateur", back_populates="formations", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('planifiée', 'terminée', 'abandonnée')", name="check_statut_formation"),
    )

    def __repr__(self):
        return f"<Formation nom={self.nom} utilisateur={self.utilisateur_id} statut={self.statut}>"
