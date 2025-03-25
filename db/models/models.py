
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text, Table, create_engine
)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime
import os
import bcrypt




Base = declarative_base()

# ========================= ASSOCIATION MACHINE ↔ OUTIL =========================
machine_outil = Table(
    'machine_outil', Base.metadata,
    Column('machine_id', ForeignKey('machines.id'), primary_key=True),
    Column('outil_id', ForeignKey('outils.id'), primary_key=True)
)

# ========================= UTILISATEUR ET DROITS =========================

# ========================= UTILISATEUR =========================

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    mot_de_passe = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    actif = Column(Boolean, default=True, nullable=False)

    # Relations
    droits = relationship("Droit", back_populates="utilisateur")
    rh = relationship("RH", back_populates="utilisateur", uselist=False)
    absences = relationship("Absence", back_populates="utilisateur")
    formations = relationship("Formation", back_populates="utilisateur")
    sanctions = relationship("Sanction", back_populates="utilisateur")
    entretiens = relationship("Entretien", back_populates="utilisateur")
    notations = relationship("NotationRH", back_populates="utilisateur")
    epis = relationship("EPIUtilisateur", back_populates="utilisateur")
    affectations = relationship("AffectationMachine", back_populates="utilisateur")
    finances = relationship("Finance", back_populates="utilisateur")
    documents = relationship("DocumentRH", back_populates="utilisateur")
    audits_realises = relationship("AuditQualite", foreign_keys="[AuditQualite.responsable]", backref="responsable_utilisateur")
    non_conformites = relationship("NonConformite", back_populates="utilisateur")
    filtres = relationship("GestionFiltrage", back_populates="utilisateur")

    # Méthodes de sécurité
    def set_password(self, plain_password: str):
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        self.mot_de_passe = hashed.decode('utf-8')

    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.mot_de_passe.encode('utf-8'))

# ========================= DROIT =========================
class Droit(Base):
    __tablename__ = "droits"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    module = Column(String(100))
    autorisation = Column(Boolean, default=False)

    utilisateur = relationship("Utilisateur", back_populates="droits")

# ========================= DROIT DACCES =========================
class DroitAcces(Base):
    __tablename__ = "droits_acces"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    module = Column(String(100))  # Ex: 'devis', 'production', 'finance', etc.
    peut_lire = Column(Boolean, default=False)
    peut_creer = Column(Boolean, default=False)
    peut_modifier = Column(Boolean, default=False)
    peut_supprimer = Column(Boolean, default=False)
    acces_total = Column(Boolean, default=False)

    utilisateur = relationship("Utilisateur", backref="droits_acces")

# ========================= GESTION ACCES UTILISATEURS =========================
class GestionAcces(Base):
    __tablename__ = "gestion_acces"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    module = Column(String(100))  # ex : production, RH, devis, QHSE...
    peut_lire = Column(Boolean, default=False)
    peut_ecrire = Column(Boolean, default=False)
    peut_supprimer = Column(Boolean, default=False)
    peut_valider = Column(Boolean, default=False)

    utilisateur = relationship("Utilisateur")

# ========================= HISTORIQUE DACTION =========================
class HistoriqueAction(Base):
    __tablename__ = 'historique_actions'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    date_action = Column(DateTime, default=datetime.utcnow)
    module = Column(String(100), nullable=False)  # Ex: 'devis', 'commande'
    action = Column(String(255), nullable=False)  # Ex: 'création', 'modification', 'suppression'
    details = Column(Text)

    utilisateur = relationship("Utilisateur", backref="historique_actions")

# ========================= RESSOURCES HUMAINES =========================

# ========================= RH =========================
class RH(Base):
    __tablename__ = 'rh'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    poste = Column(String(100))
    contrat = Column(String(100))
    temps_travail = Column(Float)
    est_cadre = Column(Boolean)
    date_debut = Column(DateTime)
    salaire_brut = Column(Float)
    statut_administratif = Column(String(100))
    remarques = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="rh")

# ========================= TABLES ABSENCE =========================
class Absence(Base):
    __tablename__ = 'absences'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    type_absence = Column(String(100))
    commentaire = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="absences")

# ========================= FORMATION =========================
class Formation(Base):
    __tablename__ = 'formations'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom = Column(String(150))
    organisme = Column(String(150))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    certification = Column(String(150))
    commentaire = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="formations")


