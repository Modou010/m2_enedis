# Rapport Machine Learning - GreenTech Solutions

Projet réalisé dans le cadre du Master 2 SISE - Statistique et Informatique pour la Science des DonnéEs  
Université Lyon 2 - Année universitaire 2025-2026  

---

## 1. Introduction

### 1.1 Contexte et motivation
Face à la crise énergétique et à la nécessité de réduire les émissions de CO₂, les **Diagnostics de Performance Énergétique (DPE)** sont devenus un enjeu central des politiques publiques. Ils permettent d'évaluer la consommation énergétique et les émissions des logements. Cependant, ces diagnostics sont souvent dispersés, hétérogènes et peu exploitables directement pour l'analyse à grande échelle.

Le projet **GreenTech Solutions** vise à proposer une approche complète d'analyse et de prédiction des performances énergétiques à partir des données publiques des DPE et de la consommation réelle Enedis, concentrée sur la région **Rhône-Alpes**.

### 1.2 Objectifs  

Le projet **GreenTech Solutions** poursuit plusieurs objectifs complémentaires :  
- **Analyser** les performances énergétiques des logements existants et neufs afin d’identifier les principaux facteurs influençant la consommation.  
- **Développer un modèle de classification** capable de prédire l’étiquette énergétique DPE (de A à G).  
- **Mettre en place un modèle de régression** permettant d’estimer le **coût énergétique annuel** (en euros) pour chaque logement.  
- **Concevoir une application web complète**, intégrant visualisation interactive, prédiction en temps réel et automatisation du réentraînement des modèles.  

---

### 1.3 Enjeux  

Ce projet s’inscrit dans une démarche de valorisation des **données ouvertes** issues de l’**ADEME** et d’**Enedis**, avec pour ambition de :  
- exploiter efficacement ces ressources publiques pour produire de la connaissance utile ;  
- concevoir des modèles **robustes, interprétables et généralisables**, adaptés aux spécificités du domaine énergétique ;  
- proposer un **outil d’aide à la rénovation et à la décision**, à destination des collectivités, professionnels et particuliers souhaitant améliorer la performance énergétique des bâtiments.  

---

## 2. Données et Préparation  

### 2.1 Sources  

Les données exploitées dans ce projet proviennent exclusivement de **sources publiques** liées à la performance énergétique des bâtiments :  
- **ADEME – DPE Existants** : environ **40 795 enregistrements** et **145 variables**, décrivant les caractéristiques énergétiques des logements déjà construits.  
- **ADEME – DPE Neufs** : environ **40 105 enregistrements** et **92 variables**, correspondant aux bâtiments récemment construits.  
- **Enedis** : données agrégées de **consommation électrique**, permettant de compléter les informations issues des DPE.  

Ces jeux de données couvrent la région **Rhône-Alpes** et offrent une base solide pour l’analyse énergétique et la modélisation.

---

### 2.2 Collecte des données  

Les données issues de l’ADEME ont été **récupérées via une API publique**, avec une gestion spécifique de la **pagination** et du **découpage dynamique** afin d’éviter les limitations de requêtes imposées par le service.  
Les bases relatives aux **DPE existants** et aux **DPE neufs** ont ensuite été **fusionnées** sur leurs **colonnes communes** (environ 80 variables), afin de constituer un ensemble de données unifié, homogène et prêt pour les étapes de nettoyage et de préparation.

### 2.3 Nettoyage et préparation  

Avant la phase de modélisation, un travail rigoureux de **nettoyage** et de **préparation** des données a été effectué afin d’assurer la fiabilité et la qualité des analyses. Les principales étapes ont été les suivantes :  
- **Suppression des doublons** pour éviter les biais liés à la redondance d’enregistrements.  
- **Imputation des valeurs manquantes** : utilisation de la **médiane** pour les variables numériques, du **mode** pour les variables catégorielles, et **suppression** des colonnes comportant plus de **50 % de valeurs manquantes**.  
- **Traitement des valeurs aberrantes (outliers)** à l’aide de la méthode de l’**IQR (Interquartile Range)** et de **seuils métiers** définis selon la cohérence énergétique attendue.  

Ces étapes ont permis d’obtenir un jeu de données propre, cohérent et prêt pour le feature engineering.

---

### 2.4 Feature Engineering  

Afin d’enrichir le jeu de données et d’améliorer la performance des modèles, plusieurs **variables dérivées** ont été créées :  
- `type_energie_recodee` : regroupement des différentes sources d’énergie (électricité, gaz, fioul, etc.) en catégories homogènes pour simplifier l’analyse.  

