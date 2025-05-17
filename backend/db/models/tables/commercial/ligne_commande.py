from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class LigneCommande(Base):
    __tablename__ = "lignes_commande"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)

    commande_id = Column(Integer, ForeignKey("commandes.id", ondelete="CASCADE"), nullable=False)
    produit_id = Column(Integer, ForeignKey("produits.id", ondelete="CASCADE"), nullable=False)

    designation = Column(String(255), nullable=False)
    quantite = Column(Float, nullable=False)
    unite = Column(String(50), nullable=False)
    prix_unitaire = Column(Float, nullable=False)
    remise = Column(Float, default=0.0)
    commentaire = Column(Text, nullable=True)
    statut_livraison = Column(String(50), default="non livré")

    # Relations
    commande = relationship("Commande", back_populates="lignes")
    produit = relationship("Produit", back_populates="lignes_commande")

    def __repr__(self):
        return f"<LigneCommande(designation='{self.designation}', qty={self.quantite})>"
