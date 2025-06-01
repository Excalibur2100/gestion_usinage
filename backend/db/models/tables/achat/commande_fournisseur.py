from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Enum, Boolean,
    ForeignKey, Text, func, CheckConstraint
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class StatutCommandeFournisseur(str, enum.Enum):
    brouillon = "brouillon"
    envoyee = "envoyee"
    partiellement_livree = "partiellement_livree"
    livree = "livree"
    annulee = "annulee"


class CommandeFournisseur(Base):
    __tablename__ = "commandes_fournisseur"
    __table_args__ = (
        CheckConstraint("montant_total >= 0", name="check_montant_total_positive"),
    )

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, index=True, nullable=True)
    numero_commande = Column(String(50), unique=True, nullable=False, index=True)
    reference_externe = Column(String(50), nullable=True)

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)

    date_commande = Column(DateTime, server_default=func.now())
    date_livraison_prevue = Column(DateTime, nullable=True)
    date_livraison_effective = Column(DateTime, nullable=True)

    statut = Column(Enum(StatutCommandeFournisseur), default=StatutCommandeFournisseur.brouillon, nullable=False)
    commentaire = Column(Text, nullable=True)
    devise = Column(String(10), default="EUR", nullable=False)
    montant_total = Column(Float, nullable=False, default=0.0)

    is_archived = Column(Boolean, default=False)
    version = Column(Integer, default=1)
    etat_synchronisation = Column(String(50), default="non_synchro")
    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relations ORM
    fournisseur = relationship("Fournisseur", back_populates="commandes_fournisseur", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="commandes_fournisseur", lazy="joined", foreign_keys=[utilisateur_id])
    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    lignes_commande = relationship(
        "LigneCommandeFournisseur",  # table à venir
        back_populates="commande",
        cascade="all, delete-orphan",
        lazy="joined"
    )

    def __repr__(self):
        return f"<CommandeFournisseur(id={self.id}, numero={self.numero_commande}, fournisseur={self.fournisseur_id})>"