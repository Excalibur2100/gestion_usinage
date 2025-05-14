# ========================= UTILISATEUR =========================
from .utilisateur import Utilisateur
from .droit import Droit
from .droit_acces import DroitAcces
from .gestion_acces import GestionAcces

# ========================= FINANCES =========================
from .finance import Finance
from .qualite.gestion_filtrage import GestionFiltrage

# ========================= RESSOURCES HUMAINES =========================
from .rh import RH
from .absence import Absence
from .formation import Formation
from .sanction import Sanction
from .entretien import Entretien
from .rh.notation import NotationRH
from .ged.document_rh import DocumentRH
from .employe import Employe

# ========================= CLIENTS ET FOURNISSEURS =========================
from .crm.clients import Client
from .achat.fournisseurs import Fournisseur
from .evaluations_fournisseur import EvaluationFournisseur

# ========================= DEVIS ET COMMANDES =========================
from .devis import Devis
from .achat.commandes import Commande
from .commande_pieces import CommandePiece
from .factures import Facture
from .finance.ligne_factures import LigneFacture

# ========================= PRODUCTION =========================
from .piece import Piece
from .programme_piece import ProgrammePiece
from .postprocesseur import PostProcesseur
from .machine import Machine
from .metrics_machines import MetricsMachine
from .gmao.maintenance import Maintenance
from .gammes_production import GammeProduction
from .traceabilite.tracabilite import Tracabilite
from .production import Production

# ========================= STOCK =========================
from .outils import Outil
from .stock.materiau import Materiau
from .stock.emplacement_stock import EmplacementStock

# ========================= PLANNING =========================
from .planning.planning_employe import PlanningEmploye
from .planning.planning_machine import PlanningMachine
from .planning.affectation_machine import AffectationMachine
from .planning.pointages import Pointage

# ========================= QHSE =========================
from .instrument_controle import InstrumentControle
from .controle_piece import ControlePiece
from .epi import EPI
from .epi_utilisateur import EPIUtilisateur
from .audit_qualite import AuditQualite
from .non_conformites import NonConformite
from .documents_qualite import DocumentQualite
from .ged.documents_reglementaires import DocumentsReglementaires

# ========================= ANALYSE ET LOGS =========================
from .analyse_fichiers import AnalyseFichier
from .ia_logs import IALogs

# ========================= SYSTEME =========================
from .robotique import Robotique
from .controle_robot import ControleRobot
from .surveillance_cameras import SurveillanceCamera
from .traceabilite.QrCodeObjet import QrCodeObjet

# ========================= ASSOCIATIONS =========================
from .liaison import machine_outil

# ========================= EXPORTS =========================
__all__ = [
    # Utilisateur
    "Utilisateur",
    "Droit",
    "DroitAcces",
    "GestionAcces",

    # Finances
    "Finance",
    "GestionFiltrage",

    # Ressources Humaines
    "RH",
    "Absence",
    "Formation",
    "Sanction",
    "Entretien",
    "NotationRH",
    "DocumentRH",

    # Clients et Fournisseurs
    "Client",
    "Fournisseur",
    "EvaluationFournisseur",

    # Devis et Commandes
    "Devis",
    "Commande",
    "CommandePiece",
    "Facture",
    "LigneFacture",

    # Production
    "Piece",
    "ProgrammePiece",
    "PostProcesseur",
    "Machine",
    "MetricsMachine",
    "Maintenance",
    "GammeProduction",
    "Tracabilite",
    "Production",

    # Stock
    "Outil",
    "Materiau",
    "EmplacementStock",

    # Planning
    "PlanningEmploye",
    "PlanningMachine",
    "AffectationMachine",
    "Pointage",

    # QHSE
    "InstrumentControle",
    "ControlePiece",
    "EPI",
    "EPIUtilisateur",
    "AuditQualite",
    "NonConformite",
    "DocumentQualite",
    "DocumentsReglementaires",

    # Analyse et Logs
    "AnalyseFichier",
    "IALogs",

    # Systeme
    "Robotique",
    "ControleRobot",
    "SurveillanceCamera",
    "QrCodeObjet",

    # Associations
    "machine_outil",
]