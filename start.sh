#!/bin/bash

echo "📦 Activation de l'environnement virtuel..."
source venv/bin/activate

echo "📦 Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🛠️ Initialisation de la base de données..."
python scripts/init_db.py

echo "✅ Exécution des tests unitaires..."
pytest tests/

echo "🚀 Lancement de l’application..."
python main.py  # Remplace `main.py` par ton fichier de lancement principal
