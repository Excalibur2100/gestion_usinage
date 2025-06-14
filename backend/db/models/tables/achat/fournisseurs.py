from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Enum, Text, ForeignKey, func
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class TypeFournisseur(str, enum.Enum):
    fabricant_machines = "fabricant_machines"
    fournisseur_matiere_premiere = "fournisseur_matiere_premiere"
    fournisseur_acier = "fournisseur_acier"
    fournisseur_inox = "fournisseur_inox"
    fournisseur_non_ferreux = "fournisseur_non_ferreux"
    fournisseur_outillage = "fournisseur_outillage"
    fournisseur_outils_de_mesure = "fournisseur_outils_de_mesure"
    fournisseur_equipements_de_protection = "fournisseur_equipements_de_protection"
    fournisseur_composants_standard = "fournisseur_composants_standard"
    fournisseur_generaliste = "fournisseur_generaliste"

    outilleur = "outilleur"
    machine_outil = "machine_outil"
    transport = "transport"
    controle_qualite = "controle_qualite"
    metrologie = "metrologie"
    logiciel_support = "logiciel_support"
    logiciel_caao = "logiciel_caao"
    services_bureau_etude = "services_bureau_etude"

    sous_traitant_usinage = "sous_traitant_usinage"
    sous_traitant_fraisage = "sous_traitant_fraisage"
    sous_traitant_tournage = "sous_traitant_tournage"
    sous_traitant_edm = "sous_traitant_edm"
    sous_traitant_soudure = "sous_traitant_soudure"

    traitement_thermique = "traitement_thermique"
    traitement_surface = "traitement_surface"
    peinture_industrielle = "peinture_industrielle"
    gravure_marque = "gravure_marque"

    maintenance_machine = "maintenance_machine"
    prestataire_logistique = "prestataire_logistique"
    prestataire = "prestataire"
    grossiste = "grossiste"
    distributeur = "distributeur"
    integrateur = "integrateur"

    autre = "autre"


class StatutFournisseur(str, enum.Enum):
    actif = "actif"
    inactif = "inactif"
    blacklisté = "blacklisté"


class Fournisseur(Base):
    __tablename__ = "fournisseurs"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, index=True, nullable=True)

    nom = Column(String(100), nullable=False)
    code = Column(String(50), unique=True, nullable=True)

    type = Column(Enum(TypeFournisseur), default=TypeFournisseur.autre)
    statut = Column(Enum(StatutFournisseur), default=StatutFournisseur.actif)

    adresse = Column(String(255), nullable=True)
    ville = Column(String(100), nullable=True)
    code_postal = Column(String(20), nullable=True)
    pays = Column(String(100), default="France")

    email = Column(String(100), nullable=True)
    telephone = Column(String(50), nullable=True)
    site_web = Column(String(255), nullable=True)

    contact_nom = Column(String(100), nullable=True)
    contact_email = Column(String(100), nullable=True)
    contact_telephone = Column(String(50), nullable=True)

    commentaire = Column(Text, nullable=True)
    actif = Column(Boolean, default=True)

    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    commandes_fournisseur = relationship("CommandeFournisseur", back_populates="fournisseur", lazy="select", cascade="all, delete-orphan")
    factures_fournisseur = relationship("FactureFournisseur", back_populates="fournisseur", lazy="select", cascade="all, delete-orphan")
    avoirs_fournisseur = relationship("AvoirFournisseur", back_populates="fournisseur", lazy="select", cascade="all, delete-orphan")
    evaluations_fournisseur = relationship("EvaluationFournisseur", back_populates="fournisseur", lazy="select", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Fournisseur(id={self.id}, nom='{self.nom}', type={self.type}, statut={self.statut})>"