# ========================= SANCTION =========================
class Sanction(Base):
    __tablename__ = 'sanctions'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_sanction = Column(String(150))
    date = Column(DateTime)
    motif = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="sanctions")

# ========================= ENTRETIEN =========================
class Entretien(Base):
    __tablename__ = 'entretiens'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_entretien = Column(String(100))
    date = Column(DateTime)
    resume = Column(Text)
    actions_prevues = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="entretiens")

# ========================= NOTATION RH =========================
class NotationRH(Base):
    __tablename__ = 'notations_rh'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_evaluation = Column(DateTime)
    note = Column(Float)
    commentaire = Column(Text)

    utilisateur = relationship("Utilisateur", back_populates="notations")

# ========================= DOCUMENTS RH =========================
class DocumentRH(Base):
    __tablename__ = 'documents_rh'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_document = Column(String(100))
    chemin_fichier = Column(String(255))
    date_ajout = Column(DateTime, default=datetime.utcnow)

    utilisateur = relationship("Utilisateur", back_populates="documents")

# ========================= CLIENTS ET FOURNISSEUR =========================

# ========================= CLIENTS =========================
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    telephone = Column(String(50))
    adresse = Column(String(255))
    siret = Column(String(20))
    tva_intracom = Column(String(20))
    secteur_activite = Column(String(100))
    site_web = Column(String(150))
    commentaire = Column(Text)

    devis = relationship("Devis", back_populates="client", cascade="all, delete-orphan")
    commandes = relationship("Commande", back_populates="client", cascade="all, delete-orphan")
    factures = relationship("Facture", back_populates="client", cascade="all, delete-orphan")
    filtres = relationship("GestionFiltrage", back_populates="client")

# ========================= FOURNISSEURS =========================
class Fournisseur(Base):
    __tablename__ = "fournisseurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    contact = Column(String(100))
    email = Column(String(150))
    telephone = Column(String(50))
    adresse = Column(String(255))
    tva = Column(String(50))
    site_web = Column(String(255))
    catalogue_interactif = Column(String(255))  # URL ou nom de fichier PDF

    materiaux = relationship("Materiau", back_populates="fournisseur")
    outils = relationship("Outil", back_populates="fournisseur")
    evaluations = relationship("EvaluationFournisseur", back_populates="fournisseur")
    finances = relationship("Finance", back_populates="fournisseur")
    filtres = relationship("GestionFiltrage", back_populates="fournisseur")

# =========================EVALUATION FOURNISSEURS =========================
class EvaluationFournisseur(Base):
    __tablename__ = "evaluations_fournisseur"
    id = Column(Integer, primary_key=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))
    date_evaluation = Column(DateTime, default=datetime.utcnow)
    critere = Column(String(150))  # délai, qualité, conformité, etc.
    note = Column(Float)
    commentaire = Column(Text)

    fournisseur = relationship("Fournisseur", back_populates="evaluations")

# ========================= DEVIS / COMMANDE / FACTURES =========================

# ========================= DEVIS =========================
class Devis(Base):
    __tablename__ = 'devis'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    date_devis = Column(DateTime, default=datetime.utcnow)
    montant_total = Column(Float)
    statut = Column(String(50))
    scenarios = Column(Text)
    client = relationship("Client", back_populates="devis")

# ========================= COMMANDES =========================
class Commande(Base):
    __tablename__ = 'commandes'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    statut = Column(String(50), default="en attente")
    date_commande = Column(DateTime, default=datetime.utcnow)
    bon_commande_client = Column(String(255))
    forcer_creation = Column(Boolean, default=False)
    code_statut = Column(String(20))  # en_attente, validee, annulee, etc.
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    client = relationship("Client", back_populates="commandes")
    lignes = relationship("CommandePiece", back_populates="commande")
    facture = relationship("Facture", back_populates="commande", uselist=False)
    filtres = relationship("GestionFiltrage", back_populates="commande")

# ========================= COMMANDE PIECE =========================
class CommandePiece(Base):
    __tablename__ = 'commande_pieces'
    id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey("commandes.id", ondelete="CASCADE"), nullable=False)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="CASCADE"), nullable=False)
    quantite = Column(Integer, nullable=False)

    commande = relationship("Commande", back_populates="lignes")
    piece = relationship("Piece", back_populates="commandes")

