<<<<<<< HEAD
# 🌿 GreenTech Solutions - Dashboard Énergétique

Application Streamlit d'analyse des données énergétiques ADEME et Enedis.
=======
# 💡 GreenTech Solutions

> _Modélisation et visualisation des performances énergétiques des logements en France_
>
> Projet réalisé dans le cadre du Master 2 **SISE – Statistique et Informatique pour la Science des donnéEs (Lyon 2)**  
> Année universitaire 2025-2026
> 
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
---

## Objectif du projet

L'objectif de **GreenTech Solutions** est de construire une chaîne complète d'analyse et de prédiction à partir des données publiques des **Diagnostics de Performance Énergétique (DPE)**.

Le projet couvre toutes les étapes du cycle de la donnée :

1. **Extraction et nettoyage** des données ADEME (DPE existants & neufs)  
2. **Analyse exploratoire et modélisation** (classification & régression)  
3. **Déploiement** d'une application web interactive sous **Streamlit**  
4. **Documentation** technique et fonctionnelle

---


## 🚀 Fonctionnalités

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
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80

##  Prérequis

- Docker Desktop installé
- Docker Compose
- 4 GB RAM minimum

<<<<<<< HEAD
## 🚀 Installation rapide
=======
---

##  Structure du projet

```
greentech-solutions/
├── Data/                                               # Données provenant des Apis
├   ├──data_ademe_existants_69.csv
│   ├──data_ademe_existants_69.csv
│   ├──donnees_enedis_69_.csv                           # Application Streamlit principale
├── Notebooks/
├   ├──1_extraction_preparation_donnees.ipynb
│   ├──2_exploration_donnees.ipynb
│   ├──3_classification_regression.ipynb
├── streamlit/
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
├── Dockerfile                     
├── docker-compose.yml             
├── docker-entrypoint.sh           
├── requirements.txt
├── .dockerignore                  
└── README.md
```
<p align="center"><img src="schema_archicture_projet.jpg" alt="Schéma d’architecture du projet" width="80%"></p>



## Stack technique

| Domaine | Outils |
|----------|--------|
| Langage principal | Python 3.10+ |
| Data & ML | pandas, numpy, scikit-learn |
| Visualisation | Plotly Express, Streamlit |
| API & déploiement | FastAPI, unicorn, Render |
| Conteneurisation | Docker |
| Collaboration | GitHub, Taiga (Scrum) |

---

## Équipe & rôles

| Membre | Rôle principal | Rôles secondaires |
|---------|----------------|-------------------|
| **Nico Dena** | Responsable data & intégration |Ingestion, Modélisation et documentation |
| **Modou Mboup** | Responsable ML & qualité | Interface, déploiement |
| **Rina Razafimahefa** | Responsable interface & design | Data, documentation |

> Chaque membre a contribué à plusieurs volets du projet : la répartition est indicative mais la production a été collective et itérative selon les sprints.

---

## Organisation agile

