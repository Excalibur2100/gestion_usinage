from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Enum, Text, Boolean,
    ForeignKey, CheckConstraint, func
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class StatutFactureFournisseur(str, enum.Enum):
    brouillon = "brouillon"
    validee = "validee"
    payee = "payee"
    partiellement_payee = "partiellement_payee"
    annulee = "annulee"


class FactureFournisseur(Base):
    __tablename__ = "factures_fournisseur"
    __table_args__ = (
        CheckConstraint("montant_ht >= 0", name="check_montant_ht_positive"),
        CheckConstraint("taux_tva >= 0", name="check_taux_tva_positive"),
        CheckConstraint("montant_ttc >= 0", name="check_montant_ttc_positive"),
    )

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, index=True, nullable=True)

    numero_facture = Column(String(50), unique=True, nullable=False)
    reference_externe = Column(String(50), nullable=True)

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id"), nullable=True)
    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)

    date_emission = Column(DateTime, default=func.now())
    date_echeance = Column(DateTime, nullable=True)
    date_paiement = Column(DateTime, nullable=True)

    montant_ht = Column(Float, nullable=False)
    taux_tva = Column(Float, default=20.0)
    montant_ttc = Column(Float, nullable=False)
    montant_paye = Column(Float, nullable=True)
    reste_a_payer = Column(Float, nullable=True)

    devise = Column(String(10), default="EUR")
    taux_conversion = Column(Float, nullable=True)
    montant_devise_origine = Column(Float, nullable=True)

    statut = Column(Enum(StatutFactureFournisseur), default=StatutFactureFournisseur.brouillon)
    commentaire = Column(Text, nullable=True)
    fichier_pdf = Column(String(255), nullable=True)

    is_archived = Column(Boolean, default=False)
    version = Column(Integer, default=1)
    etat_synchronisation = Column(String(50), default="non_synchro")
    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relations ORM
    fournisseur = relationship("Fournisseur", back_populates="factures_fournisseur", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="factures_fournisseur", lazy="joined", foreign_keys=[utilisateur_id])
    commande = relationship("CommandeFournisseur", back_populates="factures_fournisseur", lazy="joined", uselist=False)
    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    def __repr__(self):
        return f"<FactureFournisseur(id={self.id}, numero='{self.numero_facture}', fournisseur_id={self.fournisseur_id})>"