from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'entreprise cliente")
    email = Column(String(150), unique=True, nullable=True, comment="Email principal du client")
    telephone = Column(String(50), nullable=True, comment="Téléphone de contact")
    adresse = Column(String(255), nullable=True, comment="Adresse postale")
    code_postal = Column(String(10), nullable=True, comment="Code postal")
    ville = Column(String(100), nullable=True, comment="Ville")
    pays = Column(String(100), nullable=True, comment="Pays")
    contact_principal = Column(String(100), nullable=True, comment="Nom du contact principal")
    fonction_contact = Column(String(100), nullable=True, comment="Fonction du contact principal")
    date_creation = Column(String(50), nullable=True, comment="Date de création du client")
    date_modification = Column(String(50), nullable=True, comment="Date de dernière modification")
    statut = Column(String(50), default="actif", nullable=False, comment="Statut du client : actif, inactif")
    type_client = Column(String(50), nullable=True, comment="Type de client : particulier, professionnel")
    num_client = Column(String(50), nullable=True, comment="Numéro de client interne")
    num_adhesion = Column(String(50), nullable=True, comment="Numéro d'adhésion ou de contrat")
    num_siren = Column(String(20), nullable=True, comment="Numéro SIREN")
    num_rcs = Column(String(20), nullable=True, comment="Numéro RCS")
    num_ape = Column(String(20), nullable=True, comment="Numéro APE")
    num_tva = Column(String(20), nullable=True, comment="Numéro de TVA")
    num_tva_intracom = Column(String(20), nullable=True, comment="Numéro de TVA intracommunautaire")

    
    siret = Column(String(20), nullable=True, comment="Numéro SIRET")
    tva_intracom = Column(String(20), nullable=True, comment="Numéro de TVA intracommunautaire")
    secteur_activite = Column(String(100), nullable=True, comment="Secteur d'activité")
    site_web = Column(String(150), nullable=True, comment="Site internet")
    commentaire = Column(Text, nullable=True, comment="Remarques commerciales ou logistiques")
    date_creation = Column(String(50), nullable=True, comment="Date de création du client")
    date_modification = Column(String(50), nullable=True, comment="Date de dernière modification")
    statut = Column(String(50), default="actif", nullable=False, comment="Statut du client : actif, inactif")
    type_client = Column(String(50), nullable=True, comment="Type de client : particulier, professionnel")
    num_client = Column(String(50), nullable=True, comment="Numéro de client interne")
    num_adhesion = Column(String(50), nullable=True, comment="Numéro d'adhésion ou de contrat")
    num_siren = Column(String(20), nullable=True, comment="Numéro SIREN")
    num_rcs = Column(String(20), nullable=True, comment="Numéro RCS")
    num_ape = Column(String(20), nullable=True, comment="Numéro APE")
    num_tva = Column(String(20), nullable=True, comment="Numéro de TVA")
    num_tva_intracom = Column(String(20), nullable=True, comment="Numéro de TVA intracommunautaire")
    num_tva_intra = Column(String(20), nullable=True, comment="Numéro de TVA intracommunautaire")

    # Relations
    devis = relationship("Devis", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    commandes = relationship("Commande", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    factures = relationship("Facture", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    filtres = relationship("GestionFiltrage", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    pieces = relationship("Piece", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    charges = relationship("ChargeMachine", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    audits = relationship("AuditQualite", back_populates="client", cascade="all, delete-orphan", lazy="joined")


    def __repr__(self):
        return f"<Client {self.nom}>"