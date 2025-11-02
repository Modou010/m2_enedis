#!/bin/bash

# Script de démarrage pour Docker
# Permet de lancer soit Streamlit soit FastAPI selon la variable d'environnement

set -e

echo "🚀 Démarrage de GreenTech Solutions..."
echo "📦 Mode: ${SERVICE_MODE:-streamlit}"

# Vérifier que les dossiers existent et ont les bonnes permissions
for dir in data models logs; do
    if [ ! -d "$dir" ]; then
        echo "📁 Création du dossier: $dir"
        mkdir -p "$dir"
    fi
    chmod -R 755 "$dir"
done

# Afficher les informations système
echo "🐍 Python version: $(python --version)"
echo "📊 Streamlit version: $(streamlit version 2>/dev/null || echo 'Non installé')"

# Lancer le service approprié
if [ "$SERVICE_MODE" = "streamlit" ]; then
    echo "📊 Démarrage de l'interface Streamlit..."
    echo "🌐 Accessible sur: http://localhost:8501"
    exec streamlit run app.py \
        --server.address=0.0.0.0 \
        --server.port=8501 \
        --server.headless=true \
        --browser.gatherUsageStats=false \
        --server.fileWatcherType=none
        
elif [ "$SERVICE_MODE" = "api" ]; then
    echo "🔌 Démarrage de l'API FastAPI..."
    echo "🌐 Accessible sur: http://localhost:8000"
    exec uvicorn api.main:app \
        --host 0.0.0.0 \
        --port 8000 \
        --reload
        
else
    echo "⚠️  SERVICE_MODE non défini ou invalide: '${SERVICE_MODE}'"
    echo "📊 Démarrage de Streamlit par défaut..."
    echo "🌐 Accessible sur: http://localhost:8501"
    exec streamlit run app.py \
        --server.address=0.0.0.0 \
        --server.port=8501 \
        --server.headless=true \
        --browser.gatherUsageStats=false \
        --server.fileWatcherType=none
fi