from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Enum, Text, Boolean,
    ForeignKey, CheckConstraint, func
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class StatutAvoir(str, enum.Enum):
    brouillon = "brouillon"
    valide = "valide"
    rembourse = "rembourse"
    annule = "annule"


class TypeAvoir(str, enum.Enum):
    retour = "retour_marchandise"
    remise = "remise_commerciale"
    geste = "geste_commercial"
    autre = "autre"


class AvoirFournisseur(Base):
    __tablename__ = "avoirs_fournisseur"
    __table_args__ = (
        CheckConstraint("montant_ht >= 0", name="check_montant_ht_positive"),
        CheckConstraint("taux_tva >= 0", name="check_taux_tva_positive"),
        CheckConstraint("montant_ttc >= 0", name="check_montant_ttc_positive"),
    )

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, index=True, nullable=True)
    reference = Column(String(50), unique=True, nullable=False)
    reference_externe = Column(String(50), nullable=True)

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    commande_id = Column(Integer, ForeignKey("commandes.id"), nullable=True)
    facture_id = Column(Integer, ForeignKey("factures_fournisseur.id"), nullable=True)
    document_lie_id = Column(Integer, ForeignKey("documents_qhse.id"), nullable=True)

    date_emission = Column(DateTime, server_default=func.now())
    date_remboursement = Column(DateTime, nullable=True)

    type_avoir = Column(Enum(TypeAvoir), default=TypeAvoir.autre)
    motif = Column(Text, nullable=True)
    commentaire = Column(Text, nullable=True)

    montant_ht = Column(Float, nullable=False)
    taux_tva = Column(Float, default=20.0)
    montant_ttc = Column(Float, nullable=False)
    ecart_montant = Column(Float, nullable=True)

    devise = Column(String(10), default="EUR", nullable=False)
    montant_devise_origine = Column(Float, nullable=True)
    taux_conversion = Column(Float, nullable=True)

    statut = Column(Enum(StatutAvoir), default=StatutAvoir.brouillon)

    is_archived = Column(Boolean, default=False)
    etat_synchronisation = Column(String(50), default="non_synchro")
    categorie = Column(String(50), nullable=True)
    tag = Column(String(50), nullable=True)
    version = Column(Integer, default=1)

    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # --- Relations ORM
    fournisseur = relationship("Fournisseur", back_populates="avoirs_fournisseur", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="avoirs_fournisseur", lazy="joined", foreign_keys=[utilisateur_id])
    commande = relationship("Commande", back_populates="avoirs_fournisseur", lazy="joined", uselist=False)
    facture = relationship("FactureFournisseur", back_populates="avoirs_fournisseur", lazy="joined", uselist=False)
    document_lie = relationship("DocumentQHSE", back_populates="avoirs_fournisseur", lazy="joined", uselist=False)
    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    def __repr__(self):
        return f"<AvoirFournisseur(id={self.id}, ref='{self.reference}', fournisseur_id={self.fournisseur_id})>"