# ========================= FACTURES =========================
from sqlalchemy import CheckConstraint

class Facture(Base):
    __tablename__ = "factures"
    id = Column(Integer, primary_key=True)
    numero_facture = Column(String(100), unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))
    commande_id = Column(Integer, ForeignKey("commandes.id"))
    date_emission = Column(DateTime, default=datetime.utcnow)
    date_echeance = Column(DateTime)
    montant_total = Column(Float)
    statut = Column(String(50), default="En attente", nullable=False)
    mode_generation = Column(String(50), default="Automatique")
    valide_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    observations = Column(Text)
    code_statut = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    client = relationship("Client", back_populates="factures")
    commande = relationship("Commande", back_populates="facture")
    valideur = relationship("Utilisateur")
    lignes = relationship("LigneFacture", back_populates="facture")
    finances = relationship("Finance", back_populates="facture")

    __table_args__ = (
        CheckConstraint("statut IN ('En attente', 'Validée', 'Payée', 'Annulée')", name="check_statut_facture"),
    )

# ========================= LIGNE FACTURE =========================
class LigneFacture(Base):
    __tablename__ = "lignes_facture"
    id = Column(Integer, primary_key=True)
    facture_id = Column(Integer, ForeignKey("factures.id", ondelete="CASCADE"), nullable=False)
    description = Column(String(255))
    quantite = Column(Integer, nullable=False)
    prix_unitaire = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    facture = relationship("Facture", back_populates="lignes")

# ========================= PRODUCTION / MACHINES =========================

# ========================= PIECES =========================
class Piece(Base):
    __tablename__ = 'pieces'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    numero_plan = Column(String(100), nullable=False)
    description = Column(Text)

    commandes = relationship("CommandePiece", back_populates="piece", cascade="all, delete-orphan")
    gammes = relationship("GammeProduction", back_populates="piece", cascade="all, delete-orphan")
    programmes = relationship("ProgrammePiece", back_populates="piece", cascade="all, delete-orphan")
    controles = relationship("ControlePiece", back_populates="piece", cascade="all, delete-orphan")

# ========================= PROGRAMME PIECE =========================
class ProgrammePiece(Base):
    __tablename__ = "programmes_piece"
    id = Column(Integer, primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    nom_programme = Column(String(150))
    fichier_path = Column(String(255))  # Chemin du fichier sur disque
    postprocesseur_id = Column(Integer, ForeignKey("postprocesseurs.id"))
    date_import = Column(DateTime, default=datetime.utcnow)

    piece = relationship("Piece", back_populates="programmes")
    postprocesseur = relationship("PostProcesseur", back_populates="programmes")

# ========================= POST PROCESSEUR =========================
class PostProcesseur(Base):
    __tablename__ = "postprocesseurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False)  # Nom lisible (ex: "FANUC - Tour CN XYZ")
    logiciel_fao = Column(String(100), nullable=False)  # SolidCAM, TopSolid, etc.
    extension_sortie = Column(String(20), default=".nc")  # ex: .nc, .txt
    configuration = Column(Text)  # JSON / texte de configuration brute
    machine_id = Column(Integer, ForeignKey("machines.id"))
    date_creation = Column(DateTime, default=datetime.utcnow)

    machine = relationship("Machine", back_populates="postprocesseurs")
    programmes = relationship("ProgrammePiece", back_populates="postprocesseur")

# ========================= MACHINES =========================
class Machine(Base):
    __tablename__ = 'machines'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    type = Column(String(100))
    vitesse_max = Column(Float)
    puissance = Column(Float)
    nb_axes = Column(Integer)
    axe_x_max = Column(Float)
    axe_y_max = Column(Float)
    axe_z_max = Column(Float)
    commande_numerique = Column(String(100))  # Siemens, Fanuc, etc.
    logiciel_fao = Column(String(100))  # SolidCam, TopSolid, Fusion360, etc.

    affectations = relationship("AffectationMachine", back_populates="machine")
    gammes = relationship("GammeProduction", back_populates="machine")
    non_conformites = relationship("NonConformite", back_populates="machine")
    maintenances = relationship("Maintenance", back_populates="machine")
    plannings = relationship("PlanningMachine", back_populates="machine")
    charges = relationship("ChargeMachine", back_populates="machine")
    postprocesseurs = relationship("PostProcesseur", back_populates="machine")

# ========================= MAINTENANCE =========================
class Maintenance(Base):
    __tablename__ = "maintenance"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    type_maintenance = Column(String(100), nullable=False, default="Préventive")
    date_planifiee = Column(DateTime)
    date_reelle = Column(DateTime, nullable=True)
    statut = Column(String(50), default="Planifiée", nullable=False)
    operateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    description = Column(Text)
    remarques = Column(Text)

    machine = relationship("Machine", back_populates="maintenances")
    operateur = relationship("Utilisateur")

    __table_args__ = (
        CheckConstraint("type_maintenance IN ('Préventive', 'Corrective', 'Prédictive')", name="check_type_maintenance"),
        CheckConstraint("statut IN ('Planifiée', 'En cours', 'Réalisée')", name="check_statut_maintenance"),
    )

# ========================= OUTILS =========================
class Outil(Base):
    __tablename__ = 'outils'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    type = Column(String(100))
    stock = Column(Integer)
    en_stock = Column(Boolean)
    diametre = Column(Float)
    longueur = Column(Float)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))
    ref_fournisseur = Column(String(100))
    catalogue_url = Column(String(255))

    gammes = relationship("GammeProduction", back_populates="outil")
    fournisseur = relationship("Fournisseur", back_populates="outils")
    non_conformites = relationship("NonConformite", back_populates="outil")

