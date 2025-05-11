from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'entreprise cliente")
    email = Column(String(150), unique=True, nullable=True, comment="Email principal du client")
    telephone = Column(String(50), nullable=True, comment="Téléphone de contact")
    adresse = Column(String(255), nullable=True, comment="Adresse postale")
    
    siret = Column(String(20), nullable=True, comment="Numéro SIRET")
    tva_intracom = Column(String(20), nullable=True, comment="Numéro de TVA intracommunautaire")
    secteur_activite = Column(String(100), nullable=True, comment="Secteur d'activité")
    site_web = Column(String(150), nullable=True, comment="Site internet")
    commentaire = Column(Text, nullable=True, comment="Remarques commerciales ou logistiques")

    # Relations
    devis = relationship("Devis", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    commandes = relationship("Commande", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    factures = relationship("Facture", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    filtres = relationship("GestionFiltrage", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    pieces = relationship("Piece", back_populates="client", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Client {self.nom}>"
