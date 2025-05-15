from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nom_entreprise = Column(String(255), nullable=False, index=True)
    siret = Column(String(14), nullable=True, unique=True)
    adresse = Column(String(255), nullable=True)
    code_postal = Column(String(10), nullable=True)
    ville = Column(String(100), nullable=True)
    pays = Column(String(100), default="France")
    tva_intracom = Column(String(20), nullable=True)
    notes = Column(Text, nullable=True)

    nom_contact = Column(String(100), nullable=True)
    prenom_contact = Column(String(100), nullable=True)
    email_contact = Column(String(255), nullable=True)
    telephone_contact = Column(String(30), nullable=True)

    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    devis = relationship("Devis", back_populates="client", cascade="all, delete-orphan", lazy="selectin")
    commandes = relationship("CommandeClient", back_populates="client", cascade="all, delete-orphan", lazy="selectin")
    factures = relationship("Facture", back_populates="client", cascade="all, delete-orphan", lazy="selectin")
    pieces = relationship("Piece", back_populates="client", cascade="all, delete-orphan", lazy="selectin")
