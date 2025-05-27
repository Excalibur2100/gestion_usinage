from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Facture(Base):
    __tablename__ = "factures"
    __table_args__ = (
        CheckConstraint("statut IN ('brouillon', 'envoyée', 'payée', 'annulée')", name="check_statut_facture"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)

    code_facture = Column(String(50), unique=True, nullable=False)
    commande_id = Column(Integer, ForeignKey("commandes.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    date_emission = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_echeance = Column(DateTime(timezone=True), nullable=True)

    total_ht = Column(Float, default=0.0, nullable=False)
    total_ttc = Column(Float, default=0.0, nullable=False)

    statut = Column(String(50), nullable=False, default="brouillon")
    commentaire = Column(Text, nullable=True)

    entreprise = relationship("Entreprise", back_populates="factures")
    utilisateur = relationship("Utilisateur", back_populates="factures")
    commande = relationship("Commande", back_populates="facture")
    lignes = relationship("LigneFacture", back_populates="facture", cascade="all, delete-orphan")
    paiements = relationship("Paiement", back_populates="entreprise", cascade="all, delete-orphan")
    reglements = relationship("Reglement", back_populates="facture", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Facture(code='{self.code_facture}', statut='{self.statut}')>"