from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

# ========================= MATERIAUX =========================
class Materiau(Base):
    __tablename__ = "materiaux"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom du matériau")
    type = Column(
        String(50),
        nullable=False,
        default="Acier",
        comment="Type de matériau (ex: Acier, Aluminium)",
    )

    afnor = Column(
        String(100))
    
    stock = Column(
        Float, default=0.0, nullable=False, comment="Quantité en stock (en kg)"
    )
    durete = Column(
        String(100))
    
    type = Column(
        String(50), default="Acier")
    
    certificat = Column(
        String(255), nullable=True, comment="Certificat du matériau (chemin ou numéro)"
    )
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
    est_aeronautique = Column(
        Boolean,
        default=False,
        comment="Indique si le matériau est certifié pour l'aéronautique",
    )
    certificat_matiere = Column(
        String(255), nullable=True
    )

    certificat = Column(
        String(255), nullable=True, comment="Certificat du matériau (chemin ou numéro)"
    )

    # Relations
    fournisseur = relationship("Fournisseur", back_populates="materiaux")
    emplacement = relationship("EmplacementStock", back_populates="materiaux")
    gammes = relationship("GammeProduction", back_populates="materiau")
    non_conformites = relationship("NonConformite", back_populates="materiau")
    finance = relationship("Finance", back_populates="materiau")
    qhse = relationship("QHSE", back_populates="materiau")