from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Client(Base):
    __tablename__ = "clients"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    code_client = Column(String(50), unique=True, nullable=False)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), nullable=True)
    telephone = Column(String(50), nullable=True)
    site_web = Column(String(255), nullable=True)
    tva = Column(String(50), nullable=True)
    actif = Column(Boolean, default=True)
    segment_id = Column(Integer, ForeignKey("segments_client.id", ondelete="SET NULL"), nullable=True)
    commentaire = Column(Text, nullable=True)
    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)



    # Relations
    segment = relationship("SegmentClient", back_populates="clients")
    adresses = relationship("AdresseClient", back_populates="client", cascade="all, delete-orphan")
    fichiers = relationship("FichierClient", back_populates="client", cascade="all, delete-orphan")
    contacts = relationship("ContactClient", back_populates="client", cascade="all, delete-orphan")
    commandes = relationship("Commande", back_populates="client", cascade="all, delete-orphan")
    devis = relationship("Devis", back_populates="client", cascade="all, delete-orphan")
    relances = relationship("Relance", back_populates="client", cascade="all, delete-orphan")
    pieces = relationship("Piece", back_populates="client", cascade="all, delete-orphan")
    historique_prix = relationship("HistoriquePrixClient", back_populates="client", cascade="all, delete-orphan")
    portefeuilles = relationship("PortefeuilleClient", back_populates="client", cascade="all, delete-orphan")
    remises = relationship("RemiseClient", back_populates="client", cascade="all, delete-orphan")
    actions_commerciales = relationship("ActionCommerciale", back_populates="client", cascade="all, delete-orphan")
    historiques = relationship("HistoriqueClient", back_populates="client", cascade="all, delete-orphan")
    opportunites = relationship("Opportunite", back_populates="client", cascade="all, delete-orphan")
    tags = relationship("TagClient", back_populates="client", cascade="all, delete-orphan")
    entreprise = relationship("Entreprise", back_populates="clients")
    marges = relationship("ConfigMarge", back_populates="client", cascade="all, delete-orphan")
    pieces_chiffrages = relationship("ChiffragePiece", back_populates="client", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Client(code='{self.code_client}', nom='{self.nom}')>"