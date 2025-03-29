from fastapi import FastAPI
from controllers.utilisateur.utilisateur_controller import router as utilisateur_router
from controllers.rh.rh_controller import router as rh_router
from controllers.client.client_controller import router as client_router
from controllers.fournisseur.fournisseur_controller import router as fournisseur_router
from controllers.commande.commande_controller import router as commande_router
from controllers.devis.devis_controller import router as devis_router
from controllers.piece.piece_controller import router as piece_router
from controllers.machine.machine_controller import router as machine_router
from controllers.outil.outil_controller import router as outil_router
from controllers.materiau.materiau_controller import router as materiau_router
from controllers.commande_piece_controller import router as commande_piece_router
from controllers.programme_piece_controller import router as programme_router
from controllers.gamme_production_controller import router as gamme_router
from controllers.gestion_acces_controllers import router as gestion_acces_router
from controllers.planning_employe_controller import router as planning_employe_router
from controllers.planning_machine_controller import router as planning_machine_router
from controllers.gestion_filtrage_controller import router as gestion_filtrage_router
from controllers.pointage.pointage_controller import router as pointage_router
from controllers.maintenance.maintenance_controller import router as maintenance_router
from controllers.charge_machine_controller import router as charge_machine_router
from controllers.surveillance_camera_controller import router as surveillance_camera_router
from controllers.controle_robot_controller import router as controle_robot_router
from controllers.assistant_ia_controller import router as assistant_ia_router
from controllers.codegen_controller import router as codegen_router
from controllers.ia.router_ia import router as router_ia
from fastapi.staticfiles import StaticFiles
from controllers.ia.metrics_controller import router as metrics_router
from controllers.analyse_fichier_controller import router as analyse_fichier_router
from controllers.usinage_controller import router as usinage_router

app = FastAPI(
    title="API Gestion Usinage",
    version="1.0.0"
)

# Inclusion des routeurs
app.include_router(utilisateur_router)
app.include_router(rh_router)
app.include_router(client_router)
app.include_router(fournisseur_router)
app.include_router(commande_router)
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
app.include_router(router_ia)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(metrics_router, prefix="/api", tags=["Metrics"])
app.include_router(analyse_fichier_router)
app.include_router(usinage_router)

# Test de vie de l’API
@app.get("/")
def health_check():
    return {"message": "API Gestion Usinage opérationnelle"}