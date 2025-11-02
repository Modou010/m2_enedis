Dernière mise à jour : 2025-11-01  
Version 1.0 – Novembre 2025  

# Documentation technique - GreenTech Solutions

Projet réalisé dans le cadre du Master 2 SISE – Statistique et Informatique pour la Science des Données  
Université Lyon 2 - Année universitaire 2025-2026  

Application web Streamlit de modélisation et de prédiction de la performance énergétique des logements en France à partir des données publiques ADEME DPE.

---

## 1. Objectif du document

Ce document décrit la conception technique du projet GreenTech Solutions : architecture logicielle, environnement, pipeline ML et intégration de l'application web.  
Il sert de support à la maintenance et à la reproductibilité du projet.  
L'ensemble du code est open-source et disponible sur GitHub.

---

## 2. Architecture globale du projet

### 2.1 Schéma général

<p align="center"><img src="schema_archicture_projet.jpg" alt="Schéma d’architecture du projet" width="80%"></p>


### 2.2 Structure du dépôt

```
.
greentech-solutions/
├── Data/                                               # Données provenant des Apis
├   ├──data_ademe_existants_69.csv
│   ├──data_ademe_existants_69.csv
│   ├──donnees_enedis_69_.csv  
├── Docs/                                               # documentation
├   ├──assets/
│   ├──management/
├   ├──doc_fontctionnelle.md
│   ├──doc_technique.md
│   ├──rapport_ml.md
│   ├──presentation_projet.md                           
├── Notebooks/
├   ├──1_extraction_preparation_donnees.ipynb
│   ├──2_exploration_donnees.ipynb
│   ├──3_classification_regression.ipynb
├── streamlit/                          # dossier application  
|   ├── app.py                          # Application Streamlit principale
|   ├── pages/                          # Pages Streamlit
|   │   ├── welcome.py
|   │   ├── home.py
|   │   ├── analysis.py
|   │   ├── enedis.py
|   │   ├── prediction.py
|   │   ├── compare.py
|   │   ├── about.py
|   │   ├── refresh_data.py            
|   │   └── retrain_models.py          
|   ├── utils/                         # Modules utilitaires
|   │   ├── data_loader.py
|   │   ├── model_utils.py
|   │   ├── data_refresher.py          
|   │   └── model_trainer.py           
|   ├── api/                           # API FastAPI
|   │   └── main.py                    
|   ├── models/                        # Modèles ML sauvegardés
|   │   ├── classification_model.pkl
|   │   ├── regression_model.pkl
|   │   └── metrics.json
|   ├── data/                          # Données
|   │   ├── donnees_ademe_finales_nettoyees_69_final_pret.csv
|   │   ├──donnees_enedis_69_finales.csv
|   │   ├── adresses-69.csv
|   │   └── metadata.json
|   ├── app.py                          # Application Streamlit principale
|   ├── pages/                          # Pages Streamlit
|   │   ├── welcome.py
|   │   ├── home.py
|   │   ├── analysis.py
|   │   ├── enedis.py
|   │   ├── prediction.py
|   │   ├── compare.py
|   │   ├── about.py
|   │   ├── refresh_data.py            
|   │   └── retrain_models.py          
|   ├── utils/                         # Modules utilitaires
|   │   ├── data_loader.py
|   │   ├── model_utils.py
|   │   ├── data_refresher.py          
|   │   └── model_trainer.py           
|   ├── api/                           # API FastAPI
|   │   └── main.py                    
|   ├── models/                        # Modèles ML sauvegardés
|   │   ├── classification_model.pkl
|   │   ├── regression_model.pkl
|   │   └── metrics.json
|   ├── data/                          # Données application
|   │   ├── donnees_ademe_finales_nettoyees_69_final_pret.csv
|   │   ├──donnees_enedis_69_finales.csv
|   │   ├── adresses-69.csv
|   │   └── metadata.json
|   ├── Dockerfile                     
|   ├── docker-compose.yml             
|   ├──docker-entrypoint.sh           
|   ├── requirements.txt
|   ├── .dockerignore                  
└── ────README.md
```

> L'application Streamlit est centralisée dans le dossier `streamlit/`.  
> Les notebooks et scripts de nettoyage sont conservés pour la reproductibilité du pipeline.

---

## 3. Environnement et dépendances

### 3.1. Version Python
- Python 3.11.x

### 3.2. Installation locale
prérequis : avoir docker installé et avoir les images greentech-streamlit.tar ; greentch-api.tar
```bash
# charger l'image de l'application
docker load -i greentech-streamlit.tar
# charger l'image de l'api
docker load -i greentech-api.tar
# verifier que les images sont chargés
docker images
# lancer l'application
docker-compose up -d

# acceder à l'application
# ** frontend streamlit : http://localhost/8501
# ** API : http://localhost/8000

# arreter l'application
docker-compose down
```

### 3.3. Librairies principales

