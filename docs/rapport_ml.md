# Rapport Machine Learning - GreenTech Solutions

Projet réalisé dans le cadre du Master 2 SISE - Statistique et Informatique pour la Science des DonnéEs  
Université Lyon 2 - Année universitaire 2025-2026  

---

## 1. Introduction

### 1.1 Contexte et motivation
Face à la crise énergétique et à la nécessité de réduire les émissions de CO₂, les **Diagnostics de Performance Énergétique (DPE)** sont devenus un enjeu central des politiques publiques. Ils permettent d’évaluer la consommation énergétique et les émissions des logements. Cependant, ces diagnostics sont souvent dispersés, hétérogènes et peu exploitables directement pour l’analyse à grande échelle.

Le projet **GreenTech Solutions** vise à proposer une approche complète d’analyse et de prédiction des performances énergétiques à partir des données publiques des DPE et de la consommation réelle Enedis, concentrée sur la région **Rhône-Alpes**.

### 1.2 Objectifs
- Analyser les performances énergétiques des logements existants et neufs.
- Créer un modèle de **classification** pour prédire l’étiquette DPE (A–G).
- Créer un modèle de **régression** pour estimer le **coût énergétique annuel (€)**.
- Développer une **application web** intégrant visualisation, prédiction et automatisation.

### 1.3 Enjeux
- Valoriser les données ouvertes de l’ADEME et d’Enedis.
- Concevoir des modèles robustes, interprétables et généralisables.
- Offrir un outil pratique d’aide à la rénovation et à la décision.

---

## 2. Données et Préparation

### 2.1 Sources
- **ADEME – DPE Existants** : ~50 000 enregistrements (160 variables).
- **ADEME – DPE Neufs** : ~5 000 enregistrements (95 variables).
- **Enedis** : données agrégées de consommation électrique.

### 2.2 Collecte des données
Les données ADEME ont été récupérées via API, avec gestion de la pagination et découpage dynamique pour éviter les limites de requêtes. Les DPE existants et neufs ont ensuite été fusionnés sur les colonnes communes (≈80).

**Fichiers générés :**
```
data_existants_69.csv
data_neufs_69.csv
donnees_ademe_unifiees.csv
data_enedis_69.csv
```

### 2.3 Nettoyage et préparation
- Suppression des doublons sur `numero_dpe`.
- Imputation des valeurs manquantes : médiane (numériques), mode (catégorielles), suppression si >50% manquantes.
- Traitement des outliers (IQR et seuils métiers).

### 2.4 Feature Engineering
Création de variables dérivées :
- `conso_par_m2 = conso_totale / surface`
- `age_batiment = annee_actuelle - annee_construction`
- `type_energie_recodee` (regroupement d’énergies)

Encodage : Label Encoding pour `type_batiment` et `type_energie_recodee`.

### 2.5 Sélection de variables
Critères : corrélation > 0.3, taux de remplissage > 80 %, importance métier.

**Variables retenues (10 features)** :
```
conso_auxiliaires_ef, cout_eclairage, conso_5_usages_par_m2_ef,
conso_5_usages_ef, surface_habitable_logement, cout_ecs,
type_batiment, conso_ecs_ef, conso_refroidissement_ef, type_energie_recodee
```

---

## 3. Analyse exploratoire

### 3.1 Répartition des étiquettes DPE
- 70 % des logements : classes D, E, ou F.
- Très faible proportion en A ou G (extrêmes).

### 3.2 Analyse descriptive
- Les maisons consomment ~30 % de plus que les appartements.
- Corrélation forte entre surface et coût énergétique (r ≈ 0.7).

### 3.3 Visualisations principales
- Histogramme des étiquettes DPE.
- Heatmap de corrélation.
- Carte interactive par code postal.
- Boxplots de consommation par type d’énergie.

---

## 4. Modélisation

### 4.1 Tâches de Machine Learning
- **Classification** : prédire `etiquette_dpe` (A–G).
- **Régression** : estimer `cout_total_5_usages` (€/an).

