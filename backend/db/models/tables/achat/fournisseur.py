from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Fournisseur(Base):
    __tablename__ = "fournisseurs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    code_fournisseur = Column(String(50), unique=True, nullable=False, comment="Code fournisseur unique")
    nom = Column(String(100), nullable=False, comment="Nom du fournisseur")
    contact = Column(String(100), nullable=True, comment="Contact principal")
    email = Column(String(150), nullable=True, comment="Email")
    telephone = Column(String(50), nullable=True, comment="Téléphone")
    adresse = Column(String(255), nullable=True, comment="Adresse")
    tva = Column(String(50), nullable=True, comment="Numéro de TVA")
    site_web = Column(String(255), nullable=True, comment="Site web")
    catalogue_interactif = Column(String(255), nullable=True, comment="Lien ou fichier PDF")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'enregistrement")

    type_id = Column(Integer, ForeignKey("types_fournisseur.id", ondelete="SET NULL"), nullable=True)

    # Relations
    type_fournisseur = relationship("TypeFournisseur", back_populates="fournisseurs")
    factures_fournisseur = relationship("FactureFournisseur", back_populates="entreprise", cascade="all, delete-orphan")
    commandes = relationship("CommandeFournisseur", back_populates="fournisseur", cascade="all, delete-orphan")
    factures = relationship("FactureFournisseur", back_populates="fournisseur", cascade="all, delete-orphan")
    avoirs = relationship("AvoirFournisseur", back_populates="fournisseur", cascade="all, delete-orphan")
    evaluations = relationship("EvaluationFournisseur", back_populates="fournisseur", cascade="all, delete-orphan")
    reglements = relationship("SuiviReglementFournisseur", back_populates="fournisseur", cascade="all, delete-orphan")

    materiaux = relationship("Materiau", back_populates="fournisseur", cascade="all, delete-orphan", lazy="joined")
    outils = relationship("Outil", back_populates="fournisseur", cascade="all, delete-orphan", lazy="joined")


    def __repr__(self):
        return f"<Fournisseur {self.code_fournisseur} - {self.nom}>"
