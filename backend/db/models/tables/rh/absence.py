from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Absence(Base):
    __tablename__ = "absences"

    id = Column(Integer, primary_key=True, index=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True, comment="Utilisateur ayant fait la demande")
    utilisateur = relationship("Utilisateur", back_populates="absences", lazy="joined")

    employe_id = Column(Integer, ForeignKey("employes.id", ondelete="CASCADE"), nullable=False, comment="Employé concerné")
    employe = relationship("Employe", back_populates="absences", lazy="joined")

    type_absence = Column(String(50), nullable=False, comment="Type : congé, maladie, RTT, parental, exceptionnel")
    statut = Column(String(30), default="en attente", nullable=False, comment="Statut : en attente, validée, refusée, annulée")
    is_paid = Column(Boolean, default=True, nullable=False, comment="Absence rémunérée : True ou False")

    date_debut = Column(Date, nullable=False, comment="Début de l'absence")
    date_fin = Column(Date, nullable=False, comment="Fin de l'absence")
    date_demande = Column(Date, default=datetime.utcnow, nullable=False, comment="Date de demande")
    date_validation = Column(Date, nullable=True, comment="Date de validation de l'absence")
    date_annulation = Column(Date, nullable=True, comment="Date d'annulation")
    date_modification = Column(Date, nullable=True, comment="Date de dernière modification")
    date_ajout = Column(Date, default=datetime.utcnow, nullable=False, comment="Date de création de l'entrée")

    justificatif_url = Column(String(255), nullable=True, comment="Lien ou chemin vers justificatif PDF")
    commentaire = Column(Text, nullable=True, comment="Commentaire du RH ou manager")

    valide_par_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True, comment="Manager ou RH validateur")
    valide_par = relationship("Utilisateur", foreign_keys=[valide_par_id], lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('en attente', 'validée', 'refusée', 'annulée')", name="check_statut_absence"),
        CheckConstraint("type_absence IN ('congé', 'maladie', 'RTT', 'parental', 'exceptionnel')", name="check_type_absence"),
    )

    def __repr__(self):
        return f"<Absence employe_id={self.employe_id} {self.date_debut}→{self.date_fin} statut={self.statut}>"

    def duree(self):
        """Retourne la durée en jours de l'absence."""
        if self.date_fin and self.date_debut:
            return (self.date_fin - self.date_debut).days + 1
        return 0
