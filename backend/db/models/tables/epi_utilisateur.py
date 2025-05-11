from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class EPIUtilisateur(Base):
    __tablename__ = "epis_utilisateur"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur à qui l'EPI est attribué"
    )

    nom_epi = Column(String(150), nullable=False, comment="Nom ou référence de l'équipement")
    date_attribution = Column(String(50), nullable=False, comment="Date d'attribution de l'EPI")
    date_retour = Column(String(50), nullable=True, comment="Date de retour de l'EPI")
    statut = Column(String(50), default="en cours", nullable=False, comment="Statut : en cours, retourné, perdu")
    epi_id = Column(Integer, ForeignKey("epi.id", ondelete="SET NULL"), nullable=True)


    utilisateur = relationship("Utilisateur", back_populates="epis", lazy="joined")
    epi = relationship("EPI", back_populates="utilisateurs", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('en cours', 'retourné', 'perdu')", name="check_statut_epi"),
    )

    def __repr__(self):
        return f"<EPIUtilisateur {self.nom_epi} utilisateur={self.utilisateur_id} statut={self.statut} epi={self.epi_id}>"