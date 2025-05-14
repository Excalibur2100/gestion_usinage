from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Devis(Base):
    __tablename__ = "devis"

    id = Column(Integer, primary_key=True)

    code_devis = Column(String(50), unique=True, nullable=False, comment="Code unique du devis")
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False, comment="Client concerné")

    montant_total = Column(Float, nullable=False, comment="Montant TTC du devis")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'émission")
    date_livraison_souhaitee = Column(DateTime, nullable=True, comment="Date de livraison souhaitée")
    
    statut = Column(String(50), nullable=False, default="brouillon", comment="Statut : brouillon, validé, annulé")

    # Relations
    client = relationship("Client", back_populates="devis", lazy="joined")
    commandes = relationship("Commande", back_populates="devis", cascade="all, delete-orphan", lazy="joined")

    # Contraintes
    __table_args__ = (
        CheckConstraint(
            "statut IN ('brouillon', 'validé', 'annulé')",
            name="check_statut_devis"
        ),
    )

    def __repr__(self):
        return f"<Devis code={self.code_devis} client={self.client_id} statut={self.statut}>"
