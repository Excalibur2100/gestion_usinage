from .base import Base
from .table.planning.affectation_machine import AffectationMachine
from .table.planning.pointages import Pointage
from .table.instrument_controle import InstrumentControle
from .table.controle_piece import ControlePiece
from .table.epi import EPI
from .table.epi_utilisateur import EPIUtilisateur
from .table.audit_qualite import AuditQualite
from .table.non_conformites import NonConformite
from .table.documents_qualite import DocumentQualite
from .table.ged.documents_reglementaires import DocumentsReglementaires
from .table.ia.analyse_fichiers import AnalyseFichier
from .table.ia.ia_logs import IALogs
from .table.production.liaison_machine_outil import machine_outil
from .table.utilisateur import Utilisateur
from .table.droit import Droit
from .table.droit_acces import DroitAcces
from .table.gestion_acces import GestionAcces
from .table.rh import RHs
from .table.absence import Absence
from .table.formation import Formation
from .table.sanction import Sanction
from .table.entretien import Entretien
from .table.rh.notation import NotationRH
from .table.ged.document_rh import DocumentRH
from .table.crm.clients import Client
from .table.achat.fournisseurs import Fournisseur
from .table.qualite.evaluations_fournisseur import EvaluationFournisseur
from .table.devis import Devis
from .table.achat.commandes import Commande
from .table.finance.commande_pieces import CommandePiece
from .table.factures import Facture
from .table.piece import Piece
from .table.programme_piece import ProgrammePiece
from .table.postprocesseur import PostProcesseur
from .table.machine import Machine
from .table.production.metrics_machines import MetricsMachine
from .table.gmao.maintenance import Maintenance
from .table.gammes_production import GammeProduction
from .table.traceabilite.tracabilite import Tracabilite
from .table.production import Production
from .table.production.liaison_machine_outil import machine_outil
from .table.employe import Employe

