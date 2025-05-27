from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Commission(Base):
    __tablename__ = "commissions"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)
    devis_id = Column(Integer, ForeignKey("devis.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)

    montant_base = Column(Float, nullable=False)
    taux_commission = Column(Float, nullable=False)
    montant_commission = Column(Float, nullable=False)

    statut = Column(String(50), default="à valider", comment="à valider, validée, payée")
    commentaire = Column(Text, nullable=True)

    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="commissions")
    devis = relationship("Devis", back_populates="commissions")
    entreprise = relationship("Entreprise", back_populates="commissions")

    def __repr__(self):
        return f"<Commission(utilisateur={self.utilisateur_id}, taux={self.taux_commission})>"