### 4.2 Split et prétraitement
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
```
- 80 % entraînement / 20 % test.
- Pas de normalisation (Random Forest non sensible aux échelles).

### 4.3 Modèle de classification
**Algorithme :** RandomForestClassifier

```python
n_estimators=100
max_depth=20
min_samples_split=5
min_samples_leaf=2
```

**Résultats :**
| Métrique | Score |
|-----------|--------|
| Accuracy  | 98.06 % |
| Precision | 0.98 |
| Recall    | 0.98 |
| F1-score  | 0.97 |

**Top Features :** `conso_5_usages_par_m2_ef`, `surface_habitable_logement`, `cout_ecs`.

**Matrice de confusion (résumé)** : diagonale dominante, très peu d’erreurs inter-classes.

### 4.4 Modèle de régression
**Algorithme :** RandomForestRegressor

| Métrique | Score |
|-----------|--------|
| R²        | 0.979 |
| MAE (€)   | 89.5 |
| RMSE (€)  | 142.3 |
| MAPE (%)  | 8.2 |

Distribution normale des résidus et homoscédasticité vérifiée.

### 4.5 Validation croisée
K-Fold (k=5) : moyenne 0.980 ± 0.001 (classification), 0.979 ± 0.001 (régression).

Les deux modèles montrent une **stabilité remarquable**.

### 4.6 Sauvegarde
Modèles exportés avec `joblib` :
```
models/classification_model.pkl
models/regression_model.pkl
metrics.json
```

---

## 5. Interprétation et discussion

### 5.1 Importance des variables
Les consommations totales et spécifiques par m² expliquent la majorité de la variance. Le type d’énergie et la surface complètent la hiérarchie.

### 5.2 Robustesse
Les modèles résistent bien au surapprentissage grâce à la diversité des échantillons et à la validation croisée. Cependant, la généralisation hors Rhône-Alpes n’a pas été testée.

### 5.3 Limites
- Données ADEME partiellement incohérentes (formats, doublons).
- Absence de variables contextuelles (revenu, isolation, altitude).
- DPE neufs sous-représentés.

### 5.4 Pistes d’amélioration
- Ajout de modèles explainables (XGBoost + SHAP).
- Intégration d’images de façades pour prédiction multimodale.
- Déploiement d’une API continue de rafraîchissement.

---

## 6. Intégration applicative

### 6.1 Architecture globale
```
Frontend  : Streamlit (interface utilisateur)
Backend   : FastAPI (API REST)
ML        : Scikit-learn (modèles Random Forest)
Data      : Pandas, NumPy
Docker    : Déploiement multi-service
```

### 6.2 API FastAPI
Endpoints clés :
- `/predict` (individuel)
- `/predict/batch` (CSV)
- `/models/retrain` (réentraînement)
- `/data/refresh` (rafraîchissement ADEME)

### 6.3 Interface Streamlit
- Tableau de bord dynamique (Plotly)
- Prédiction interactive
- Comparaison de logements
- Réentraînement et rafraîchissement en un clic

### 6.4 Dockerisation
Deux services :
- `streamlit` (port 8501)
- `api` (port 8000)

Volumes persistants : `data/`, `models/`, `logs/`.

---

## 7. Conclusion
Le projet **GreenTech Solutions** démontre la faisabilité d’un pipeline complet de Machine Learning appliqué aux données énergétiques publiques, combinant rigueur scientifique, automatisation et accessibilité utilisateur.

Les modèles atteignent des performances très élevées (R² = 0.979, F1 = 0.97) et peuvent servir de base à des outils d’aide à la décision pour la rénovation énergétique et la planification territoriale.

Les prochaines étapes visent à :
- Étendre la couverture géographique (niveau national).
- Intégrer des modèles explicatifs (Explainable AI).
- Déployer une API publique sur le cloud (FastAPI + Streamlit).

---

## Annexes
- **Notebook 1 :** [Extraction et préparation des données](./notebooks/1_extraction_prepartaion_donnees.ipynb)
- **Notebook 2 :** [Exploration et analyse](./notebooks/2_exploration_donnees.ipynb)
- **Notebook 3 :** [Modélisation ML](./notebooks/3_classification_regression.ipynb)
- **README complet :** [GreenTech Solutions](./readme.md)

---

**Auteurs :** Nico DENA, Modou MBOUP, Rina RAZAFIMAHEFA
**Date :** Novembre 2025