#!/bin/bash
echo '🚀 Début de la réorganisation du projet...'

# === Création des dossiers models ===
mkdir -p backend/db/models/tables/achat
mkdir -p backend/db/models/tables/commercial
mkdir -p backend/db/models/tables/crm
mkdir -p backend/db/models/tables/finance
mkdir -p backend/db/models/tables/gmao
mkdir -p backend/db/models/tables/ia
mkdir -p backend/db/models/tables/planning
mkdir -p backend/db/models/tables/production
mkdir -p backend/db/models/tables/qualite
mkdir -p backend/db/models/tables/rh
mkdir -p backend/db/models/tables/securite
mkdir -p backend/db/models/tables/stock
mkdir -p backend/db/models/tables/traceabilite
mkdir -p backend/db/models/tables/workflow

# === Création des dossiers schemas ===
mkdir -p backend/schemas/achat
mkdir -p backend/schemas/commercial
mkdir -p backend/schemas/crm
mkdir -p backend/schemas/finance
mkdir -p backend/schemas/gmao
mkdir -p backend/schemas/ia
mkdir -p backend/schemas/planning
mkdir -p backend/schemas/production
mkdir -p backend/schemas/qualite
mkdir -p backend/schemas/rh
mkdir -p backend/schemas/securite
mkdir -p backend/schemas/stock
mkdir -p backend/schemas/traceabilite
mkdir -p backend/schemas/workflow

# === Création des dossiers services ===
mkdir -p backend/services/achat
mkdir -p backend/services/commercial
mkdir -p backend/services/crm
mkdir -p backend/services/finance
mkdir -p backend/services/gmao
mkdir -p backend/services/ia
mkdir -p backend/services/planning
mkdir -p backend/services/production
mkdir -p backend/services/qualite
mkdir -p backend/services/rh
mkdir -p backend/services/securite
mkdir -p backend/services/stock
mkdir -p backend/services/traceabilite
mkdir -p backend/services/workflow

# === Création des dossiers controllers ===
mkdir -p backend/controllers/achat
mkdir -p backend/controllers/commercial
mkdir -p backend/controllers/crm
mkdir -p backend/controllers/finance
mkdir -p backend/controllers/gmao
mkdir -p backend/controllers/ia
mkdir -p backend/controllers/planning
mkdir -p backend/controllers/production
mkdir -p backend/controllers/qualite
mkdir -p backend/controllers/rh
mkdir -p backend/controllers/securite
mkdir -p backend/controllers/stock
mkdir -p backend/controllers/traceabilite
mkdir -p backend/controllers/workflow

# === Suppression des anciens dossiers inutiles ===
rm -rf old
rm -rf temp
rm -rf tests
rm -rf archives

echo '✅ Réorganisation terminée.'
