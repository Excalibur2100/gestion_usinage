from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class GestionFiltrage(Base):
    __tablename__ = "gestion_filtrage"

    id = Column(Integer, primary_key=True, index=True)
    nom_filtre = Column(String, nullable=False)
    niveau = Column(Integer, nullable=False)
    actif = Column(Boolean, default=True)

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
