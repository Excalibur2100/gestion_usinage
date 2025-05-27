from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class JournalComptable(Base):
    __tablename__ = "journal_comptable"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    type_ecriture = Column(String(100), nullable=False, comment="facture, paiement, règlement...")
    reference = Column(String(100), nullable=True)
    libelle = Column(String(255), nullable=True)

    montant_debit = Column(Float, nullable=False, default=0.0)
    montant_credit = Column(Float, nullable=False, default=0.0)

    commentaire = Column(Text, nullable=True)
    date_ecriture = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    entreprise = relationship("Entreprise", back_populates="ecritures_comptables")
    utilisateur = relationship("Utilisateur", back_populates="ecritures_comptables")

    def __repr__(self):
        return f"<JournalComptable({self.type_ecriture} {self.reference})>"