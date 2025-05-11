from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class GestionFiltrage(Base):
    __tablename__ = "gestion_filtrage"

    id = Column(Integer, primary_key=True, index=True)

    filtre = Column(String(100), nullable=False, comment="Nom du filtre (ex: statut, type, niveau)")
    valeur = Column(String(255), nullable=False, comment="Valeur appliquée (ex: actif, manager, client)")
    actif = Column(Boolean, default=True, comment="Filtre activé ?")

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True)
    commande_id = Column(Integer, ForeignKey("commandes.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="SET NULL"), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="filtres", lazy="joined")
    client = relationship("Client", back_populates="filtres", lazy="joined")
    commande = relationship("Commande", back_populates="filtres", lazy="joined")
    fournisseur = relationship("Fournisseur", back_populates="filtres", lazy="joined")

    def __repr__(self):
        return f"<GestionFiltrage filtre={self.filtre} valeur={self.valeur} actif={self.actif}>"
