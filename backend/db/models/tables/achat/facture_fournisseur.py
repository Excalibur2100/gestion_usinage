from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class FactureFournisseur(Base):
    __tablename__ = "factures_fournisseur"
    __table_args__ = (
        CheckConstraint("statut IN ('en attente', 'payée', 'annulée')", name="check_statut_facture_fournisseur"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)

    code_facture = Column(String(50), unique=True, nullable=False)
    commande_fournisseur_id = Column(Integer, ForeignKey("commandes_fournisseur.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="SET NULL"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)

    date_facture = Column(DateTime(timezone=True), nullable=False, default=func.now())
    date_echeance = Column(DateTime(timezone=True), nullable=True)

    total_ht = Column(Float, nullable=False, default=0.0)
    total_ttc = Column(Float, nullable=False, default=0.0)

    statut = Column(String(50), nullable=False, default="en attente")
    commentaire = Column(Text, nullable=True)

    fournisseur = relationship("Fournisseur", back_populates="factures")
    commande_fournisseur = relationship("CommandeFournisseur", back_populates="facture")
    entreprise = relationship("Entreprise", back_populates="factures_fournisseur")
    reglements = relationship("SuiviReglementFournisseur", back_populates="facture_fournisseur", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<FactureFournisseur(code='{self.code_facture}', statut='{self.statut}')>"