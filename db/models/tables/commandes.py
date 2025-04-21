from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= COMMANDES =========================
class Commande(Base):
    __tablename__ = "commandes"

    id = Column(Integer, primary_key=True)
    client_id = Column(
        Integer,
        ForeignKey("clients.id"),
        nullable=False,
        comment="ID du client associé",
    )
    devis_id = Column(
        Integer, ForeignKey("devis.id"), nullable=True, comment="ID du devis associé"
    )
    date_validation = Column(
        DateTime, nullable=False, comment="Date de validation de la commande"
    )
    statut = Column(
        String(50),
        nullable=False,
        comment="Statut de la commande (en cours, terminée, annulée)",
    )
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création de la commande",
    )

    # Relations
    client = relationship("Client", back_populates="commandes")
    devis = relationship("Devis", back_populates="commandes")
    pieces = relationship(
        "CommandePiece", back_populates="commande", cascade="all, delete-orphan"
    )
    facture = relationship("Facture", back_populates="commande", uselist=False)

    # Contraintes
    __table_args__ = (
        CheckConstraint(
            "statut IN ('en cours', 'terminée', 'annulée')",
            name="check_statut_commande",
        ),
    )
