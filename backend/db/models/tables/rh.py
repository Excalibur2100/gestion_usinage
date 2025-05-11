from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class RH(Base):
    __tablename__ = "rh"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur concerné"
    )

    poste = Column(String(100), nullable=False, comment="Poste actuel (ex: opérateur, technicien)")
    contrat = Column(String(100), nullable=False, comment="Type de contrat (CDI, CDD, intérim)")
    temps_travail = Column(Float, nullable=False, comment="Taux temps plein (1.0 = 100%)")
    est_cadre = Column(Boolean, default=False, nullable=False, comment="Est-ce un cadre ?")
    date_debut = Column(DateTime, nullable=False, comment="Date de début de contrat")
    salaire_brut = Column(Float, nullable=True, comment="Salaire mensuel brut (€)")
    statut_administratif = Column(String(100), nullable=True, comment="Statut : actif, suspendu, démissionnaire, etc.")
    remarques = Column(Text, nullable=True, comment="Remarques RH (optionnel)")

    utilisateur = relationship("Utilisateur", back_populates="rh", lazy="joined")

    __table_args__ = (
        CheckConstraint("temps_travail >= 0.1 AND temps_travail <= 1.0", name="check_temps_travail_range"),
    )

    def __repr__(self):
        return f"<RH utilisateur={self.utilisateur_id} poste='{self.poste}' contrat={self.contrat}>"
