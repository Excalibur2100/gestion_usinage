from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class GestionFiltrage(Base):
    __tablename__ = "gestion_filtrage"

    id = Column(Integer, primary_key=True, index=True)
    filtre = Column(String(100), nullable=False, comment="Nom du filtre")
    valeur = Column(String(255), nullable=False, comment="Valeur associée au filtre")
    actif = Column(Boolean, default=True, comment="Indique si le filtre est actif")

    # Relations facultatives vers les entités filtrables
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=True)
    commande_id = Column(Integer, ForeignKey("commandes.id"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"), nullable=True)

    # ORM relationships
    utilisateur = relationship("Utilisateur", back_populates="filtres")
    client = relationship("Client", back_populates="filtres")
    commande = relationship("Commande", back_populates="filtres")
    fournisseur = relationship("Fournisseur", back_populates="filtres")

    def __repr__(self):
        return (
            f"<GestionFiltrage(id={self.id}, filtre={self.filtre}, valeur={self.valeur}, actif={self.actif})>"
        )