from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from db.models.database import Base

class OrdreFabrication(Base):
    __tablename__ = "ordres_fabrication"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(50), unique=True, nullable=False, comment="Numéro OF unique")
    produit_id = Column(Integer, ForeignKey("produits.id"), nullable=True, comment="Produit concerné")
    poste_id = Column(Integer, ForeignKey("postes.id"), nullable=True, comment="Poste de fabrication")
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True, comment="Opérateur assigné")

    date_lancement = Column(Date, nullable=False, comment="Date de lancement prévue")
    date_fin = Column(Date, nullable=True, comment="Date de fin estimée")
    statut = Column(String(30), default="prévu", comment="Statut : prévu, en cours, terminé, annulé")
    commentaire = Column(Text, nullable=True, comment="Informations complémentaires")

    poste = relationship("Poste", back_populates="ordres")
    utilisateur = relationship("Utilisateur", back_populates="ordres")
    produit = relationship("Produit", back_populates="ordres", lazy="joined")

    def __repr__(self):
        return f"<OrdreFabrication #{self.numero}>"