Les variables catégorielles ont ensuite été **encodées** afin de pouvoir être utilisées dans les algorithmes de Machine Learning :  
- **Label Encoding** appliqué aux variables `type_batiment` et `type_energie_recodee`.  

Ces transformations ont contribué à rendre le dataset plus exploitable et à renforcer la capacité explicative des futurs modèles.

### 2.5 Sélection de variables
Pour la sélection des variables, nous avons d’abord examiné les variables numériques à l’aide de la matrice de corrélation, afin d’identifier les éventuelles corrélations fortes entre elles. Concernant les variables qualitatives, nous avons étudié leurs associations à l’aide du test du Khi-deux, puis nous avons complété cette analyse en calculant le V de Cramer afin d’évaluer l’intensité des liaisons entre les variables.

**Variables retenues (9 features)** :
```
À la suite de l’analyse exploratoire des données, nous avons retenu les variables suivantes pour la modélisation :
conso_auxiliaires_ef, cout_eclairage, conso_5_usages_par_m2_ef, conso_5_usages_ef, surface_habitable_logement, cout_ecs, type_batiment, conso_ecs_ef, conso_refroidissement_ef et type_energie_recodee.
Ces variables ont été sélectionnées en raison de leur pertinence et de leur contribution potentielle à l’explication du phénomène étudié.
```

---

## 3. Analyse exploratoire

### 3.1 Répartition des étiquettes DPE
- 70 % des logements : classes D, E, ou F.
- Très faible proportion en A ou G (extrêmes).

### 3.2 Analyse descriptive
L’analyse descriptive a permis de dégager plusieurs tendances générales. Tout d’abord, il apparaît que les **maisons consomment en moyenne environ 30 % d’énergie de plus que les appartements**. Cette différence peut s’expliquer par une **surface habitable généralement plus importante**, ainsi que par une **moindre compacité thermique** des maisons individuelles.  
De plus, une **corrélation forte** (r ≈ 0.7) a été observée entre la **surface du logement** et le **coût énergétique total**, confirmant que la taille du logement est un facteur déterminant de la consommation énergétique. Ces premiers constats permettent de mieux comprendre la structure des données et d’orienter la sélection des variables pertinentes pour la suite du travail.  

---

### 3.3 Visualisations principales
Afin d’explorer visuellement les relations entre les variables, plusieurs représentations graphiques ont été réalisées :  
- un **histogramme des étiquettes DPE**, permettant d’observer la répartition des logements selon leur performance énergétique ;  
- une **heatmap de corrélation**, utilisée pour identifier les liens entre variables numériques et détecter d’éventuelles redondances ;  
- une **carte interactive par code postal**, mettant en évidence la variabilité géographique des consommations énergétiques ;  
- enfin, des **boxplots de consommation selon le type d’énergie**, afin de visualiser les différences de comportement entre les sources énergétiques (gaz, électricité, fioul, etc.).  
---

## 4. Modélisation

### 4.1 Tâches de Machine Learning
Deux tâches principales ont été mises en œuvre :  
- une **classification**, visant à prédire la classe de performance énergétique `etiquette_dpe` (de A à G) ;  
- une **régression**, destinée à estimer le **coût total des cinq usages énergétiques (`cout_total_5_usages`)**, exprimé en euros par an.  

Le jeu de données a été divisé en deux sous-ensembles : **80 % pour l’entraînement** des modèles et **20 % pour le test**, afin d’évaluer la capacité de généralisation des algorithmes.  

---
## 4.2 Modélisation

### 4.2.1 Modèle de classification

L’objectif de cette première tâche de modélisation était de **prédire la classe de performance énergétique (`etiquette_dpe`)** des logements, comprise entre A et G.  
Pour cela, un **Random Forest Classifier** a été implémenté à l’aide d’un pipeline intégrant à la fois le **prétraitement des données** et la **gestion du déséquilibre des classes**.

#### a) Construction du pipeline

Le pipeline utilisé comprend les étapes suivantes :
1. **Prétraitement (`preprocessor`)** : normalisation des variables numériques et encodage des variables catégorielles.
2. **Équilibrage des classes** avec la méthode **SMOTE (Synthetic Minority Over-sampling Technique)**, afin d’éviter que les classes minoritaires ne soient sous-représentées.
3. **Modélisation** avec un **RandomForestClassifier**, configuré avec un poids de classes équilibré (`class_weight='balanced'`) pour renforcer la robustesse du modèle.

