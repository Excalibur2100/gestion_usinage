import sys
import os
import json
import sys, os
from pathlib import Path

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
from starlette.templating import _TemplateResponse  # interne, à ne pas supprimer

# Corrige le path pour les imports relatifs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

# === ROUTERS BACKEND ===
from backend.controllers.securite.utilisateur_controller import router as utilisateur_router
from backend.controllers.rh.rh_controller import router as rh_router
from backend.controllers.crm.client_controller import router as client_router
from backend.controllers.achat.fournisseur_controller import router as fournisseur_router
from backend.controllers.achat.commande_fournisseur_controller import router as commande_fournisseur_router
from backend.controllers.finance.devis_controller import router as devis_router
from backend.controllers.production.piece_controller import router as piece_router
from backend.controllers.production.machine_controller import router as machine_router
from backend.controllers.production.outil_controller import router as outil_router
from backend.controllers.commercial.commande_piece_controller import router as commande_piece_router
from backend.controllers.production.programme_piece_controller import router as programme_router
from backend.controllers.production.gamme_production_controller import router as gamme_router
from backend.controllers.planning.planning_employe_controller import router as planning_employe_router
from backend.controllers.planning.planning_machine_controller import router as planning_machine_router
from backend.controllers.planning.pointage_controller import router as pointage_router
from backend.controllers.maintenance.maintenance_controller import router as maintenance_router
from backend.controllers.production.charges_machine_controller import router as charge_machine_router
from backend.controllers.securite.surveillance_camera_controller import router as surveillance_camera_router
from backend.controllers.ia.assistant_ia_controller import router as assistant_ia_router
from backend.controllers.ia.analyse_fichier_controller import router as analyse_fichier_router
from backend.controllers.securite.securite_controller import router as securite_router
from backend.controllers.ia.copilot_controller import router as copilot_router
from backend.controllers.rh.formation_controller import router as formation_router
from backend.controllers.rh.absence_controller import router as absence_router
from backend.controllers.rh.epi_controller import router as epi_router
from backend.controllers.systeme.version_systeme_controller import router as version_systeme_router
from backend.controllers.crm.adresse_client_controller import router as adresse_client_router
from backend.controllers.crm.fichier_client_controller import router as fichier_client_router
from backend.controllers.crm.tag_controller import router as tag_router
from backend.controllers.crm.tag_client_controller import router as tag_client_router
from backend.controllers.entreprise.entreprise_controller import router as entreprise_router
from backend.controllers.achat.ligne_commande_fournisseur_controller import router as ligne_commande_fournisseur_router
from backend.controllers.commercial.commande_controller import router as commande_router
from backend.controllers.commercial.ligne_commande_controller import router as ligne_commande_router
from backend.controllers.achat.reception_controller import router as reception_router
from backend.controllers.achat.facture_fournisseur_controller import router as facture_fournisseur_router
from backend.controllers.achat.avoir_fournisseur_controller import router as avoir_fournisseur_router
from backend.controllers.achat.evaluation_fournisseur_controller import router as evaluation_fournisseur_router
from backend.controllers.achat.reception_controller import router as reception_router
from backend.controllers.achat.type_fournisseur_controller import router as type_fournisseur_router
from backend.controllers.achat.suivi_reglement_fournisseur_controller import router as suivi_reglement_fournisseur_router
from backend.controllers.commercial.action_commerciale_controller import router as action_commerciale_router
from backend.controllers.commercial.campagne_commerciale_controller import router as campagne_commerciale_router
from backend.controllers.commercial.commande_piece_controller import router as commande_piece_router
from backend.controllers.commercial.condition_paiement_controller import router as condition_paiement_router
from backend.controllers.commercial.historique_prix_client_controller import router as historique_prix_client_router
from backend.controllers.commercial.objectif_commercial_controller import router as objectif_commercial_router
from backend.controllers.commercial.portefeuille_client_controller import router as portefeuille_client_router
from backend.controllers.commercial.segment_client_controller import router as segment_client_router
from backend.controllers.config.config_langue_controller import router as config_langue_router
from backend.controllers.config.config_metier_controller import router as config_metier_router
from backend.controllers.config.config_monnaie_controller import router as config_monnaie_router
from backend.controllers.config.config_notification_controller import router as config_notification_router
from backend.controllers.config.config_tva_controller import router as config_tva_router
from backend.controllers.crm.adresse_client_controller import router as adresse_client_router
from backend.controllers.crm.contact_client_controller import router as contact_client_router
from backend.controllers.crm.relance_controller import router as relance_router
from backend.controllers.crm.opportunite_controller import router as opportunite_router
from backend.controllers.crm.segment_client_controller import router as segment_client_router
from backend.controllers.entreprise.parametrage_interne_controller import router as parametrage_interne_router
from backend.controllers.entreprise.preference_entreprise_controller import router as preference_entreprise_router
from backend.controllers.entreprise.profil_acces_controller import router as profil_acces_router
from backend.controllers.entreprise.site_controller import router as site_router
from backend.controllers.entreprise.utilisateur_site_controller import router as utilisateur_site_router
from backend.controllers.finance.aide_calcul_tva_controller import router as aide_tva_router
from backend.controllers.finance.config_marge_controller import router as config_marge_router
from backend.controllers.finance.config_paiement_controller import router as config_paiement_router
from backend.controllers.finance.export_comptable_controller import router as export_comptable_router
from backend.controllers.finance.facture_controller import router as facture_router
from backend.controllers.finance.ligne_devis_controller import router as ligne_devis_router
from backend.controllers.finance.ligne_facture_controller import router as ligne_facture_router
from backend.controllers.finance.paiement_controller import router as paiement_router
from backend.controllers.finance.reglement_controller import router as reglement_router
from backend.controllers.finance.journal_comptable_controller import router as journal_comptable_router
from backend.controllers.finance.suivi_reglement_fournisseur_controller import router as suivi_reglement_fournisseur_router
from backend.controllers.ged.autorisation_document_controller import router as autorisation_document_router
from backend.controllers.ged.document_rh_controller import router as document_rh_router
from backend.controllers.ged.document_qhse_controller import router as documents_qhse_router
from backend.controllers.ged.document_qualite_controller import router as documents_qualite_router
from backend.controllers.ged.documents_reglementaires_controller import router as documents_reglementaires_router
from backend.controllers.ged.signature_document_controller import router as signature_document_router
from backend.controllers.ged.version_document_controller import router as version_document_router
from backend.controllers.ged.workflow_document_controller import router as workflow_document_router
from backend.controllers.ia.chiffrage_controller import router as chiffrage_router
from backend.controllers.ia.chiffrage_metiers_controller import router as chiffrage_metier_router
from backend.controllers.ia.historique_chiffrage_controller import router as historique_chiffrage_router
from backend.controllers.ia.conditions_coupe_controller import router as conditions_coupe_router
from backend.controllers.ia.conditions_coupe_metier_controller import router as conditions_coupe_metier_router
from backend.controllers.ia.code_generator_controller import router as code_generator_router
from backend.controllers.ia.code_generator_metier_controller import router as code_generator_metier_router
from backend.controllers.ia.logs_ia_controller import router as logs_ia_router
from backend.controllers.ia.optimisation_production_ai_controller import router as optimisation_ai_router
from backend.controllers.ia.optimisation_production_ai_metier_controller import router as optimisation_ai_metier_router
from backend.controllers.ia.prediction_maintenance_ai_controller import router as prediction_ai_router
from backend.controllers.ia.prediction_maintenance_ai_metier_controller import router as prediction_ai_metier_router
from backend.controllers.ia.reconnaissance_vocale_controller import router as reconnaissance_vocale_router
from backend.controllers.ia.reconnaissance_vocale_metier_controller import router as reconnaissance_vocale_metier_router
from backend.controllers.ia.simulation_chiffrage_controller import router as simulation_chiffrage_router
from backend.controllers.ia.simulation_chiffrage_metier_controller import router as simulation_chiffrage_metier_router
from backend.controllers.ia.suggestion_outil_controller import router as suggestion_outil_router
from backend.controllers.ia.suggestion_outil_metier_controller import router as suggestion_outil_metier_router
from backend.controllers.ia.assistant_ia_controller import router as assistant_ia_router
from backend.controllers.ia.assistant_ia_metier_controller import router as assistant_ia_metier_router
from backend.controllers.ia.chiffrage_piece_controller import router as chiffrage_piece_router




