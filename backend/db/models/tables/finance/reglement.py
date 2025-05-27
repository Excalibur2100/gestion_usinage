from sqlalchemy import Column, Integer, Float, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Reglement(Base):
    __tablename__ = "reglements"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    facture_id = Column(Integer, ForeignKey("factures.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    montant = Column(Float, nullable=False)
    mode = Column(String(100), nullable=False, comment="Mode de paiement : virement, carte, chèque...")
    statut = Column(String(50), default="enregistré", comment="enregistré, encaissé, rejeté")
    commentaire = Column(Text, nullable=True)

    date_reglement = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    entreprise = relationship("Entreprise", back_populates="reglements")
    utilisateur = relationship("Utilisateur", back_populates="reglements")
    facture = relationship("Facture", back_populates="reglements")

    def __repr__(self):
        return f"<Reglement(montant={self.montant}, mode='{self.mode}', statut='{self.statut}')>"