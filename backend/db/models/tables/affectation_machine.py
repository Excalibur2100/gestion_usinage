from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Text, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from db.models.base import Base

class AffectationMachine(Base):
    __tablename__ = "affectations_machines"

    id = Column(Integer, primary_key=True)

    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)

    date_affectation = Column(DateTime, default=datetime.utcnow, nullable=False)
    date_validation = Column(DateTime, nullable=True, comment="Date de validation par le manager")
    date_annulation = Column(DateTime, nullable=True, comment="Date d'annulation de l'affectation")
    date_fermeture = Column(DateTime, nullable=True, comment="Date de clôture de l'affectation")
    date_ajout = Column(DateTime, default=datetime.utcnow, nullable=False)
    date_modification = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    statut = Column(String(50), default="Actif", nullable=False, comment="Actif, Terminé, Annulé, Validé")
    tache = Column(Text, nullable=True)
    motif = Column(Text, nullable=True, comment="Motif d'annulation ou modification")
    commentaire = Column(Text, nullable=True)

    machine = relationship("Machine", back_populates="affectations", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="affectations", lazy="joined")

    # Utilisateur ayant réalisé les actions (relations multiples)
    cree_par_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    modifie_par_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    valide_par_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    annule_par_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    ferme_par_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    cree_par = relationship("Utilisateur", foreign_keys=[cree_par_id], lazy="joined")
    modifie_par = relationship("Utilisateur", foreign_keys=[modifie_par_id], lazy="joined")
    valide_par = relationship("Utilisateur", foreign_keys=[valide_par_id], lazy="joined")
    annule_par = relationship("Utilisateur", foreign_keys=[annule_par_id], lazy="joined")
    ferme_par = relationship("Utilisateur", foreign_keys=[ferme_par_id], lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('Actif', 'Terminé', 'Annulé', 'Validé')", name="check_statut_affectation"),
    )

    def __repr__(self):
        return f"<AffectationMachine utilisateur={self.utilisateur_id} machine={self.machine_id} statut={self.statut}>"

    def is_active(self):
        return self.statut == "Actif" and self.date_fermeture is None
