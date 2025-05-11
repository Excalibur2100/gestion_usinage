from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= COMMANDES CLIENTS =========================
class Commande(Base):
    __tablename__ = "commandes"

    id = Column(Integer, primary_key=True)

    code_commande = Column(
        String(50), unique=True, nullable=False, comment="Code unique de la commande client"
    )

    client_id = Column(
        Integer,
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID du client associé",
    )
    devis_id = Column(
        Integer,
        ForeignKey("devis.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID du devis associé",
    )

    date_validation = Column(
        DateTime,
        nullable=False,
        comment="Date de validation de la commande",
    )
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création de la commande",
    )

    statut = Column(
        String(50),
        nullable=False,
        default="en cours",
        comment="Statut de la commande (en cours, terminée, annulée)",
    )

    # Relations
    client = relationship("Client", back_populates="commandes")
    filtres = relationship("GestionFiltrage", back_populates="commande", cascade="all, delete-orphan")
    devis = relationship("Devis", back_populates="commandes")
    pieces = relationship(
        "CommandePiece", back_populates="commande", cascade="all, delete-orphan"
    )
    facture = relationship("Facture", back_populates="commande", uselist=False, cascade="all, delete-orphan")


    # Contraintes SQL
    __table_args__ = (
        CheckConstraint(
            "statut IN ('en cours', 'terminée', 'annulée')",
            name="check_statut_commande",
        ),
    )

    def __repr__(self):
        return f"<Commande code={self.code_commande} client={self.client_id}>"
