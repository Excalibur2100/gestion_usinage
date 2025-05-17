from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class CommandeFournisseur(Base):
    __tablename__ = "commandes_fournisseur"
    __table_args__ = (
        CheckConstraint(
            "statut IN ('brouillon', 'validée', 'reçue', 'annulée')",
            name="check_statut_commande_fournisseur"
        ),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)
    code_commande = Column(String(100), unique=True, nullable=False)
    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_validation = Column(DateTime(timezone=True), nullable=True)
    statut = Column(String(50), nullable=False, default="brouillon")
    commentaire = Column(Text, nullable=True)
    conditions_paiement = Column(String(255), nullable=True)

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="CASCADE"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)

    # Relations
    fournisseur = relationship("Fournisseur", back_populates="commandes")
    entreprise = relationship("Entreprise", back_populates="commandes_fournisseur")

    lignes_commande = relationship("LigneCommandeFournisseur", back_populates="commande", cascade="all, delete-orphan")
    facture = relationship("FactureFournisseur", back_populates="commande", uselist=False)
    receptions = relationship("Reception", back_populates="commande", cascade="all, delete-orphan")
    evaluations = relationship("EvaluationFournisseur", back_populates="commande")
    # TODO: à activer quand EvaluationFournisseur sera créé
    # 

    def __repr__(self):
        return f"<CommandeFournisseur(code={self.code_commande}, statut={self.statut})>"
