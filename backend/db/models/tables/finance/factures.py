from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Facture(Base):
    __tablename__ = "factures"

    id = Column(Integer, primary_key=True)

    code_facture = Column(String(50), unique=True, nullable=False, comment="Code unique de la facture (ex: FAC-2024-001)")

    commande_id = Column(
        Integer,
        ForeignKey("commandes.id", ondelete="CASCADE"),
        nullable=False,
        comment="Commande associée"
    )

    montant_total = Column(Float, nullable=False, comment="Montant TTC")
    date_emission = Column(DateTime, nullable=False, comment="Date d'émission")
    date_echeance = Column(DateTime, nullable=False, comment="Date limite de paiement")

    statut = Column(String(50), default="En attente", nullable=False, comment="Statut : En attente, Validée, Payée, Annulée")
    commentaire = Column(String(255), nullable=True, comment="Remarques internes")
    url_facture = Column(String(255), nullable=True, comment="Lien vers le PDF de la facture")

    commande = relationship("Commande", back_populates="facture", lazy="joined")

    lignes = relationship("LigneFacture", back_populates="facture", cascade="all, delete-orphan", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "statut IN ('En attente', 'Validée', 'Payée', 'Annulée')",
            name="check_statut_facture"
        ),
        CheckConstraint(
            "montant_total >= 0",
            name="check_montant_facture"
        ),
    )

    def __repr__(self):
        return f"<Facture code={self.code_facture} statut={self.statut}>"
