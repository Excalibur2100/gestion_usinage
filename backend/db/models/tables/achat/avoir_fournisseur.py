from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class AvoirFournisseur(Base):
    """
    Représente un avoir lié à une facture fournisseur.
    Utilisé pour les remboursements partiels, erreurs de facturation ou remises.
    """
    __tablename__ = "avoirs_fournisseur"
    __table_args__ = (
        CheckConstraint("montant >= 0", name="check_montant_avoir_positive"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True, index=True)
    numero_avoir = Column(String(100), unique=True, nullable=False, comment="Référence unique de l'avoir")
    date_avoir = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, comment="Date d'émission de l'avoir")
    montant = Column(Float, nullable=False, comment="Montant total TTC de l'avoir")
    motif = Column(Text, nullable=True, comment="Raison de l'avoir")
    statut = Column(String(50), default="non imputé", comment="Statut de l'avoir : non imputé / imputé")

    facture_id = Column(Integer, ForeignKey("factures_fournisseur.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="CASCADE"), nullable=False)

    # Relations
    facture = relationship("FactureFournisseur", back_populates="avoirs")
    fournisseur = relationship("Fournisseur", back_populates="avoirs")