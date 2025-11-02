# 💡 GreenTech Solutions

> _Modélisation et visualisation des performances énergétiques des logements en France_
>
> Projet réalisé dans le cadre du Master 2 **SISE - Statistique et Informatique pour la Science des donnéEs (Lyon 2)**  
> Année universitaire 2025-2026

---

## Objectif du projet

**GreenTech Solutions** vise à construire une chaîne complète d'analyse et de prédiction à partir des données publiques des **Diagnostics de Performance Énergétique (DPE)**.

Le projet couvre toutes les étapes du cycle de la donnée :

1. **Extraction et nettoyage** des données ADEME (DPE existants & neufs)  
2. **Analyse exploratoire et modélisation** (classification & régression)  
3. **Déploiement** d'une application web interactive sous **Streamlit**  
4. **Documentation** technique et fonctionnelle complètes

L'application finale est développée en Python (Streamlit) et intègre des modèles de classification et régression pour estimer la classe DPE et la consommation énergétique d'un logement.

---

## Architecture du depot

```bash
m2_enedis/
├── app -> streamlit/                # Dossier principal de l'application Streamlit
│   ├── app.py                       # Point d'entrée Streamlit
│   ├── pages/                       # Pages (Contexte, Prediction, etc.)
│   ├── data/                        # Données sources (ADEME, Enedis)
│   ├── models/                      # Modèles sauvegardés (.pkl)
│   ├── assets/                      # Images et ressources statiques
│   └── utils/                       # Fonctions utilitaires
├── data/                            # Répertoire standard (non utilisé ici)
├── docker/                          # Fichiers Docker pour conteneurisation
├── docs/                            # Documentation technique, fonctionnelle et rapport ML
├── scripts/                         # Scripts annexes (tests, automatisations)
├── train_models_full.py             # Script principal d'entraînement des modèles
└── Procfile / runtime.txt           # Fichiers de configuration pour Render
```

---

## Installation et dépendances

### Créer l'environnement
```bash
conda create -n greentech python=3.11 -y
conda activate greentech
```

### Installer les dépendances
```bash
pip install -r streamlit/requirements.txt
```

---

## Entraînement des modèles

Le script principal d'entraînement est `train_models_full.py`.  
Il remplace les anciennes versions locales utilisées pour les tests intermédiaires.

### Exécution locale
```bash
python train_models_full.py
```

### Description
- Source de données : `streamlit/data/donnees_ademe_finales_nettoyees_69_final_pret.csv`
- Cibles :
  - Classification -> `etiquette_dpe`
  - Régression -> `conso_5_usages_par_m2_ef`
- Algorithmes : RandomForestClassifier et RandomForestRegressor
- Sorties générées :
  - `streamlit/models/classification_randomforest_full.pkl`
  - `streamlit/models/regression_randomforest_full.pkl`
  - Résumé des performances -> `docs/results_full.txt`

### Notes
- Le script utilise le dataset complet ADEME, sans échantillonnage.  
- Il crée automatiquement les répertoires necessaires (`streamlit/models`, `docs`).  
- Les anciennes versions (`train_models_local.py`, `train_models_light.py`) sont archivées dans `scripts/archive/`.  
- La graine aléatoire est fixée (`random_state=42`) pour garantir la reproductibilite des resultats.

---

## Validation et intégration Streamlit

Une fois les modèles entraines avec `train_models_full.py`, ils sont enregistres dans `streamlit/models/` et directement utilises par l application Streamlit.

### Chargement des modeles
Les modeles sont charges au demarrage via `streamlit/utils/model_utils.py` :
- `classification_randomforest_full.pkl`
- `regression_randomforest_full.pkl`

### Tests de bon fonctionnement
```bash
streamlit run streamlit/app.py
```
Verifier :
- Page Prediction : affichage des resultats de la classification et regression.
- Page Contexte : coherence des visualisations avec les donnees ADEME.

### Conseils
- En cas d erreur de chargement, verifier le chemin des fichiers `.pkl` et les permissions du dossier `streamlit/models/`.  
- Si le schema des donnees evolue, relancer `train_models_full.py`.  
- Les metriques detaillees sont sauvegardees dans `docs/results_full.txt`.

---

## Dockerisation

### Build local
```bash
docker build -t greentech-app -f docker/Dockerfile .
```

### Execution locale
```bash
docker run -p 8501:8501 greentech-app
# Acces via http://localhost:8501
```

### Exemple de Dockerfile minimal

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY streamlit/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 8501
CMD ["streamlit", "run", "streamlit/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

---

## Deploiement sur Render

1. Creer un nouveau Web Service via https://render.com
2. Connecter le depot GitHub  
3. Runtime : Python  
4. Build command :
   ```bash
   pip install -r streamlit/requirements.txt
   ```
5. Start command :
   ```bash
   streamlit run streamlit/app.py --server.port $PORT --server.address 0.0.0.0
   ```
6. Variables d environnement :
   - `PYTHONPATH=.`  
   - Version Python specifiee dans `runtime.txt` (ex. `python-3.11.9`)

Verifier ensuite que :
- L application se lance sans erreur.  
- Les modeles `.pkl` sont bien presents dans `streamlit/models/`.  
- Les pages Contexte et Prediction affichent des resultats coherents.

---

## Annexes

- Matrice de tracabilite projet : `docs/management/Trace_project.md`  
- Matrice de tracabilite SRS : `docs/management/SRS_Trace.md`  
- Resultats d entrainement complets : `docs/results_full.txt`  
- Smoke test : voir `scripts/smoke_test.sh`

---

## Auteurs

- Modou MBOUP - Modélisation et intégration ML  
- Nico DENA - Collecte et préparation des donnees  
- Rina RAZAFIMAHEFA - Documentation, interface Streamlit, coordination et qualité projet

Version : 1.0 - Novembre 2025