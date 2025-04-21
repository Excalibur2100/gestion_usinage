from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= FACTURES =========================
class Facture(Base):
    __tablename__ = "factures"

    id = Column(Integer, primary_key=True)
    commande_id = Column(
        Integer,
        ForeignKey("commandes.id"),
        nullable=False,
        comment="ID de la commande associée",
    )
    montant_total = Column(Float, nullable=False, comment="Montant total de la facture")
    date_emission = Column(
        DateTime, nullable=False, comment="Date d'émission de la facture"
    )
    statut = Column(
        String(50),
        nullable=False,
        default="En attente",
        comment="Statut de la facture (payée, impayée, annulée)",
    )

    # Relations
    commande = relationship("Commande", back_populates="facture")
    lignes = relationship(
        "LigneFacture", back_populates="facture", cascade="all, delete-orphan"
    )

    # Contraintes
    __table_args__ = (
        CheckConstraint(
            "statut IN ('En attente', 'Validée', 'Payée', 'Annulée')",
            name="check_statut_facture",
        ),
    )
