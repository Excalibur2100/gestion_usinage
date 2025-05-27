from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class SuiviReglementFournisseur(Base):
    __tablename__ = "suivis_reglement_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    facture_fournisseur_id = Column(Integer, ForeignKey("factures_fournisseur.id", ondelete="CASCADE"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    montant = Column(Float, nullable=False)
    mode_paiement = Column(String(100), nullable=False)
    statut = Column(String(50), default="prévu", comment="prévu, payé, rejeté")
    commentaire = Column(Text, nullable=True)

    date_reglement = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    facture_fournisseur = relationship("FactureFournisseur", back_populates="reglements")
    entreprise = relationship("Entreprise", back_populates="reglements_fournisseur")
    utilisateur = relationship("Utilisateur", back_populates="reglements_fournisseur")

    def __repr__(self):
        return f"<SuiviReglementFournisseur(facture={self.facture_fournisseur_id}, montant={self.montant})>"