- Outil de gestion : [Taiga.io](https://tree.taiga.io/) – Méthode **Scrum**  
- Backlog structuré en 6 Épics : Data / ML / Interface / Déploiement / Documentation / Gestion  
- Sprints hebdomadaires (burndown suivi automatiquement)  
- Revue et rétrospective à chaque fin de sprint  

---

## Livrables clés

| Type | Fichier / dossier |
|-------|-------------------|
| Dataset final | `Data/donnees_ademe_finales_nettoyees_69_final_pret.csv`, `Data/donnees_enedis_69_finales.csv` |
| Modèles | `streamlit/models/classification_model.pkl`, `streamlit/models/regression_model.pkl` |
| Application Streamlit | `streamlit/app.py` |
| Documentation technique | `docs/doc_technique.md` |
| Documentation fonctionnelle | `docs/doc_fonctionnelle.md` |
| Rapport ML | `docs/rapport_ml.md` |
| Vidéo démo | 🔗 _[Lien à venir]_ |

---


## 🛠️ Installation
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80

### Option 1 : Avec Docker (Recommandé)

```bash
<<<<<<< HEAD
# 1. Cloner le projet
git clone https://github.com/votre-username/greentech-project.git
cd greentech-project
=======
# Cloner le dépôt
git clone https://github.com/Modou010/m2_enedis.git
cd greentech-solutions
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80

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
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\activate  # Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer Streamlit
streamlit run app.py
```

<<<<<<< HEAD
## 📁 Structure du projet

```
greentech-project/
├── app.py                 # Application principale
├── pages/                 # Pages Streamlit
│   ├── analysis.py       # Analyses ADEME
│   ├── enedis.py         # Analyses Enedis
│   └── about.py          # À propos
├── data/                  # Données CSV
├── models/                # Modèles ML
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Commandes utiles

### Avec Make
=======
### Option 2 : Avec Docker (Recommandé)

```bash
# Construire et lancer les services
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down
```

##  Accès aux services

Une fois lancé :

- **Interface Streamlit** : [http://localhost:8501](http://localhost:8501)
- **API FastAPI** : [http://localhost:8000](http://localhost:8000)
- **Documentation API** : [http://localhost:8000/docs](http://localhost:8000/docs)

## Rafraîchissement des données

### Via l'interface Streamlit
1. Aller dans " Rafraîchir données"
2. Choisir le mode (nouveaux DPE uniquement ou rechargement complet)
3. Cliquer sur "Lancer le rafraîchissement"
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80

```bash
make build          # Construire les images
make streamlit      # Démarrer Streamlit
make logs           # Voir les logs
make down           # Tout arrêter
make clean          # Nettoyer
```

<<<<<<< HEAD
### Avec Docker Compose

=======
## Réentraînement des modèles

### Via l'interface Streamlit
1. Aller dans " Réentraîner modèles"
2. Configurer les hyperparamètres (optionnel)
3. Cliquer sur "Lancer l'entraînement"

### Via l'API
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80
```bash
docker-compose up -d streamlit       # Démarrer
docker-compose logs -f streamlit     # Logs en temps réel
docker-compose restart streamlit     # Redémarrer
docker-compose down                  # Arrêter
```

## 🔧 Développement

### Mode hot-reload

Décommentez dans `docker-compose.yml` :

```yaml
volumes:
  - ./pages:/app/pages
  - ./app.py:/app/app.py
```

Les modifications seront prises en compte automatiquement !

### Reconstruire après modifications

```bash
docker-compose up -d --build streamlit
```

## 📊 Accès aux services

| Service   | URL                        | Description          |
| --------- | -------------------------- | -------------------- |
| Streamlit | http://localhost:8502      | Interface principale |
| API       | http://localhost:8000      | API REST (optionnel) |
| Swagger   | http://localhost:8000/docs | Documentation API    |

## 🐛 Résolution de problèmes

### Port déjà utilisé

```bash
# Changer le port dans docker-compose.yml
ports:
  - "8503:8501"  # Utiliser 8503
```

### Logs pour déboguer

```bash
docker-compose logs -f streamlit
```

<<<<<<< HEAD
### Redémarrage complet

```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d streamlit
```

## 📦 Données requises

Placez vos fichiers CSV dans le dossier `data/` :

- `donnees_ademe_finales_nettoyees_69_final_pret.csv`
- `donnees_enedis_finales_69.csv`
=======
## 📊 Modèles de Machine Learning

### Modèle de Classification
- **Algorithme** : Random Forest Classifier
- **Objectif** : Prédire l'étiquette DPE (A, B, C, D, E, F, G)
- **Performance** : ~96% accuracy

### Modèle de Régression
- **Algorithme** : DecisionTree Regressor
- **Objectif** : Prédire le coût total des 5 usages (€/an)
- **Performance** : R² > 0.97
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80

## 👥 Contribution

<<<<<<< HEAD
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit (`git commit -m 'Ajout fonctionnalité'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📝 License

MIT License

## 👨‍💻 Auteur

Modou Mboup - M2 Projet Énergétique 2025

---

**Note** : Pour toute question, ouvrir une issue sur GitHub.
=======
## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request, ou à nous laisser un message

## 📄 Licence

Ce projet est sous licence MIT.

## Contact

Pour toute question, contactez l'équipe GreenTech Solutions : franckdena@gmail.com, mboupmodou05@gmail.com, n.razafimahefa@univ-lyon2.fr

---

**Version** : 1.0.0  
**Dernière mise à jour** : 2025
>>>>>>> 6d7b8eb60e07cb371d6f937da3311d6eed4bfc80
