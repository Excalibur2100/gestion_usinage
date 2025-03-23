from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, DateTime, Float, Boolean, Text
)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

# ========================= TABLE UTILISATEURS =========================
class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    mot_de_passe = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    actif = Column(Boolean, default=True)

    epis = relationship("EPIUtilisateur", back_populates="utilisateur")
    rh = relationship("RH", back_populates="utilisateur", uselist=False)
    affectations = relationship("AffectationMachine", back_populates="utilisateur")
    finances = relationship("Finance", back_populates="utilisateur")
    notations = relationship("NotationRH", back_populates="utilisateur")
    absences = relationship("Absence", back_populates="utilisateur")
    formations = relationship("Formation", back_populates="utilisateur")
    sanctions = relationship("Sanction", back_populates="utilisateur")
    entretiens = relationship("Entretien", back_populates="utilisateur")


# ========================= TABLE CLIENTS =========================
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    telephone = Column(String(20))
    adresse = Column(String(255))
    commandes = relationship("Commande", back_populates="client")
    devis = relationship("Devis", back_populates="client")

# ========================= TABLE FOURNISSEURS =========================
class Fournisseur(Base):
    __tablename__ = "fournisseurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    contact = Column(String(100))
    email = Column(String(150))
    telephone = Column(String(50))
    adresse = Column(String(255))
    materiaux = relationship("Materiau", back_populates="fournisseur")

# ========================= TABLE PIECES =========================
class Piece(Base):
    __tablename__ = "pieces"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    numero_plan = Column(String(100), unique=True)
    description = Column(Text)
    date_creation = Column(DateTime, default=datetime.utcnow)
    historique_commandes = relationship("CommandePiece", back_populates="piece")
    gammes = relationship("GammeProduction", back_populates="piece")
    machine_id = Column(Integer, ForeignKey("machines.id"))
    machine = relationship("Machine", back_populates="pieces")
    controles = relationship("ControlePiece", back_populates="piece")

# ========================= TABLE COMMANDES =========================
class Commande(Base):
    __tablename__ = "commandes"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    statut = Column(String(50), default="En attente")
    date_commande = Column(DateTime, default=datetime.utcnow)
    bon_commande_client = Column(String(255))
    forcer_creation = Column(Boolean, default=False)
    machine_id = Column(Integer, ForeignKey("machines.id"))

    client = relationship("Client", back_populates="commandes")
    pieces = relationship("CommandePiece", back_populates="commande")
    machine = relationship("Machine", back_populates="commandes")

# ========================= LIEN COMMANDE / PIECE =========================
class CommandePiece(Base):
    __tablename__ = "commande_pieces"
    id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey("commandes.id"))
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    quantite = Column(Integer, nullable=False)

    commande = relationship("Commande", back_populates="pieces")
    piece = relationship("Piece", back_populates="historique_commandes")

# ========================= TABLE DEVIS =========================
class Devis(Base):
    __tablename__ = "devis"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    date_devis = Column(DateTime, default=datetime.utcnow)
    montant_total = Column(Float)
    statut = Column(String(50), default="En attente")
    scenarios = Column(Text)
    machine_id = Column(Integer, ForeignKey("machines.id"))

    client = relationship("Client", back_populates="devis")
    machine = relationship("Machine")

# ========================= TABLE MATERIAUX =========================
class Materiau(Base):
    __tablename__ = "materiaux"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    afnor = Column(String(100))
    stock = Column(Integer)
    durete = Column(String(100))
    type = Column(String(50), default="Acier")
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))

    fournisseur = relationship("Fournisseur", back_populates="materiaux")
    gammes = relationship("GammeProduction", back_populates="materiau")
    qhse = relationship("QHSE", back_populates="materiau")
    finance = relationship("Finance", back_populates="materiau")

# ========================= TABLE OUTILS =========================
class Outil(Base):
    __tablename__ = "outils"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type = Column(String(100))
    stock = Column(Integer)
    en_stock = Column(Boolean, default=True)

    gammes = relationship("GammeProduction", back_populates="outil")
    machines = relationship("MachineOutil", back_populates="outil")

class MachineOutil(Base):
    __tablename__ = "machine_outil"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    outil_id = Column(Integer, ForeignKey("outils.id"))

    machine = relationship("Machine", back_populates="outils_associes")
    outil = relationship("Outil", back_populates="machines")

# ========================= TABLE MACHINES =========================
class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type = Column(String(100))
    vitesse_max = Column(Float)
    puissance = Column(Float)
    nb_axes = Column(Integer)
    axe_x_max = Column(Float)
    axe_y_max = Column(Float)
    axe_z_max = Column(Float)

    pieces = relationship("Piece", back_populates="machine")
    commandes = relationship("Commande", back_populates="machine")
    gammes = relationship("GammeProduction", back_populates="machine")
    outils_associes = relationship("MachineOutil", back_populates="machine")
    affectations = relationship("AffectationMachine", back_populates="machine")
    devis = relationship("Devis", back_populates="machine")

class AffectationMachine(Base):
    __tablename__ = "affectation_machine"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    machine_id = Column(Integer, ForeignKey("machines.id"))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)

    utilisateur = relationship("Utilisateur", back_populates="affectations")
    machine = relationship("Machine", back_populates="affectations")

