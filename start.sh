#!/bin/bash

#echo "📦 Activation de l'environnement virtuel..."
#source venv/bin/activate

#echo "📦 Installation des dépendances..."
#pip install --upgrade pip
#pip install -r requirements.txt

#echo "🛠️ Initialisation de la base de données..."
#python scripts/init_db.py

#echo "✅ Exécution des tests unitaires..."
#pytest tests/

#echo "🚀 Lancement de l’application..."
#python main.py  # Remplace `main.py` par ton fichier de lancement principal


#!/bin/bash

# =============================
# Script de démarrage ERP Usinage
# =============================

echo "🔧 Activation de l'environnement virtuel Python..."
source venv/bin/activate || { echo "❌ Erreur : impossible d'activer venv"; exit 1; }

echo "🚀 Lancement du back-end Python (FastAPI)..."
cd Backend/backend || exit
uvicorn app:app --host 0.0.0.0 --port 8000 &
BACK_PID=$!
cd ../../

echo "🌐 Lancement du front-end Tauri..."
cd Front-end/ERP_interface || exit
npm run tauri dev &
FRONT_PID=$!
cd ../../

echo "✅ Services lancés :
- Backend PID : $BACK_PID
- Frontend PID : $FRONT_PID"

echo "📌 Pour arrêter proprement :"
echo "    kill $BACK_PID $FRONT_PID"
