# 💡 GreenTech Solutions

> _Modélisation et visualisation des performances énergétiques des logements en France_
>
> Projet réalisé dans le cadre du Master 2 **SISE – Statistique et Informatique pour la Science des donnéEs (Lyon 2)**  
> Année universitaire 2025-2026

---

## Objectif du projet

**GreenTech Solutions** vise à construire une chaîne complète d'analyse et de prédiction à partir des données publiques des **Diagnostics de Performance Énergétique (DPE)**.

Le projet couvre toutes les étapes du cycle de la donnée :

1. **Extraction et nettoyage** des données ADEME (DPE existants & neufs)  
2. **Analyse exploratoire et modélisation** (classification & régression)  
3. **Déploiement** d'une application web interactive sous **Streamlit**  
4. **Documentation** technique et fonctionnelle complètes

---

## Fonctionnalités

### Interface Utilisateur (Streamlit)
-  **Tableau de bord** : Visualisation interactive des données DPE
-  **Analyse** : Analyses statistiques approfondies
-  **Enedis** : Intégration des données de consommation Enedis
-  **Prédiction** : Prédiction d'étiquette DPE et de coûts énergétiques
-  API : mise à disposition de données et de modèles à travers une API
-  **Rafraîchissement des données** : Mise à jour automatique depuis l'API ADEME
-  **Réentraînement des modèles** : Réentraînement des modèles ML avec nouvelles données

### API REST (FastAPI)
-  **Prédictions individuelles** : Endpoint `/predict`
-  **Prédictions par lot** : Endpoint `/predict/batch`
-  **Métriques des modèles** : Endpoint `/models/metrics`
-  **Rafraîchissement des données** : Endpoint `/data/refresh`
-  **Réentraînement** : Endpoint `/models/retrain`

##  Prérequis

- Docker Desktop installé
- Docker Compose
- 4 GB RAM minimum

---

## Architecture du dépôt

```text
m2_enedis/
├── app/                     # code principal de l'application Streamlit
│   ├── app.py               # point d'entrée de l'application (lancement local ou Render)
│   ├── pages/               # pages multipages Streamlit (Contexte, Carte, Prédiction, etc.)
│   ├── components/          # petits modules réutilisables : graphiques, filtres, exports...
│   ├── model/               # modèles entraînés (fichiers .pkl / .joblib)
│   ├── utils/               # fonctions d'aide : prétraitement, calculs, API, logs...
│   ├── assets/              # feuilles CSS, icônes, images
│   └── styles/              # thème ou fichiers de configuration Streamlit (.toml / .css)
│
├── data/                    # jeux de données utilisés
│   ├── raw/                 # données brutes ADEME téléchargées (DPE existants et neufs)
│   └── processed/           # données nettoyées, enrichies, prêtes à l'analyse ou à la modélisation
│
├── notebooks/               # analyses exploratoires et modélisation (Jupyter)
│   ├── exploration.ipynb
│   ├── classification.ipynb
│   └── regression.ipynb
│
├── docker/                  # conteneurisation de l'application
│   └── Dockerfile           # instructions pour construire l'image Docker
│
├── docs/                    # documentation complète du projet
│   ├── doc_technique.md     # ≤ 2 pages : installation, architecture, dépendances
│   ├── doc_fonctionnelle.md # ≤ 2 pages : pages, fonctionnalités, parcours utilisateur
│   ├── rapport_ml.md        # 4-6 pages : contexte, modèles, résultats, interprétation
│   ├── SRS_TRACE.md         # matrice de traçabilité du cahier des charges
│   ├── SCRUM_GITHUB_CHECKLIST.md  # suivi organisationnel et qualité (Scrum / GitHub)
│   └── assets/              # schémas Draw.io, captures d'écran, logos
│
├── tests/                   # vérifications minimales
│   └── smoke_test.py        # "smoke test" : s'assure que les imports se font sans erreur
│
├── requirements.txt         # liste des librairies Python nécessaires
├── Procfile                 # commande exécutée sur Render / Heroku (déploiement automatique)
├── runtime.txt              # version Python utilisée
├── README.md                # ce fichier : présentation du projet
└── LICENSE
```

---

## Stack technique

| Domaine | Outils |
|----------|--------|
| Langage principal | Python 3.10+ |
| Data & ML | pandas, numpy, scikit-learn |
| Visualisation | Plotly Express, Streamlit |
| API & déploiement | requests, Render / Heroku |
| Conteneurisation | Docker |
| Collaboration | GitHub, Taiga (Scrum) |

---

## Équipe & rôles

| Membre | Rôle principal | Rôles secondaires |
|---------|----------------|-------------------|
| **Nico Dena** | Responsable data & intégration | Modélisation, documentation |
| **Modou Mboup** | Responsable ML & qualité | Interface, déploiement |
| **Rina Razafimahefa** | Responsable Interface & Design | Data, documentation |

> Chaque membre a contribué à plusieurs volets : la répartition est indicative mais la production a été collective et itérative selon les sprints.

---

## Organisation agile

- Outil de gestion : [Taiga.io](https://tree.taiga.io/) – Méthode **Scrum**  
- Backlog structuré en 6 Épics : Data / ML / Interface / Déploiement / Documentation / Gestion  
- Sprints hebdomadaires avec **revue et rétrospective** à chaque fin de sprint  

---

## Livrables clés

| Type | Fichier / dossier |
|-------|-------------------|
| Dataset final | `data/processed/dpe_full.parquet` |
| Modèles | `app/model/classification_model.pkl`, `app/model/regression_model.pkl` |
| Application Dash | `app/app.py` |
| Documentation technique | `docs/doc_technique.md` |
| Documentation fonctionnelle | `docs/doc_fonctionnelle.md` |
| Rapport ML | `docs/rapport_ml.md` |
| Matrice de conformité | `docs/SRS_TRACE.md` |

---

## Installation

### Option 1 : Avec Docker (Recommandé)

```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/greentech-project.git
cd greentech-project
=======
# Cloner le dépôt
git clone https://github.com/Modou010/m2_enedis.git
cd greentech-solutions

# 2. Démarrer l'application
docker-compose up -d streamlit

# 3. Accéder à l'application
# Streamlit : http://localhost:8502
# API : http://localhost:8000 (optionnel)
```

### Option 2 : Sans Docker (Local)

```bash
# 1. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Linux/Mac
# .\venv\Scripts\activate  # Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer Streamlit
streamlit run app.py
```

---

## Déploiement

L'application est hébergée sur **Render** :  
🔗 [Lien vers l'application déployée](https://...)  

Endpoints disponibles :
- `/predict` → prédiction DPE + consommation  
- `/health` → vérification du service  
- `/retrain` → réentraînement du modèle

---

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request, ou à nous laisser un message.

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit (`git commit -m 'Ajout fonctionnalité'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

---

## Licence

Ce projet est sous licence MIT.

---

## Contact

Pour toute question, contactez l'équipe GreenTech Solutions : franckdena@gmail.com, mboupmodou05@gmail.com, rsquare.europe@gmail.com

---
**Dernière mise à jour** : 2025-11-01