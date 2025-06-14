from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Text,
    ForeignKey, Enum, CheckConstraint, func
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class StatutLigneCommande(str, enum.Enum):
    non_recue = "non_recue"
    partiellement_recue = "partiellement_recue"
    recue = "recue"
    annulee = "annulee"


class LigneCommandeFournisseur(Base):
    __tablename__ = "lignes_commande_fournisseur"
    __table_args__ = (
        CheckConstraint("quantite >= 0", name="check_quantite_positive"),
        CheckConstraint("prix_unitaire_ht >= 0", name="check_pu_ht_positive"),
        CheckConstraint("montant_ht >= 0", name="check_montant_ht_positive"),
        CheckConstraint("montant_ttc >= 0", name="check_montant_ttc_positive"),
        CheckConstraint("taux_tva >= 0", name="check_taux_tva_positive"),
    )

    id = Column(Integer, primary_key=True, index=True)
    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=True)

    designation = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    quantite = Column(Float, nullable=False)
    prix_unitaire_ht = Column(Float, nullable=False)
    taux_tva = Column(Float, default=20.0)
    montant_ht = Column(Float, nullable=False)
    montant_ttc = Column(Float, nullable=False)
    unite = Column(String(50), nullable=True)

    statut = Column(Enum(StatutLigneCommande), default=StatutLigneCommande.non_recue)
    commentaire = Column(Text, nullable=True)

    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relations
    commande = relationship("CommandeFournisseur", back_populates="lignes_commande", lazy="joined")
    article = relationship("Article", back_populates="lignes_commande", lazy="joined")
    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    def __repr__(self):
        return (
            f"<LigneCommandeFournisseur(id={self.id}, designation='{self.designation}', "
            f"quantite={self.quantite}, statut={self.statut})>"
        )