| Catégorie | Librairies | Rôle |
|------------|-------------|------|
| Traitement de données | pandas, numpy | Chargement et transformation |
| Modélisation | scikit-learn, joblib | Entraînement et sauvegarde des modèles |
| Visualisation | matplotlib, seaborn, plotly | Graphiques et figures ML |
| Interface web | streamlit | UI et interactions |
| Déploiement | render, docker | Hébergement et conteneurisation |

### 3.4. Configuration Render

| Fichier | Contenu clé |
|----------|--------------|
| Procfile | web: streamlit run streamlit/app.py --server.port=$PORT --server.address=0.0.0.0 |
| runtime.txt | python-3.11.8 |
| requirements.txt | Liste exhaustive des dépendances validées |

---

## 4. Pipeline de données et de modélisation

### 4.1. Flux général

1. Extraction : téléchargement des jeux ADEME DPE (existants + neufs).  
2. Nettoyage : suppression des doublons, traitement des valeurs manquantes, typage.  
3. Feature Engineering : normalisation, encodage, sélection des variables pertinentes.  
4. Entraînement : séparation Train/Test (80/20) + cross-validation.  
5. Évaluation : calcul Accuracy, F1, RMSE, MAE, R².  
6. Sauvegarde : export des modèles `.pkl` dans `streamlit/model/`.  
7. Chargement dans l'app : fonctions `load_model()` et `predict()` dans `streamlit/utils/`.

### 4.2. Modèles utilisés

| Tâche | Algorithme principal | Alternatives testées | Sélection finale |
|-------|----------------------|----------------------|------------------|
| Classification DPE | Gradient Boosting Classifier | Logistic Regression, Random Forest | Gradient Boosting |
| Régression consommation | Random Forest Regressor | Linear Regression, Gradient Boosting Regressor | Random Forest Regressor |

### 4.3. Métriques clés

| Modèle | Jeu | Principales métriques | Commentaire |
|---------|-----|------------------------|--------------|
| Classification DPE | Test | Accuracy ≈ 0.84 / F1 macro ≈ 0.80 | Bonne stabilité inter-folds |
| Régression consommation | Test | RMSE ≈ 32 / R² ≈ 0.73 | Légère sous-estimation des très hautes consommations |

---

## 5. Application Streamlit

### 5.1. Structure fonctionnelle

L'application repose sur Streamlit et permet :
- la visualisation des données DPE,
- la prédiction de la classe énergétique et de la consommation,
- l'export des résultats.

| Élément | Description | Fichier(s) |
|----------|--------------|-------------|
| Interface principale | Point d'entrée | streamlit/app.py |
| Pages Streamlit | Contexte, Prédiction | streamlit/pages/context.py, streamlit/pages/predict.py |
| Composants graphiques | Graphiques, filtres | streamlit/components/charts.py |
| Modèles chargés | .pkl | streamlit/model/ |
| Fonctions internes | predict(), check_health() | streamlit/utils/ |

---

### 5.2. Pages principales

#### Page Contexte
Exploration visuelle des données avec histogrammes, boxplots, carte interactive (Plotly) et filtres.

#### Page Prédiction
Saisie utilisateur : surface, année, chauffage, zone climatique, énergie.  
Affichage des prédictions avec `st.metric()`.

---

## 6. Déploiement Render et Docker

### 6.1. Render
Déploiement via Render (Free Tier).  
Procfile et runtime configurés pour Streamlit.

### 6.2. Docker
Image légère basée sur `python:3.11-slim` :

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "streamlit/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 7. Maintenance et évolutions

| Script | Rôle |
|--------|------|
| src/train.py | Réentraîner les modèles |
| scripts/smoke_test.sh | Vérifier le démarrage Streamlit |
| src/evaluate.py | Calcul des métriques |

Évolutions prévues :
- CI/CD via GitHub Actions  
- API FastAPI pour les prédictions  
- Tracking des métriques avec MLflow

---

## 8. Annexes et traçabilité

### 8.1. Matrice projet

| Épopée | Livrable | Statut |
|---------|-----------|--------|
| E01 – Données | Dataset propre | ✅ |
| E02 – Modèles ML | .pkl + rapport | ✅ |
| E03 – App Streamlit | UI + exports | ✅ |
| E04 – Déploiement | URL Render + Docker | 🚧 |
| E05 – Docs | Technique / Fonctionnelle / ML | 🚧 |
| E06 – Gestion projet | Rôles + suivi | ✅ |

### 8.2 Leçons apprises

| Points positifs | Difficultés | Améliorations |
|------------------|--------------|----------------|
| Bonne coordination | Fusion Git | Automatiser merges |
| Interface stable | Render lent | Optimiser dépendances |
| Pipeline reproductible | Variance modèles | MLflow |

---

## 9. Références

- ADEME - Données publiques DPE : https://data.ademe.fr  
- Streamlit : https://docs.streamlit.io  
- Scikit-learn : https://scikit-learn.org/stable/  
- Render : https://render.com/docs

---

## Annexes liées

- [Annexe A - Matrice de traçabilité du sujet](management/SRS_Trace.md)  
- [Annexe B - Matrice de traçabilité projet](management/Trace_project.md)

---

Auteurs : Modou, Nico, Rina  
Version : 1.0 – Novembre 2025
