from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class LigneCommandeFournisseur(Base):
    __tablename__ = "lignes_commande_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)

    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id", ondelete="CASCADE"), nullable=False)
    produit_id = Column(Integer, ForeignKey("produits.id", ondelete="CASCADE"), nullable=False)

    designation = Column(String(255), nullable=False)
    quantite = Column(Float, nullable=False)
    unite = Column(String(50), nullable=False)
    prix_unitaire = Column(Float, nullable=False)
    remise = Column(Float, default=0.0)
    commentaire = Column(Text, nullable=True)
    statut_reception = Column(String(50), default="non reçu")

    # Relations
    commande = relationship("CommandeFournisseur", back_populates="lignes_commande")
    produit = relationship("Produit", back_populates="lignes_commande_fournisseur")
    receptions = relationship("Reception", back_populates="ligne_commande", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<LigneCommandeFournisseur(designation='{self.designation}', qty={self.quantite})>"
