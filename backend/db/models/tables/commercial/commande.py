from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Commande(Base):
    __tablename__ = "commandes"
    __table_args__ = (
        CheckConstraint(
            "statut IN ('en cours', 'terminée', 'annulée')",
            name="check_statut_commande_client"
        ),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)
    code_commande = Column(String(50), unique=True, nullable=False)
    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_validation = Column(DateTime(timezone=True), nullable=True)
    statut = Column(String(50), nullable=False, default="en cours")
    commentaire = Column(String(255), nullable=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    devis_id = Column(Integer, ForeignKey("devis.id", ondelete="SET NULL"), nullable=True)

    # Relations
    client = relationship("Client", back_populates="commandes")
    devis = relationship("Devis", back_populates="commandes")
    lignes = relationship("LigneCommande", back_populates="commande", cascade="all, delete-orphan")
    facture = relationship("Facture", back_populates="commande", uselist=False)
    pieces = relationship("CommandePiece", back_populates="commande", cascade="all, delete-orphan")
    


    def __repr__(self):
        return f"<Commande(code={self.code_commande}, client={self.client_id})>"