# === ROUTERS FRONT / VIEWS ===
from views.dashboard_ia.dashboard_views import router as dashboard_router
from views.dashboard.global_dashboard import router as global_dashboard_router
from views.chiffrage.chiffrage_view import router as chiffrage_router
from views.setup_view.setup_view import router as setup_router
from views.parametres_view.parametres_view import router as parametres_router
from views.planningemploye.planning_employe_view import router as planning_employe_view_router
from backend.controllers.commercial.remise_client_controller import router as remise_client_router
from backend.controllers.crm.historique_client_controller import router as historique_client_router
from backend.controllers.finance.commission_controller import router as commission_router



# === APP FASTAPI ===
app = FastAPI(
    title="ERP Usinage",
    description="API de gestion des opérations d'usinage pour l'ERP multi-entreprise.",
    version="1.0.0",
    contact={"name": "Support Technique", "email": "support@gestion-usinage.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)

# === ROUTERS API ===
app.include_router(utilisateur_router)
app.include_router(rh_router)
app.include_router(client_router)
app.include_router(fournisseur_router)
app.include_router(commande_fournisseur_router)
app.include_router(devis_router)
app.include_router(piece_router)
app.include_router(machine_router)
app.include_router(outil_router)
app.include_router(programme_router)
app.include_router(gamme_router)
app.include_router(planning_employe_router)
app.include_router(planning_machine_router)
app.include_router(pointage_router)
app.include_router(maintenance_router)
app.include_router(charge_machine_router)
app.include_router(surveillance_camera_router)
app.include_router(assistant_ia_router)
app.include_router(analyse_fichier_router)
app.include_router(securite_router)
app.include_router(copilot_router)
app.include_router(formation_router)
app.include_router(absence_router)
app.include_router(epi_router)
app.include_router(version_systeme_router)
app.include_router(adresse_client_router)
app.include_router(fichier_client_router)
app.include_router(tag_router)
app.include_router(tag_client_router)
app.include_router(entreprise_router)
app.include_router(ligne_commande_fournisseur_router)
app.include_router(commande_router)
app.include_router(ligne_commande_router)
app.include_router(reception_router)
app.include_router(facture_fournisseur_router)
app.include_router(avoir_fournisseur_router)
app.include_router(evaluation_fournisseur_router)
app.include_router(reception_router)
app.include_router(type_fournisseur_router)
app.include_router(suivi_reglement_fournisseur_router)
app.include_router(action_commerciale_router)
app.include_router(campagne_commerciale_router)
app.include_router(commande_piece_router)
app.include_router(condition_paiement_router)
app.include_router(historique_prix_client_router)
app.include_router(objectif_commercial_router)
app.include_router(portefeuille_client_router)
app.include_router(remise_client_router)
app.include_router(segment_client_router)
app.include_router(config_langue_router)
app.include_router(config_metier_router)
app.include_router(config_monnaie_router)
app.include_router(config_notification_router)
app.include_router(config_tva_router)
app.include_router(adresse_client_router)
app.include_router(contact_client_router)
app.include_router(relance_router)
app.include_router(historique_client_router)
app.include_router(opportunite_router)
app.include_router(segment_client_router)
app.include_router(parametrage_interne_router)
app.include_router(preference_entreprise_router)
app.include_router(profil_acces_router)
app.include_router(site_router)
app.include_router(utilisateur_site_router)
app.include_router(aide_tva_router)
app.include_router(commission_router)
app.include_router(config_marge_router)
app.include_router(config_paiement_router)
app.include_router(export_comptable_router)
app.include_router(facture_router)
app.include_router(ligne_devis_router)
app.include_router(ligne_facture_router)
app.include_router(paiement_router)
app.include_router(reglement_router)
app.include_router(journal_comptable_router)
app.include_router(suivi_reglement_fournisseur_router)
app.include_router(autorisation_document_router)
app.include_router(document_rh_router)
app.include_router(documents_qhse_router)
app.include_router(documents_qualite_router)
app.include_router(documents_reglementaires_router)
app.include_router(signature_document_router)
app.include_router(version_document_router)
app.include_router(workflow_document_router)
app.include_router(chiffrage_router)
app.include_router(chiffrage_metier_router)
app.include_router(historique_chiffrage_router)
app.include_router(conditions_coupe_router)
app.include_router(conditions_coupe_metier_router)
app.include_router(code_generator_router)
app.include_router(code_generator_metier_router)
app.include_router(logs_ia_router)
app.include_router(optimisation_ai_router)
app.include_router(optimisation_ai_metier_router)
app.include_router(prediction_ai_router)
app.include_router(prediction_ai_metier_router)
app.include_router(reconnaissance_vocale_router)
app.include_router(reconnaissance_vocale_metier_router)
app.include_router(simulation_chiffrage_router)
app.include_router(simulation_chiffrage_metier_router)
app.include_router(suggestion_outil_router)
app.include_router(suggestion_outil_metier_router)
app.include_router(assistant_ia_router)
app.include_router(assistant_ia_metier_router)
app.include_router(chiffrage_piece_router)

# === ROUTERS FRONT ===
app.include_router(dashboard_router)
app.include_router(global_dashboard_router)
app.include_router(chiffrage_router)
app.include_router(setup_router)
app.include_router(parametres_router)
app.include_router(planning_employe_view_router)

# === STATIC FILES ===
app.mount("/static", StaticFiles(directory="static"), name="static")

# === JINJA2 Templates ===
templates = Jinja2Templates(directory="templates")
templates.env = Environment(loader=FileSystemLoader("templates"))

# === Middleware pour redirection vers /setup ===
@app.middleware("http")
async def rediriger_si_non_configure(request: Request, call_next):
    if request.url.path.startswith("/static") or request.url.path.startswith("/setup"):
        return await call_next(request)

    config_path = Path("config_metiers.json")
    if not config_path.exists():
        return RedirectResponse(url="/setup")

    with open(config_path, "r") as f:
        config = json.load(f)

    if not config.get("setup_complet", False):
        return RedirectResponse(url="/setup")

    return await call_next(request)

# === Route Dashboard ===
@app.get("/dashboard", response_class=HTMLResponse)
async def afficher_dashboard(request: Request):
    data = {
        "nb_modules": 5,
        "nb_incomplets": 2,
        "composants": [
            {"nom": "Module 1", "chemins_trouves": ["chemin1", "chemin2"]},
            {"nom": "Module 2", "chemins_trouves": ["chemin1"]},
        ],
        "logs": [
            {
                "timestamp": "2025-04-25 10:00:00",
                "fichiers_crees": ["fichier1.py", "fichier2.py"],
            }
        ],
    }
    return templates.TemplateResponse("dashboard_templates/dashboard.html", {"request": request, **data})
