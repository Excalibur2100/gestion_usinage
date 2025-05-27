from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Devis(Base):
    __tablename__ = "devis"
    __table_args__ = (
        CheckConstraint("statut IN ('brouillon', 'envoyé', 'accepté', 'refusé')", name="check_statut_devis"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)

    code_devis = Column(String(50), unique=True, nullable=False, comment="Identifiant unique du devis")
    
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_validite = Column(DateTime(timezone=True), nullable=True)

    statut = Column(String(50), nullable=False, default="brouillon", comment="Statut du devis")
    commentaire = Column(Text, nullable=True)
    
    total_ht = Column(Float, nullable=False, default=0.0)
    total_ttc = Column(Float, nullable=False, default=0.0)

    # Relations
    client = relationship("Client", back_populates="devis")
    entreprise = relationship("Entreprise", back_populates="devis")
    utilisateur = relationship("Utilisateur", back_populates="devis")

    lignes = relationship("LigneDevis", back_populates="devis", cascade="all, delete-orphan")
    commandes = relationship("Commande", back_populates="devis", cascade="all, delete-orphan")
    commissions = relationship("Commission", back_populates="devis", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Devis(code='{self.code_devis}', client={self.client_id}, statut='{self.statut}')>"