#!/usr/bin/env bash
# =============================================================
# GreenTech Solutions – Mise à jour du dépôt local
# Généré le 2025-11-01 15:21
# =============================================================
# Ce script met à jour l'arborescence du repo pour l'aligner
# avec les livrables déclarés dans Taiga (Extraction, Modèles,
# Interface, Déploiement, Documentation).
# -------------------------------------------------------------
# ⚠️ Rien n'est automatique : tu peux lire, modifier, ou exécuter
# partiellement ce script à la main dans VS Code.
# -------------------------------------------------------------

echo "🚀 Début de la mise à jour GreenTech Solutions"

# === 1. Renommages et réorganisation =========================
echo "🧩 Renommage et organisation des fichiers..."

mv clean_data_funct.py dpe_cleaning.py 2>/dev/null || echo "(déjà renommé ou absent)"
mkdir -p src/data/raw src/data/processed

mv notebooks/1_extraction_prepartaion_donnees.ipynb notebooks/extraction_donnees.ipynb 2>/dev/null || true
mv notebooks/2_exploration_donnees.ipynb notebooks/exploration.ipynb 2>/dev/null || true
mv notebooks/3_classification_regression.ipynb notebooks/classification_regression.ipynb 2>/dev/null || true

mv docs/SRS_TRACE.md docs/doc_technique.md 2>/dev/null || true

# === 2. Fichiers à créer ======================================
echo "🧱 Création des fichiers manquants..."

# Déploiement
echo "web: streamlit run streamlit/app.py" > Procfile
echo "python-3.11.9" > runtime.txt

mkdir -p docker
cat > docker/Dockerfile <<'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r streamlit/requirements.txt
CMD ["streamlit", "run", "streamlit/app.py"]
EOF

# Données DPE neufs
mkdir -p src/data/raw/dpe_neufs
cat > src/data/raw/dpe_neufs/dpe_download_neuf.py <<'EOF'
# Script de récupération des DPE neufs via API ADEME
# Auteur : Rina / GreenTech Solutions
# À compléter avec endpoint et schéma de sauvegarde
EOF

# Documentation
touch docs/doc_fonctionnelle.md docs/rapport_ml.md

# === 3. Smoke test ============================================
echo "⚙️ Création du script de smoke test..."

mkdir -p scripts
cat > scripts/smoke_test.sh <<'EOF'
#!/usr/bin/env bash
echo "=== Smoke test : démarrage app ==="
python3 -c "import streamlit, sys; sys.exit(0)" && echo "✅ Import OK"
streamlit run streamlit/app.py --server.headless true --server.port 8501 &
sleep 10
curl -f http://localhost:8501/ || echo "⚠️ Streamlit non démarré"
pkill -f streamlit
echo "Smoke test terminé."
EOF
chmod +x scripts/smoke_test.sh

# === 4. Lien symbolique (optionnel) ============================
echo "🔗 Création du lien symbolique vers 'app' (optionnel)..."
ln -s streamlit app 2>/dev/null || echo "(lien déjà présent)"

# === 5. Résumé final ===========================================
echo "✅ Mise à jour terminée. Vérifie les changements :"
echo "   - dpe_cleaning.py créé"
echo "   - dossiers src/, docker/, scripts/ ajoutés"
echo "   - fichiers de déploiement et docs générés"
echo "   - lance 'bash scripts/smoke_test.sh' pour test rapide"

echo "💡 Tu peux valider avec 'git status' avant de commit."
