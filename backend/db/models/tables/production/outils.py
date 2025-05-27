from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Outil(Base):
    __tablename__ = "outils"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom de l'outil")
    type = Column(String(50), nullable=False, comment="Type (fraise, foret, etc.)")
    stock = Column(Integer, default=0, nullable=False, comment="Quantité disponible en stock")
    etat = Column(String(50), default="neuf", nullable=False, comment="État : neuf, utilisé, cassé")
    diametre = Column(Float, nullable=True, comment="Diamètre (mm)")
    longueur = Column(Float, nullable=True, comment="Longueur (mm)")
    rayon = Column(Float, nullable=True, comment="Rayon (mm)")
    ref_fournisseur = Column(String(100), nullable=True, comment="Référence catalogue fournisseur")

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="SET NULL"), nullable=True)
    emplacement_id = Column(Integer, ForeignKey("emplacements.id", ondelete="SET NULL"), nullable=True)

    # Relations
    fournisseur = relationship("Fournisseur", back_populates="outils", lazy="joined")
    emplacement = relationship("EmplacementStock", back_populates="outils", lazy="joined")
    gammes = relationship("GammeProduction", back_populates="outil", cascade="all, delete-orphan", lazy="joined")
    non_conformites = relationship("NonConformite", back_populates="outil", cascade="all, delete-orphan", lazy="joined")
    machines = relationship("Machine", secondary="machine_outil", back_populates="outils", lazy="joined")
    conditions_coupe = relationship("ConditionsCoupe", back_populates="outil", cascade="all, delete-orphan")
    suggestions_ia = relationship("SuggestionOutil", back_populates="outil", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("etat IN ('neuf', 'utilisé', 'cassé')", name="check_etat_outil"),
    )

    def __repr__(self):
        return f"<Outil nom={self.nom} type={self.type} etat={self.etat} stock={self.stock}>"
