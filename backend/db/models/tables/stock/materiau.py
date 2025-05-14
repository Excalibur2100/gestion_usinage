from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Materiau(Base):
    __tablename__ = "materiaux"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom du matériau")
    type = Column(String(50), nullable=False, default="Acier", comment="Type (ex: Acier, Aluminium)")
    afnor = Column(String(100), nullable=True, comment="Norme AFNOR ou équivalent")
    durete = Column(String(100), nullable=True, comment="Dureté du matériau")
    stock = Column(Float, default=0.0, nullable=False, comment="Quantité en stock (kg)")
    certificat = Column(String(255), nullable=True, comment="Numéro ou chemin du certificat")
    certificat_matiere = Column(String(255), nullable=True, comment="Certificat matière si distinct")
    est_aeronautique = Column(Boolean, default=False, comment="Certifié pour l'aéronautique ?")

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="SET NULL"), nullable=True)
    emplacement_id = Column(Integer, ForeignKey("emplacements.id", ondelete="SET NULL"), nullable=True)

    # Relations
    fournisseur = relationship("Fournisseur", back_populates="materiaux", lazy="joined")
    emplacement = relationship("EmplacementStock", back_populates="materiaux", lazy="joined")
    gammes = relationship("GammeProduction", back_populates="materiau", cascade="all, delete-orphan", lazy="joined")
    non_conformites = relationship("NonConformite", back_populates="machine/materiau/outil/instrument", cascade="all, delete-orphan")
    finance = relationship("Finance", back_populates="materiau", lazy="joined")
    qhse = relationship("QHSE", back_populates="materiau", lazy="joined")

    __table_args__ = (
        CheckConstraint("stock >= 0", name="check_stock_positif_materiau"),
    )

    def __repr__(self):
        return f"<Materiau {self.nom} ({self.type}) stock={self.stock}kg>"
