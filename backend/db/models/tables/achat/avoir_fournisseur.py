from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class AvoirFournisseur(Base):
    __tablename__ = "avoirs_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)

    numero_avoir = Column(String(100), unique=True, nullable=False)
    date_avoir = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    montant = Column(Float, nullable=False)
    motif = Column(Text, nullable=True)
    statut = Column(String(50), default="non imputé")

    facture_id = Column(Integer, ForeignKey("factures_fournisseur.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="CASCADE"), nullable=False)

    # Relations
    facture = relationship("FactureFournisseur", back_populates="avoirs")  # ← à ajouter dans facture_fournisseur.py
    fournisseur = relationship("Fournisseur", back_populates="avoirs")     # ← à ajouter dans fournisseur.py

    def __repr__(self):
        return f"<AvoirFournisseur(num={self.numero_avoir}, montant={self.montant})>"
