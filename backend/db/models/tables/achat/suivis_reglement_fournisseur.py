from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class SuiviReglementFournisseur(Base):
    __tablename__ = "suivi_reglement_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)

    date_reglement = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    montant_paye = Column(Float, nullable=False)
    mode_paiement = Column(String(100), nullable=True)
    statut = Column(String(50), default="en attente")
    commentaire = Column(Text, nullable=True)

    facture_id = Column(Integer, ForeignKey("factures_fournisseur.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    # Relations
    facture = relationship("FactureFournisseur", back_populates="reglements")
    utilisateur = relationship("Utilisateur", back_populates="reglements_fournisseur")

    def __repr__(self):
        return f"<SuiviReglementFournisseur(facture={self.facture_id}, montant={self.montant_paye})>"
