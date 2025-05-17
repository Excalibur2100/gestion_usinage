import sys
import os
import json
from pathlib import Path

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
from starlette.templating import _TemplateResponse  # interne, à ne pas supprimer

# Corrige le path pour les imports relatifs
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# === ROUTERS BACKEND ===
from backend.controllers.securite.utilisateur_controller import router as utilisateur_router
from backend.controllers.rh.rh_controller import router as rh_router
from backend.controllers.crm.client_controller import router as client_router
from backend.controllers.fournisseur.fournisseur_controller import router as fournisseur_router
from backend.controllers.achat.commande_fournisseur_controller import router as commande_fournisseur_router
from backend.controllers.finance.devis_controller import router as devis_router
from backend.controllers.piece.piece_controller import router as piece_router
from backend.controllers.production.machine_controller import router as machine_router
from backend.controllers.outil.outil_controller import router as outil_router
from backend.controllers.materiau.materiau_controller import router as materiau_router
from backend.controllers.commandepiece.commande_piece_controller import router as commande_piece_router
from backend.controllers.production.programme_piece_controller import router as programme_router
from backend.controllers.production.gamme_production_controller import router as gamme_router
from backend.controllers.gestion_acces.gestion_acces_controllers import router as gestion_acces_router
from backend.controllers.planning.planning_employe_controller import router as planning_employe_router
from backend.controllers.planning.planning_machine_controller import router as planning_machine_router
from backend.controllers.gestion_filtrage.gestion_filtrage_controller import router as gestion_filtrage_router
from backend.controllers.planning.pointage_controller import router as pointage_router
from backend.controllers.gmao.maintenance_controller import router as maintenance_router
from backend.controllers.production.charges_machine_controller import router as charge_machine_router
from backend.controllers.securite.surveillance_camera_controller import router as surveillance_camera_router
from backend.controllers.controlerobot.controle_robot_controller import router as controle_robot_router
from backend.controllers.ia.assistant_ia_controller import router as assistant_ia_router
from backend.controllers.codegen_controller import router as codegen_router
from backend.controllers.ia.metrics_controller import router as metrics_router
from backend.controllers.analyse_fichier_controller.analyse_fichier_controller import router as analyse_fichier_router
from backend.controllers.production.usinage_controller import router as usinage_router
from backend.controllers.securite.securite_controller import router as securite_router
from backend.controllers.ia.copilot_controller import router as copilot_router
from backend.controllers.rh.formation_controller import router as formation_router
from backend.controllers.rh.absence_controller import router as absence_router
from backend.controllers.epi.epi_controller import router as epi_router
from backend.controllers.ordre_fabrication.ordre_fabrication_controller import router as of_router
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











# === ROUTERS FRONT / VIEWS ===
from views.dashboard_ia.dashboard_views import router as dashboard_router
from views.dashboard.global_dashboard import router as global_dashboard_router
from views.chiffrage.chiffrage_view import router as chiffrage_router
from views.setup_view.setup_view import router as setup_router
from views.parametres_view.parametres_view import router as parametres_router
from views.planningemploye.planning_employe_view import router as planning_employe_view_router

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
app.include_router(materiau_router)
app.include_router(commande_piece_router)
app.include_router(programme_router)
app.include_router(gamme_router)
app.include_router(gestion_acces_router)
app.include_router(planning_employe_router)
app.include_router(planning_machine_router)
app.include_router(gestion_filtrage_router)
app.include_router(pointage_router)
app.include_router(maintenance_router)
app.include_router(charge_machine_router)
app.include_router(surveillance_camera_router)
app.include_router(controle_robot_router)
app.include_router(assistant_ia_router)
app.include_router(codegen_router)
app.include_router(metrics_router, prefix="/api", tags=["Metrics"])
app.include_router(analyse_fichier_router)
app.include_router(usinage_router)
app.include_router(securite_router)
app.include_router(copilot_router)
app.include_router(formation_router)
app.include_router(absence_router)
app.include_router(epi_router)
app.include_router(of_router)
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
