from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class FactureFournisseur(Base):
    __tablename__ = "factures_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)

    numero_facture = Column(String(100), unique=True, nullable=False)
    date_facture = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_echeance = Column(DateTime(timezone=True), nullable=True)

    montant_ht = Column(Float, nullable=False)
    montant_tva = Column(Float, nullable=False)
    montant_ttc = Column(Float, nullable=False)

    statut = Column(String(50), default="non payé")
    commentaire = Column(Text, nullable=True)

    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="CASCADE"), nullable=False)

    # Relations
    commande = relationship("CommandeFournisseur", back_populates="facture")
    fournisseur = relationship("Fournisseur", back_populates="factures")
    avoirs = relationship("AvoirFournisseur", back_populates="facture", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<FactureFournisseur(num={self.numero_facture}, montant_ttc={self.montant_ttc})>"
