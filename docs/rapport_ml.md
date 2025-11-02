# Rapport Machine Learning - GreenTech Solutions

Projet réalisé dans le cadre du Master 2 SISE - Statistique et Informatique pour la Science des Données  
Université Lyon 2 - Année universitaire 2025-2026  

---

## 1. Objectif

Construire et comparer deux modèles supervisés :
- **Classification** : prédiction de l'étiquette énergétique (A-G) des logements.
- **Régression** : estimation de la consommation énergétique (kWh/m²/an).

Les données utilisées proviennent des jeux ADEME (Diagnostics de Performance Énergétique) et Enedis (consommations réelles) pour le département du Rhône (69).

---

## 2. Données et préparation

### 2.1 Sources
- **ADEME** : `donnees_ademe_finales_nettoyees_69_final_pret.csv`
- **Enedis** : `donnees_enedis_finales_69.csv`

### 2.2 Nettoyage et intégration
- Suppression des doublons et des valeurs aberrantes.
- Harmonisation des codes postaux et types d'énergie.
- Fusion sur le champ `code_postal` lorsque nécessaire.
- Séparation train/test : 80 % / 20 %.

### 2.3 Variables utilisées
| Type | Variables principales |
|------|-----------------------|
| Numériques | conso_auxiliaires_ef, cout_eclairage, conso_5_usages_par_m2_ef, surface_habitable_logement, cout_ecs |
| Catégorielles | type_batiment, type_energie_recodee |
| Cible classification | etiquette_dpe |
| Cible régression | conso_5_usages_par_m2_ef |

---

## 3. Méthodologie

1. Prétraitement des données : encodage des variables catégorielles, normalisation des numériques.  
2. Entraînement et évaluation de plusieurs algorithmes :
   - **Classification** : Régression Logistique (baseline), Random Forest.
   - **Régression** : Régression Linéaire (baseline), Random Forest Regressor.
3. Sélection du modèle final selon les métriques :
   - Classification : Accuracy, F1-macro, AUC-ROC.
   - Régression : R², RMSE, MAE.
4. Sauvegarde des modèles finaux au format `.pkl` :
   - `classification_randomforest_full.pkl`
   - `regression_randomforest_full.pkl`

---

## 4. Résultats

### 4.1 Classification (étiquette DPE)

| Modèle | Accuracy | F1-macro | AUC-ROC | Commentaire |
|---------|-----------|----------|----------|--------------|
| Régression Logistique | _à compléter_ | _à compléter_ | _à compléter_ | Baseline simple |
| Random Forest | **0.945** | **0.922** | _à compléter_ | Très bonne généralisation |

**Analyse**  
La Random Forest surperforme largement la baseline. La stabilité est élevée et les erreurs sont concentrées sur les frontières entre classes voisines (C/D et E/F). Les variables les plus influentes sont la **surface**, la **consommation totale** et le **type d'énergie**.

---

### 4.2 Régression (consommation énergétique)

| Modèle | R² | RMSE | MAE | Commentaire |
|---------|----|------|-----|-------------|
| Régression Linéaire | _à compléter_ | _à compléter_ | _à compléter_ | Baseline |
| Random Forest Regressor | _à compléter_ | _à compléter_ | _à compléter_ | Modèle final |

**Analyse**  
_Les performances finales seront ajoutées dès la fin de l'entraînement._  
_Si le modèle complet est trop long à exécuter, une version “light” sur échantillon (5 000 lignes) est utilisée pour l'intégration Streamlit._

---

## 5. Interprétation

- **Importance des variables** (SHAP ou feature_importances_) :  
  Les variables relatives à la consommation par usage et au type d'énergie sont prédominantes.  
- **Corrélation** : les consommations par m² et totales présentent une forte redondance, justifiant d'éventuelles réductions dimensionnelles ultérieures.

---

## 6. Limites et perspectives

- Optimisation possible des hyperparamètres (GridSearchCV).  
- Ajout d'un pipeline d'automatisation (retrain / refresh).  
- Intégration de la régression dans l'interface Streamlit pour un retour utilisateur instantané.  
- Exploration d'algorithmes alternatifs : Gradient Boosting, XGBoost, CatBoost.  

---

## 7. Sauvegardes et intégration

| Élément | Fichier | Emplacement |
|----------|----------|--------------|
| Modèle classification | `classification_randomforest_full.pkl` | `streamlit/models/` |
| Modèle régression | `regression_randomforest_full.pkl` | `streamlit/models/` |
| Log complet | `docs/results_full.txt` | — |
| Script d'entraînement | `train_models_full.py` | racine du projet |

---

## 8. Références

- Données publiques ADEME & Enedis  
- Documentation scikit-learn (2025)  
- Cours M2 SISE - [Python Machine Learning](https://github.com/asardell/M2-SISE)  

---

**Auteurs :** Modou Mboup, Nico Dena, Rina Razafimahefa  
**Version :** 1.0 - Novembre 2025
