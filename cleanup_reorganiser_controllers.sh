#!/bin/bash
echo '🚀 Réorganisation des controllers...'
mkdir -p backend/controllers/ia
if [ -f backend/controllers/analyse_fichier_controller.py ]; then mv backend/controllers/analyse_fichier_controller.py backend/controllers/ia/analyse_fichier_controller.py; fi
mkdir -p backend/controllers/finance
if [ -f backend/controllers/commande/commande_controller.py ]; then mv backend/controllers/commande/commande_controller.py backend/controllers/finance/commande_controller.py; fi
mkdir -p backend/controllers/finance
if [ -f backend/controllers/commandepiece/commande_piece_controller.py ]; then mv backend/controllers/commandepiece/commande_piece_controller.py backend/controllers/finance/commande_piece_controller.py; fi
mkdir -p backend/controllers/qualite
if [ -f backend/controllers/documentreglementaire_controller.py ]; then mv backend/controllers/documentreglementaire_controller.py backend/controllers/qualite/documentreglementaire_controller.py; fi
mkdir -p backend/controllers/qualite
if [ -f backend/controllers/evaluationfournisseur/evaluationfournisseur_controller.py ]; then mv backend/controllers/evaluationfournisseur/evaluationfournisseur_controller.py backend/controllers/qualite/evaluation_fournisseur_controller.py; fi
mkdir -p backend/controllers/achat
if [ -f backend/controllers/fournisseur/fournisseur_controller.py ]; then mv backend/controllers/fournisseur/fournisseur_controller.py backend/controllers/achat/fournisseur_controller.py; fi
mkdir -p backend/controllers/qualite
if [ -f backend/controllers/gestion_filtrage/gestion_filtrage_controller.py ]; then mv backend/controllers/gestion_filtrage/gestion_filtrage_controller.py backend/controllers/qualite/gestion_filtrage_controller.py; fi
mkdir -p backend/controllers/workflow
if [ -f backend/controllers/historiqueaction/historiqueaction_controller.py ]; then mv backend/controllers/historiqueaction/historiqueaction_controller.py backend/controllers/workflow/historiqueaction_controller.py; fi
mkdir -p backend/controllers/stock
if [ -f backend/controllers/materiau/materiau_controller.py ]; then mv backend/controllers/materiau/materiau_controller.py backend/controllers/stock/materiau_controller.py; fi
mkdir -p backend/controllers/traceabilite
if [ -f backend/controllers/qrcodeobjet/qrcodeobjet_controller.py ]; then mv backend/controllers/qrcodeobjet/qrcodeobjet_controller.py backend/controllers/traceabilite/qrcodeobjet_controller.py; fi
mkdir -p backend/controllers/production
if [ -f backend/controllers/robotique/robotique_controller.py ]; then mv backend/controllers/robotique/robotique_controller.py backend/controllers/production/robotique_controller.py; fi
mkdir -p backend/controllers/reporting
if [ -f backend/controllers/statfinance/statfinance_controller.py ]; then mv backend/controllers/statfinance/statfinance_controller.py backend/controllers/reporting/statfinance_controller.py; fi
mkdir -p backend/controllers/reporting
if [ -f backend/controllers/statrh/statrh_controller.py ]; then mv backend/controllers/statrh/statrh_controller.py backend/controllers/reporting/statrh_controller.py; fi
mkdir -p backend/controllers/reporting
if [ -f backend/controllers/statproduction/statproduction_controller.py ]; then mv backend/controllers/statproduction/statproduction_controller.py backend/controllers/reporting/statproduction_controller.py; fi
mkdir -p backend/controllers/securite
if [ -f backend/controllers/surveillancecamera/surveillance_camera_controller.py ]; then mv backend/controllers/surveillancecamera/surveillance_camera_controller.py backend/controllers/securite/surveillance_camera_controller.py; fi
rm -rf backend/controllers/epi
rm -rf backend/controllers/epiutilisateur
rm -rf backend/controllers/droit
rm -rf backend/controllers/gestion_acces
rm -rf backend/controllers/ged
echo '🧱 Ajout des __init__.py dans tous les sous-dossiers controllers'
find backend/controllers -type d -exec touch {}/__init__.py \;
echo '✅ Fini.'