# ========================= TABLE GAMMES DE PRODUCTION =========================
class GammeProduction(Base):
    __tablename__ = "gammes_production"
    id = Column(Integer, primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    ordre = Column(Integer)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    outil_id = Column(Integer, ForeignKey("outils.id"))
    materiau_id = Column(Integer, ForeignKey("materiaux.id"))
    operation = Column(String(100))
    temps_prevu = Column(Float)
    temps_reel = Column(Float)
    statut = Column(String(50), default="En attente")

    piece = relationship("Piece", back_populates="gammes")
    machine = relationship("Machine", back_populates="gammes")
    outil = relationship("Outil", back_populates="gammes")
    materiau = relationship("Materiau", back_populates="gammes")

# ========================= TABLE TRACABILITE =========================
class Tracabilite(Base):
    __tablename__ = "tracabilite"
    id = Column(Integer, primary_key=True)
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"))
    date = Column(DateTime, default=datetime.utcnow)
    remarque = Column(Text)

# ========================= TABLE CONTROLE DES PIECES =========================
class ControlePiece(Base):
    __tablename__ = "controle_piece"
    id = Column(Integer, primary_key=True)
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id"))
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    resultat = Column(String(100))
    date_controle = Column(DateTime, default=datetime.utcnow)

    piece = relationship("Piece", back_populates="controles")

# ========================= TABLE INSTRUMENTS DE CONTROLE =========================
class InstrumentControle(Base):
    __tablename__ = "instruments_controle"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    type_instrument = Column(String(100))
    date_calibrage = Column(DateTime, default=datetime.utcnow)
    conforme_qhse = Column(Boolean)

# ========================= TABLE EPI =========================
class EPI(Base):
    __tablename__ = "epi"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    stock = Column(Integer)
    seuil_alerte = Column(Integer)

class EPIUtilisateur(Base):
    __tablename__ = "epi_utilisateur"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    epi_id = Column(Integer, ForeignKey("epi.id"))
    utilisateur = relationship("Utilisateur", back_populates="epis")

# ========================= TABLE RH =========================
class RH(Base):
    __tablename__ = "rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    poste = Column(String(100))
    contrat = Column(String(100))
    temps_travail = Column(Float)
    est_cadre = Column(Boolean, default=False)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime, nullable=True)
    statut_administratif = Column(String(100))
    salaire_brut = Column(Float)
    remarques = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="rh")


# ========================= TABLE FINANCE =========================
class Finance(Base):
    __tablename__ = "finance"
    id = Column(Integer, primary_key=True)
    type_transaction = Column(String(100))
    montant = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    categorie = Column(String(100))
    materiau_id = Column(Integer, ForeignKey("materiaux.id"))
    epi_id = Column(Integer, ForeignKey("epi.id"))
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id"))
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))

    materiau = relationship("Materiau", back_populates="finance")
    utilisateur = relationship("Utilisateur", back_populates="finances")

# ========================= TABLE QHSE =========================
class QHSE(Base):
    __tablename__ = "qhse"
    id = Column(Integer, primary_key=True)
    type_document = Column(String(100))
    conformite = Column(Boolean)
    remarque = Column(Text)
    instrument_controle_id = Column(Integer, ForeignKey("instruments_controle.id"))
    epi_id = Column(Integer, ForeignKey("epi.id"))
    materiau_id = Column(Integer, ForeignKey("materiaux.id"))

    materiau = relationship("Materiau", back_populates="qhse")

# ========================= TABLE ENTRETIENS RH =========================
class Entretien(Base):
    __tablename__ = "entretiens"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_entretien = Column(String(100))  # annuel, professionnel...
    date = Column(DateTime, default=datetime.utcnow)
    resume = Column(Text)
    actions_prevues = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="entretiens")


# ========================= TABLE SANCTIONS RH =========================
class Sanction(Base):
    __tablename__ = "sanctions"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_sanction = Column(String(150))
    date = Column(DateTime, default=datetime.utcnow)
    motif = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="sanctions")


# ========================= TABLE NOTATIONS RH =========================
class NotationRH(Base):
    __tablename__ = "notations_rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_evaluation = Column(DateTime, default=datetime.utcnow)
    note = Column(Float)
    commentaire = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="notations")


# ========================= TABLE ABSENCES RH =========================
class Absence(Base):
    __tablename__ = "absences"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    type_absence = Column(String(100))  # ex: maladie, congé, etc.
    commentaire = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="absences")


# ========================= TABLE FORMATIONS RH =========================
class Formation(Base):
    __tablename__ = "formations"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom = Column(String(150), nullable=False)
    organisme = Column(String(150))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    certification = Column(String(150))
    commentaire = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="formations")



# ========================= TABLE ROBOTIQUE =========================
class Robotique(Base):
    __tablename__ = "robotique"
    id = Column(Integer, primary_key=True)
    nom_robot = Column(String(100))
    fonction = Column(String(100))
    statut = Column(String(50))
    affectation = Column(String(255))


# ========================= CONNEXION DB =========================
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://excalibur:Christopher@localhost:5432/gestion_usinage"
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)