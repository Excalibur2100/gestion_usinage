from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

# ========================= OUTILS =========================
class Outil(Base):
    __tablename__ = "outils"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    stock = Column(Integer, default=0)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))
    etat = Column(String(50), default="neuf")  # neuf, utilisé, cassé
    emplacement_id = Column(Integer, ForeignKey("emplacements.id"))

    fournisseur = relationship("Fournisseur", back_populates="outils")
    emplacement = relationship("EmplacementStock", back_populates="outils")

# ========================= MATERIAUX =========================
class Materiau(Base):
    __tablename__ = "materiaux"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    stock = Column(Float, default=0.0)
    certificat = Column(String(255), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))
    emplacement_id = Column(Integer, ForeignKey("emplacements.id"))

    fournisseur = relationship("Fournisseur", back_populates="materiaux")
    emplacement = relationship("EmplacementStock", back_populates="materiaux")

# ========================= EMPLACEMENT STOCK =========================
class EmplacementStock(Base):
    __tablename__ = "emplacements"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)  # armoire, rack, bac, etc.
    capacite = Column(Float, nullable=False)
    occupation_actuelle = Column(Float, default=0.0)

    outils = relationship("Outil", back_populates="emplacement")
    materiaux = relationship("Materiau", back_populates="emplacement")