# ========================= MATERIAUX =========================
class Materiau(Base):
    __tablename__ = "materiaux"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    afnor = Column(String(100))
    stock = Column(Integer)
    durete = Column(String(100))
    type = Column(String(50), default="Acier")
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))
    est_aeronautique = Column(Boolean, default=False)
    certificat_matiere = Column(String(255))  # chemin fichier ou numéro

    fournisseur = relationship("Fournisseur", back_populates="materiaux")
    gammes = relationship("GammeProduction", back_populates="materiau")
    qhse = relationship("QHSE", back_populates="materiau")
    finance = relationship("Finance", back_populates="materiau")
    non_conformites = relationship("NonConformite", back_populates="materiau")

# ========================= GAMME PRODUCTION =========================
class GammeProduction(Base):
    __tablename__ = "gammes_production"
    id = Column(Integer, primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    ordre = Column(Integer)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    outil_id = Column(Integer, ForeignKey("outils.id"))
    materiau_id = Column(Integer, ForeignKey("materiaux.id"))
    programme_id = Column(Integer, ForeignKey("programmes_piece.id"), nullable=True)
    operation = Column(String(100))
    temps_prevu = Column(Float)
    temps_reel = Column(Float)
    statut = Column(String(50), default="En attente")
    moyen_controle = Column(String(100))
    longueur_debit = Column(Float)  # en mm ou cm
    nombre_debits = Column(Integer)

    piece = relationship("Piece", back_populates="gammes")
    machine = relationship("Machine", back_populates="gammes")
    outil = relationship("Outil", back_populates="gammes")
    materiau = relationship("Materiau", back_populates="gammes")
    pointages = relationship("Pointage", back_populates="gamme")
    programme = relationship("ProgrammePiece")

# ========================= TRACABILITE =========================
class Tracabilite(Base):
    __tablename__ = 'tracabilite'
    id = Column(Integer, primary_key=True)
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"))
    date = Column(DateTime, default=datetime.utcnow)
    remarque = Column(Text)

# ========================= PLANNING ET POINTAGE =========================

# ========================= PLANNING EMPLOYER =========================
class PlanningEmploye(Base):
    __tablename__ = "planning_employe"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=True)
    date = Column(DateTime, nullable=False)
    plage_horaire = Column(String(50))
    tache = Column(Text)
    statut = Column(String(50), default="Prévu")
    affectation_auto = Column(Boolean, default=True)

    utilisateur = relationship("Utilisateur")
    machine = relationship("Machine")

# ========================= PLANNING MACHINE =========================
class PlanningMachine(Base):
    __tablename__ = "planning_machine"
    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    plage_horaire = Column(String(50), nullable=False)
    tache = Column(Text)
    statut = Column(String(50), default="Prévu", nullable=False)
    charge_estimee = Column(Float)
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"))

    machine = relationship("Machine", back_populates="plannings")
    gamme = relationship("GammeProduction")

# ========================= AFFECTATION MACHINE =========================

