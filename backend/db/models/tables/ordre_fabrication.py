from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class OrdreFabrication(Base):
    __tablename__ = "ordres_fabrication"

    id = Column(Integer, primary_key=True, index=True)

    numero = Column(String(50), unique=True, nullable=False, comment="Numéro unique de l'ordre de fabrication")

    produit_id = Column(Integer, ForeignKey("produits.id", ondelete="SET NULL"), nullable=True, comment="Produit fabriqué")
    poste_id = Column(Integer, ForeignKey("postes.id", ondelete="SET NULL"), nullable=True, comment="Poste de fabrication assigné")
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True, comment="Opérateur en charge")

    date_lancement = Column(Date, nullable=False, comment="Date de démarrage prévue")
    date_fin = Column(Date, nullable=True, comment="Date de fin prévue ou effective")
    
    statut = Column(String(30), default="prévu", nullable=False, comment="Statut : prévu, en cours, terminé, annulé")
    commentaire = Column(Text, nullable=True, comment="Remarques complémentaires")

    produit = relationship("Produit", back_populates="ordres", lazy="joined")
    poste = relationship("Poste", back_populates="ordres", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="ordres", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('prévu', 'en cours', 'terminé', 'annulé')", name="check_statut_of"),
    )

    def __repr__(self):
        return f"<OrdreFabrication #{self.numero}>"
