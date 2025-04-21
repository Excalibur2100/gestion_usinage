from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= OUTILS =========================
class Outil(Base):
    __tablename__ = "outils"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'outil")
    type = Column(
        String(50), nullable=False, comment="Type de l'outil (ex: fraise, foret)"
    )
    stock = Column(Integer, default=0, nullable=False, comment="Quantité en stock")
    etat = Column(
        String(50),
        default="neuf",
        nullable=False,
        comment="État de l'outil (neuf, utilisé, cassé)",
    )
    diametre = Column(Float, nullable=True, comment="Diamètre de l'outil (en mm)")
    longueur = Column(Float, nullable=True, comment="Longueur de l'outil (en mm)")
    rayon = Column(Float, nullable=True, comment="Rayon de la plaquette (en mm)")
    fournisseur_id = Column(
        Integer,
        ForeignKey("fournisseurs.id"),
        nullable=True,
        comment="ID du fournisseur associé",
    )
    emplacement_id = Column(
        Integer,
        ForeignKey("emplacements.id"),
        nullable=True,
        comment="ID de l'emplacement associé",
    )

    ref_fournisseur = Column(String(100))

    # Relations
    fournisseur = relationship("Fournisseur", back_populates="outils", cascade="all, delete-orphan")
    emplacement = relationship("EmplacementStock", back_populates="outils", cascade="all, delete-orphan")
    gammes = relationship("GammeProduction", back_populates="outil", cascade="all, delete-orphan")
    non_conformites = relationship("NonConformite", back_populates="outil", cascade="all, delete-orphan")