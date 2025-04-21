from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= FOURNISSEURS =========================
class Fournisseur(Base):
    __tablename__ = "fournisseurs"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom du fournisseur")
    contact = Column(
        String(100), nullable=True, comment="Contact principal du fournisseur"
    )
    email = Column(String(150), nullable=True, comment="Email du fournisseur")
    telephone = Column(String(50), nullable=True, comment="Téléphone du fournisseur")
    adresse = Column(String(255), nullable=True, comment="Adresse du fournisseur")
    tva = Column(String(50), nullable=True, comment="Numéro de TVA du fournisseur")
    site_web = Column(String(255), nullable=True, comment="Site web du fournisseur")
    catalogue_interactif = Column(
        String(255), nullable=True, comment="URL ou fichier PDF du catalogue interactif"
    )
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création du fournisseur",
    )

    # Relations
    materiaux = relationship(
        "Materiau", back_populates="fournisseur", cascade="all, delete-orphan"
    )
    outils = relationship(
        "Outil", back_populates="fournisseur", cascade="all, delete-orphan"
    )
    evaluations = relationship(
        "EvaluationFournisseur",
        back_populates="fournisseur",
        cascade="all, delete-orphan",
    )
    finances = relationship(
        "Finance", back_populates="fournisseur", cascade="all, delete-orphan"
    )
    filtres = relationship(
        "GestionFiltrage", back_populates="fournisseur", cascade="all, delete-orphan"
    )