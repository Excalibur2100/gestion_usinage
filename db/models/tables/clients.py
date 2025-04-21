from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    telephone = Column(String(50))
    adresse = Column(String(255))
    siret = Column(String(20))
    tva_intracom = Column(String(20))
    secteur_activite = Column(String(100))
    site_web = Column(String(150))
    commentaire = Column(Text)

    # Relations
    devis = relationship("Devis", back_populates="client", cascade="all, delete-orphan")
    commandes = relationship(
        "Commande", back_populates="client", cascade="all, delete-orphan"
    )
    factures = relationship(
        "Facture", back_populates="client", cascade="all, delete-orphan"
    )
    filtres = relationship("GestionFiltrage", back_populates="client")