#### b) Optimisation des hyperparamètres

Une recherche par **validation croisée (GridSearchCV, k=5)** a été menée sur les paramètres clés :
- `n_estimators` : [100, 300]  
- `max_depth` : [None, 10, 20]

#### c) Évaluation sur les données de test

Après entraînement, le modèle a été évalué sur l’échantillon de test (30 % des données) :

| Métrique | Score |
|-----------|--------|
| **Accuracy**  | 95.81 % |
| **Precision moyenne** | 0.96 |
| **Recall moyen**    | 0.96 |
| **F1-score moyen**  | 0.96 |

La **matrice de confusion** montre une **diagonale dominante**, ce qui indique que la plupart des prédictions sont correctes pour toutes les classes DPE, avec très peu de confusions entre classes voisines.

---

### 4.2.2 Modèle de régression

La seconde tâche visait à **estimer le coût total annuel des cinq usages énergétiques (`cout_total_5_usages`)**.  
Deux modèles ont été comparés :  
- une **régression linéaire**,  
- un **arbre de décision régressif (DecisionTreeRegressor)**.

#### a) Optimisation et évaluation

Pour le **DecisionTreeRegressor**, une recherche par grille a été réalisée sur les paramètres suivants :
- `max_depth` : [5, 10, 20, 30, 40, 50]  
- `min_samples_split` : [2, 5, 10, 15, 20]  
- `min_samples_leaf` : [1, 2, 4]

Les scores moyens en validation croisée (k=5) ont montré une nette supériorité du modèle d’arbre :

| Modèle | R² (CV) | MAE (€) | 
|---------|----------|---------|
| LinearRegression | 0.912 | 140.52 |
| DecisionTreeRegressor | 0.968 | 46.29 | 

Le **DecisionTreeRegressor** atteint un **R² = 0.969** sur l’échantillon de test, confirmant sa capacité à expliquer près de 97 % de la variance du coût énergétique.  

---

### 4.2.3 Synthèse des performances

| Tâche | Modèle | Score principal | Performance globale |
|-------|---------|-----------------|----------------------|
| Classification | RandomForestClassifier | Accuracy = 0.958 | Excellent équilibre précision/rappel |
| Régression | DecisionTreeRegressor | R² = 0.969 | Très bonne capacité explicative |

Les deux modèles présentent une **stabilité remarquable** (écart-type faible en validation croisée, ±0.001), démontrant la **robustesse** et la **fiabilité** des résultats obtenus.


### 4.5 Sauvegarde
Modèles exportés avec `joblib` :
```
models/classification_model.pkl
models/regression_model.pkl
metrics.json
```

---

## 5. Interprétation et discussion

### 5.1 Importance des variables  

L’analyse des importances de variables issues du modèle de classification met en évidence que les **consommations totales et spécifiques par mètre carré** constituent les **principaux facteurs explicatifs** de la performance énergétique (`etiquette_dpe`).  
En particulier, la variable `conso_5_usages_par_m2_ef` se distingue comme la plus déterminante, confirmant que la consommation d’énergie normalisée par la surface est un indicateur pertinent de l’efficacité énergétique d’un logement.  

Le **type d’énergie utilisée** (`type_energie_recodee`) et la **surface habitable du logement** (`surface_habitable_logement`) apparaissent également comme des variables influentes. Ces facteurs complètent la hiérarchie des déterminants de la consommation, en reflétant à la fois les **caractéristiques structurelles** du bâti et les **choix énergétiques** des occupants.  
Ainsi, la combinaison de variables techniques (surface, équipements) et comportementales (type d’énergie, usages) permet d’obtenir une compréhension globale du profil énergétique des logements étudiés.

---

### 5.2 Robustesse des modèles  

Les modèles développés montrent une **robustesse élevée**, confirmée par les performances obtenues en **validation croisée (k=5)**, avec des écarts-types très faibles (≈ ±0.001). Cette stabilité indique que les modèles **ne souffrent pas de surapprentissage**, grâce à une bonne diversité des échantillons d’entraînement et à une régularisation implicite efficace, notamment pour le modèle Random Forest.  

Cependant, il convient de souligner que la **capacité de généralisation géographique** n’a pas encore été testée. En effet, le jeu de données utilisé est restreint à la **région Rhône-Alpes**, ce qui peut limiter la transférabilité des modèles à d’autres contextes territoriaux (climat, typologie des bâtiments, comportements énergétiques).  
Des tests complémentaires sur d’autres régions ou périodes temporelles seraient nécessaires pour **valider la robustesse externe** du modèle et confirmer sa pertinence à plus grande échelle.  


