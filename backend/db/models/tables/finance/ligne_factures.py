from sqlalchemy import Column, Integer, Float, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class LigneFacture(Base):
    __tablename__ = "ligne_factures"

    id = Column(Integer, primary_key=True)

    facture_id = Column(
        Integer,
        ForeignKey("factures.id", ondelete="CASCADE"),
        nullable=False,
        comment="Facture concernée"
    )

    description = Column(Text, nullable=False, comment="Détail de la ligne")
    quantite = Column(Integer, nullable=False, comment="Quantité")
    prix_unitaire = Column(Float, nullable=False, comment="Prix unitaire")
    total = Column(Float, nullable=False, comment="Montant total de cette ligne")

    facture = relationship("Facture", back_populates="lignes", lazy="joined")

    __table_args__ = (
        CheckConstraint("quantite >= 0", name="check_quantite_ligne"),
        CheckConstraint("prix_unitaire >= 0", name="check_prix_ligne"),
        CheckConstraint("total >= 0", name="check_total_ligne"),
    )

    def __repr__(self):
        return f"<LigneFacture facture_id={self.facture_id} total={self.total}>"
