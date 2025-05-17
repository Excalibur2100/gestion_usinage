from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base


class Entreprise(Base):
    __tablename__ = "entreprises"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False, unique=True)
    raison_sociale = Column(String(255), nullable=True)
    type_entreprise = Column(String(100), nullable=True)
    siret = Column(String(20), nullable=True)
    tva_intra = Column(String(30), nullable=True)
    email = Column(String(255), nullable=True)
    telephone = Column(String(50), nullable=True)
    adresse = Column(Text, nullable=True)
    pays = Column(String(100), default="France")
    site_web = Column(String(255), nullable=True)
    logo = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    date_creation = Column(DateTime(timezone=True), server_default=func.now())
    actif = Column(Boolean, default=True)

    # 🔗 RELATIONS vers d'autres entités
    utilisateurs = relationship("Utilisateur", back_populates="entreprise", cascade="all, delete-orphan")
    clients = relationship("Client", back_populates="entreprise", cascade="all, delete-orphan")
    fournisseurs = relationship("Fournisseur", back_populates="entreprise", cascade="all, delete-orphan")
    machines = relationship("Machine", back_populates="entreprise", cascade="all, delete-orphan")
    produits = relationship("Produit", back_populates="entreprise", cascade="all, delete-orphan")
    ordres_fabrication = relationship("OrdreFabrication", back_populates="entreprise", cascade="all, delete-orphan")
    documents = relationship("DocumentQualite", back_populates="entreprise", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Entreprise(id={self.id}, nom='{self.nom}')>"
