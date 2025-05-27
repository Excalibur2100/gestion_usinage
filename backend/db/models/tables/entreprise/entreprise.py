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

    # === RELATIONS COMPLÈTES
    utilisateurs = relationship("Utilisateur", back_populates="entreprise", cascade="all, delete-orphan")
    clients = relationship("Client", back_populates="entreprise", cascade="all, delete-orphan")
    fournisseurs = relationship("Fournisseur", back_populates="entreprise", cascade="all, delete-orphan")
    machines = relationship("Machine", back_populates="entreprise", cascade="all, delete-orphan")
    produits = relationship("Produit", back_populates="entreprise", cascade="all, delete-orphan")
    ordres_fabrication = relationship("OrdreFabrication", back_populates="entreprise", cascade="all, delete-orphan")
    documents = relationship("DocumentQualite", back_populates="entreprise", cascade="all, delete-orphan")
    commandes_client = relationship("Commande", back_populates="entreprise", cascade="all, delete-orphan")
    commande_pieces = relationship("CommandePiece", back_populates="entreprise", cascade="all, delete-orphan")
    opportunites = relationship("Opportunite", back_populates="entreprise", cascade="all, delete-orphan")
    devis = relationship("Devis", back_populates="entreprise", cascade="all, delete-orphan")
    commissions = relationship("Commission", back_populates="entreprise", cascade="all, delete-orphan")
    marges = relationship("ConfigMarge", back_populates="entreprise", cascade="all, delete-orphan")
    exports_comptables = relationship("ExportComptable", back_populates="entreprise", cascade="all, delete-orphan")
    factures = relationship("Facture", back_populates="entreprise", cascade="all, delete-orphan")
    factures_fournisseur = relationship("FactureFournisseur", back_populates="entreprise", cascade="all, delete-orphan")
    reglements = relationship("Reglement", back_populates="entreprise", cascade="all, delete-orphan")
    ecritures_comptables = relationship("JournalComptable", back_populates="entreprise", cascade="all, delete-orphan")
    reglements_fournisseur = relationship("SuiviReglementFournisseur", back_populates="entreprise", cascade="all, delete-orphan")
    documents_rh = relationship("DocumentRH", back_populates="entreprise", cascade="all, delete-orphan")
    documents_qhse = relationship("DocumentQHSE", back_populates="entreprise", cascade="all, delete-orphan")
    documents_qualite = relationship("DocumentQualite", back_populates="entreprise", cascade="all, delete-orphan")
    documents_reglementaires = relationship("DocumentReglementaire", back_populates="entreprise", cascade="all, delete-orphan")
    chiffrages = relationship("Chiffrage", back_populates="entreprise", cascade="all, delete-orphan")
    code_generations = relationship("CodeGenerator", back_populates="entreprise", cascade="all, delete-orphan")
    assistants_ia = relationship("AssistantIA", back_populates="entreprise", cascade="all, delete-orphan")

    # === RELATIONS internes au module entreprise
    sites = relationship("Site", back_populates="entreprise", cascade="all, delete-orphan")
    preferences = relationship("PreferenceEntreprise", back_populates="entreprise", cascade="all, delete-orphan")
    parametres = relationship("ParametrageInterne", back_populates="entreprise", cascade="all, delete-orphan")
    profils = relationship("ProfilAcces", back_populates="entreprise", cascade="all, delete-orphan")
    

    def __repr__(self):
        return f"<Entreprise(id={self.id}, nom='{self.nom}')>"