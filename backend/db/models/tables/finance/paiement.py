from sqlalchemy import Column, Integer, Float, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Paiement(Base):
    __tablename__ = "paiements"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    facture_id = Column(Integer, ForeignKey("factures.id", ondelete="CASCADE"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    montant = Column(Float, nullable=False)
    mode_paiement = Column(String(100), nullable=False, comment="espèces, virement, carte…")
    reference = Column(String(100), nullable=True)
    commentaire = Column(Text, nullable=True)

    date_paiement = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    facture = relationship("Facture", back_populates="paiements")
    entreprise = relationship("Entreprise", back_populates="paiements")
    utilisateur = relationship("Utilisateur", back_populates="paiements")

    def __repr__(self):
        return f"<Paiement(montant={self.montant}, facture={self.facture_id})>"