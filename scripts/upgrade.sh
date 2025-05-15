#!/bin/bash
echo "🔁 Lancement de la mise à jour..."

echo "🗃 Migration base de données..."
alembic upgrade head

echo "🔁 Restart du serveur..."
sudo systemctl restart mon-erp.service

echo "✅ Mise à jour terminée."