class AffectationMachine(Base):
    __tablename__ = 'affectation_machine'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    machine_id = Column(Integer, ForeignKey("machines.id"))
    date_affectation = Column(DateTime)
    tache = Column(String(255))
    statut = Column(String(50))
    utilisateur = relationship("Utilisateur", back_populates="affectations")
    machine = relationship("Machine", back_populates="affectations")

# ========================= POINTAGE =========================
class Pointage(Base):
    __tablename__ = "pointages"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"), nullable=False)
    date_pointage = Column(DateTime, default=datetime.utcnow, nullable=False)
    heure_debut = Column(DateTime, nullable=False)
    heure_fin = Column(DateTime)
    duree_effective = Column(Float)
    remarques = Column(Text)

    utilisateur = relationship("Utilisateur")
    machine = relationship("Machine")
    gamme = relationship("GammeProduction", back_populates="pointages")

    __table_args__ = (
        CheckConstraint('heure_fin IS NULL OR heure_fin >= heure_debut', name='check_pointage_heure'),
    )

# ========================= QHSE/CONTROLE QUALITE =========================

# =========================INSTRUMENT CONTROLES =========================
class InstrumentControle(Base):
    __tablename__ = "instruments_controle"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type_instrument = Column(String(100), nullable=False)
    numero_serie = Column(String(100), unique=True, nullable=False)
    date_calibrage = Column(DateTime)
    date_prochaine_calibration = Column(DateTime)
    conforme_qhse = Column(Boolean, default=True)
    en_service = Column(Boolean, default=True)

    controles = relationship("ControlePiece", back_populates="instrument")
    qhse = relationship("QHSE", back_populates="instrument")
    finances = relationship("Finance", back_populates="instrument")
    non_conformites = relationship("NonConformite", back_populates="instrument")

# ========================= CONTROLE PIECE =========================
class ControlePiece(Base):
    __tablename__ = "controle_piece"
    id = Column(Integer, primary_key=True)
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id"), nullable=False)
    piece_id = Column(Integer, ForeignKey("pieces.id"), nullable=False)
    resultat = Column(String(100), nullable=False)
    date_controle = Column(DateTime, default=datetime.utcnow, nullable=False)
    remarque = Column(Text)

    instrument = relationship("InstrumentControle", back_populates="controles")
    piece = relationship("Piece", back_populates="controles")


# ========================= EPI =========================
class EPI(Base):
    __tablename__ = 'epi'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    stock = Column(Integer, default=0)
    seuil_alerte = Column(Integer, default=0)

# ========================= EPI UTILISATEUR =========================

class EPIUtilisateur(Base):
    __tablename__ = 'epi_utilisateur'
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    epi_id = Column(Integer, ForeignKey("epi.id"), nullable=False)
    date_distribution = Column(DateTime, nullable=False)
    quantite = Column(Integer, nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="epis")
    epi = relationship("EPI")

# ========================= QHSE =========================
class QHSE(Base):
    __tablename__ = 'qhse'
    id = Column(Integer, primary_key=True)
    type_document = Column(String(100), nullable=False)
    conformite = Column(Boolean, default=True)
    remarque = Column(Text)

    instrument_controle_id = Column(Integer, ForeignKey("instruments_controle.id"), nullable=True)
    epi_id = Column(Integer, ForeignKey("epi.id"), nullable=True)
    materiau_id = Column(Integer, ForeignKey("materiaux.id"), nullable=True)

    instrument = relationship("InstrumentControle", back_populates="qhse")
    # Relations avec EPI et Materiau peuvent être ajoutées selon besoin

# ========================= DOCUMENT QHSE =========================
class DocumentQHSE(Base):
    __tablename__ = "documents_qhse"
    id = Column(Integer, primary_key=True)
    titre = Column(String(150), nullable=False)
    type_document = Column(String(100), nullable=False)
    date_emission = Column(DateTime, nullable=False)
    date_expiration = Column(DateTime)
    fichier = Column(String(255), nullable=False)
    visible = Column(Boolean, default=True)
    categorie = Column(String(100))  # Nouveau champ optionnel

# ========================= AUDIT QUALITE =========================
class AuditQualite(Base):
    __tablename__ = "audits_qualite"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    type_audit = Column(String(100), nullable=False)
    responsable_nom = Column(String(100), nullable=False)
    remarques = Column(Text)
    statut = Column(String(50), nullable=False)

    document_id = Column(Integer, ForeignKey("documents_qualite.id"), nullable=False)
    document = relationship("DocumentQualite", back_populates="audits")

