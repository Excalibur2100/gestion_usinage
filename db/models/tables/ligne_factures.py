from sqlalchemy import Column, Integer,Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= LIGNE FACTURE =========================
class LigneFacture(Base):
    __tablename__ = "ligne_factures"

    id = Column(Integer, primary_key=True)
    facture_id = Column(
        Integer,
        ForeignKey("factures.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la facture associée",
    )
    description = Column(
        Text, nullable=False, comment="Description de la ligne de facture"
    )
    quantite = Column(Integer, nullable=False, comment="Quantité facturée")
    prix_unitaire = Column(Float, nullable=False, comment="Prix unitaire")
    total = Column(
        Float, nullable=False, comment="Total de la ligne (quantité * prix unitaire)"
    )

    # Relations
    facture = relationship("Facture", back_populates="lignes")