---

## 6. Intégration applicative  

L’ensemble des modèles développés a été intégré dans une architecture applicative complète, combinant une interface utilisateur interactive, une API de service, et une infrastructure conteneurisée pour le déploiement. Cette intégration permet à la fois la **visualisation des données**, la **prédiction en temps réel**, et le **réentraînement automatisé des modèles**.

---

### 6.1 Interface Streamlit  

Une interface **Streamlit** a été conçue pour faciliter l’exploration et l’exploitation des résultats :  
- **Tableau de bord dynamique** : visualisation interactive des données et des indicateurs à l’aide de **graphiques Plotly**.  
- **Prédiction interactive** : l’utilisateur peut saisir les caractéristiques d’un logement et obtenir instantanément la **classe DPE prédite** ou le **coût énergétique estimé**.  
- **Réentraînement et mise à jour automatique** : un simple clic permet de lancer un **réentraînement du modèle** ou un **rafraîchissement des données** afin de maintenir l’outil à jour.  

Cette interface offre une expérience utilisateur fluide et permet de démocratiser l’accès aux résultats du modèle.

---

### 6.2 API FastAPI  

Une **API RESTful** a été développée avec **FastAPI** pour assurer la communication entre le front-end et les modèles de Machine Learning.  
Les principaux endpoints implémentés sont :  

- **`/predict`** : permet d’obtenir une prédiction individuelle à partir d’un jeu de caractéristiques en entrée.  
- **`/predict/batch`** : réalise des prédictions en masse à partir d’un fichier CSV.  
- **`/models/retrain`** : déclenche un **réentraînement automatique** du modèle à partir des nouvelles données disponibles.  
- **`/data/refresh`** : met à jour la base de données locale à partir des **sources ADEME** les plus récentes.  

Cette API garantit une **modularité élevée** et facilite l’intégration du modèle dans d’autres applications ou systèmes externes.

---

### 6.3 Dockerisation  

L’ensemble de l’application a été **dockerisé** pour assurer sa portabilité et simplifier son déploiement.  
Deux services principaux sont définis dans la configuration Docker :  
- **`streamlit`** : interface utilisateur (port **8501**)  
- **`api`** : service FastAPI pour les prédictions et le réentraînement (port **8000**)  

Des **volumes persistants** sont montés pour garantir la conservation des données et des modèles entre les redéploiements :  
- `data/` : jeux de données et mises à jour  
- `models/` : modèles entraînés et sauvegardés  
- `logs/` : journaux d’exécution et traces système  

Cette architecture conteneurisée rend la solution **reproductible, scalable et facilement déployable** sur tout environnement compatible Docker.


---

## 7. Conclusion  

Le projet **GreenTech Solutions** a permis de mettre en œuvre une démarche complète d’analyse et de modélisation autour des données énergétiques. Au-delà des résultats obtenus, il a constitué une expérience riche, combinant approche scientifique, réflexion environnementale et développement d’outils concrets.  

Ce travail a offert l’occasion de renforcer des compétences en traitement et interprétation de données, tout en découvrant les enjeux liés à la performance énergétique des bâtiments. Il a également mis en lumière l’importance d’une approche rigoureuse et structurée, depuis l’exploration des données jusqu’à la mise en place d’une solution opérationnelle accessible aux utilisateurs.  

Enfin, ce projet ouvre des perspectives intéressantes pour la suite : élargir l’analyse à d’autres régions, intégrer davantage de dimensions explicatives, et poursuivre le développement d’outils numériques favorisant la transition énergétique et la prise de décision éclairée.

---

## Annexes
- **Notebook 1 :** [Extraction et préparation des données](https://github.com/Modou010/m2_enedis/blob/main/Notebooks/1_extraction_prepartaion_donnees.ipynb)
- **Notebook 2 :** [Exploration et analyse](https://github.com/Modou010/m2_enedis/blob/main/Notebooks/2_exploration_donnees.ipynb)
- **Notebook 3 :** [Modélisation ML](https://github.com/Modou010/m2_enedis/blob/main/Notebooks/3_classification_regression.ipynb)
- **README complet :** [GreenTech Solutions](https://github.com/Modou010/m2_enedis/blob/main/Notebooks/readme.md)

---

**Auteurs :** Nico DENA, Modou MBOUP, Rina RAZAFIMAHEFA
**Date :** Novembre 2025