# ========================= DOCUMENT QUALITE =========================
class DocumentQualite(Base):
    __tablename__ = "documents_qualite"
    id = Column(Integer, primary_key=True)
    titre = Column(String(150), nullable=False)
    categorie = Column(String(100))  # Nouveau champ optionnel
    type_document = Column(String(100), nullable=False)
    reference_norme = Column(String(100))
    fichier_path = Column(String(255), nullable=False)
    version = Column(String(20))
    date_ajout = Column(DateTime, default=datetime.utcnow)
    actif = Column(Boolean, default=True)

    audits = relationship("AuditQualite", back_populates="document")

# ========================= DOCUMENT REGLEMENTAIRE =========================
class DocumentReglementaire(Base):
    __tablename__ = 'documents_reglementaires'
    id = Column(Integer, primary_key=True)
    titre = Column(String(150), nullable=False)
    description = Column(Text)
    type_document = Column(String(100), nullable=False)  # Procédure, Fiche sécurité, etc.
    date_edition = Column(DateTime, default=datetime.utcnow, nullable=False)
    valide_jusquau = Column(DateTime)
    fichier_stocke = Column(String(255), nullable=False)
    conforme = Column(Boolean, default=True)
    norme_associee = Column(String(100))
    categorie = Column(String(100))  # Nouveau champ optionnel

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    utilisateur = relationship("Utilisateur", backref="documents_responsables")

# ========================= NON CONFORMITE =========================
class NonConformite(Base):
    __tablename__ = "non_conformites"
    id = Column(Integer, primary_key=True)
    origine = Column(String(100), nullable=False)  # matière, machine, opérateur, etc.
    description = Column(Text, nullable=False)
    action_corrective = Column(Text)
    date_detection = Column(DateTime, default=datetime.utcnow, nullable=False)
    date_resolution = Column(DateTime)
    statut = Column(String(50), default="Ouvert", nullable=False)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=True)
    materiau_id = Column(Integer, ForeignKey("materiaux.id"), nullable=True)
    outil_id = Column(Integer, ForeignKey("outils.id"), nullable=True)
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id"), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="non_conformites")
    machine = relationship("Machine", back_populates="non_conformites")
    materiau = relationship("Materiau", back_populates="non_conformites")
    outil = relationship("Outil", back_populates="non_conformites")
    instrument = relationship("InstrumentControle", back_populates="non_conformites")

# ========================= ROBOTIQUE =========================
class Robotique(Base):
    __tablename__ = 'robotique'
    id = Column(Integer, primary_key=True)
    nom_robot = Column(String(100))
    fonction = Column(String(100))
    statut = Column(String(50))
    affectation = Column(String(255))

class SurveillanceCamera(Base):
    __tablename__ = "surveillance_cameras"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    emplacement = Column(String, nullable=False)
    actif = Column(Boolean, default=True)

class ControleRobot(Base):
    __tablename__ = "controle_robot"

    id = Column(Integer, primary_key=True, index=True)
    robot_id = Column(Integer, ForeignKey("robotique.id"), nullable=False)
    action = Column(String, nullable=False)
    statut = Column(String, nullable=True)
    date_execution = Column(DateTime, default=datetime.utcnow)

    robot = relationship("Robotique")




# ========================= FINANCE/STATISTIQUE =========================

# ========================= FINANCE =========================
class Finance(Base):
    __tablename__ = 'finance'
    id = Column(Integer, primary_key=True)
    
    # Détail de la transaction
    type_transaction = Column(String(100), nullable=False)  # Achat, Vente, etc.
    categorie = Column(String(100))
    sous_categorie = Column(String(100))
    description = Column(Text)

    montant = Column(Float, nullable=False)
    devise = Column(String(10), default="EUR", nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    periode = Column(String(20))  # ex: 2024-03

    statut = Column(String(50), default="Validé")
    moyen_paiement = Column(String(50))
    code_statut = Column(String(20))  # brouillon, validé, rejeté...
    justificatif = Column(String(255))
    type_justificatif = Column(String(50))
    reference_facture = Column(String(100))

    # Relations clés   
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"))
    materiau_id = Column(Integer, ForeignKey("materiaux.id"))
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id"))
    outil_id = Column(Integer, ForeignKey("outils.id"))
    machine_id = Column(Integer, ForeignKey("machines.id"))
    facture_id = Column(Integer, ForeignKey("factures.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    # ORM relationships
    utilisateur = relationship("Utilisateur", back_populates="finances")
    fournisseur = relationship("Fournisseur", back_populates="finances")
    materiau = relationship("Materiau", back_populates="finance")
    instrument = relationship("InstrumentControle", back_populates="finances")
    outil = relationship("Outil")
    piece = relationship("Piece")
    machine = relationship("Machine")
    facture = relationship("Facture")


# ========================= STAT FINANCE =========================
class StatFinance(Base):
    __tablename__ = 'stat_finance'
    id = Column(Integer, primary_key=True)

    periode = Column(String(20), nullable=False)  # ex : 2024-03
    type_stat = Column(String(50), nullable=False)  # revenu, dépense...
    categorie = Column(String(100))
    sous_categorie = Column(String(100))
    montant_total = Column(Float, nullable=False)

    source_finance_id = Column(Integer, ForeignKey("finance.id"))
    devise = Column(String(10), default="EUR")
    precision = Column(String(20), default="mois")  # jour / semaine / mois / année
    date_calcul = Column(DateTime, default=datetime.utcnow)

    source = relationship("Finance")

# ========================= STAT RH =========================
class StatRH(Base):
    __tablename__ = 'stat_rh'
    id = Column(Integer, primary_key=True)

    periode = Column(String(20), nullable=False)
    type_stat = Column(String(50), nullable=False)  # absenteisme, heures_travaillees...
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    departement = Column(String(100))

    valeur = Column(Float, nullable=False)
    unite = Column(String(20), default="heures")
    precision = Column(String(20), default="mois")
    date_calcul = Column(DateTime, default=datetime.utcnow)

    utilisateur = relationship("Utilisateur")

# ========================= STAT PRODUCTION =========================
class StatProduction(Base):
    __tablename__ = 'stat_production'
    id = Column(Integer, primary_key=True)

    periode = Column(String(20), nullable=False)
    type_stat = Column(String(50), nullable=False)  # pieces_produites, trs...
    valeur = Column(Float, nullable=False)
    unite = Column(String(20), default="unités")
    precision = Column(String(20), default="mois")
    date_calcul = Column(DateTime, default=datetime.utcnow)

    machine_id = Column(Integer, ForeignKey("machines.id"))
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"))

    machine = relationship("Machine")
    gamme = relationship("GammeProduction")

# ========================= SYSTEME =========================    

# ========================= QR CODE =========================
class QrCodeObjet(Base):
    __tablename__ = "qr_codes"
    id = Column(Integer, primary_key=True)
    objet_type = Column(String(100), nullable=False)  # "piece", "outil", etc.
    objet_id = Column(Integer, nullable=False)
    qr_code_data = Column(String(255), nullable=False, unique=True)  # UUID ou lien unique
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False)

# ========================= CHARGE MACHINE =========================
class ChargeMachine(Base):
    __tablename__ = "charges_machine"
    id = Column(Integer, primary_key=True)

    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    gamme_id = Column(Integer, ForeignKey("gammes_production.id"), nullable=True)
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    statut = Column(String(50), default="planifié", nullable=False)  # planifié, en cours, terminé

    machine = relationship("Machine")
    gamme = relationship("GammeProduction")

# ========================= FILTRAGE =========================
class GestionFiltrage(Base):
    __tablename__ = "gestion_filtrage"

    id = Column(Integer, primary_key=True, index=True)
    nom_filtre = Column(String, nullable=False)
    niveau = Column(Integer, nullable=False)
    actif = Column(Boolean, default=True)

    # Relations facultatives vers les entités filtrables
    utilisateur_id = Column(Integer, ForeignKey("utilisateur.id"), nullable=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=True)
    commande_id = Column(Integer, ForeignKey("commande.id"), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="filtres")
    client = relationship("Client", back_populates="filtres")
    commande = relationship("Commande", back_populates="filtres")
    Fournisseur = relationship("Fournisseur", back_populates="filtres")

# ========================= CONNEXION DB =========================
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://excalibur:Christopher@localhost:5432/gestion_usinage"
)

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)
