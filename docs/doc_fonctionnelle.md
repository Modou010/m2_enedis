# Documentation fonctionnelle - GreenTech Solutions

Projet réalisé dans le cadre du Master 2 SISE - Statistique et Informatique pour la Science des Données  
Université Lyon 2 - Année universitaire 2025-2026  

Application web Streamlit de modélisation et de prédiction de la performance énergétique des logements en France à partir des données publiques ADEME DPE.

---

## Objectif du document

Ce document présente les aspects fonctionnels de l'application GreenTech Solutions : son objectif, son public cible, ses principales fonctionnalités, son organisation interne et son utilisation prévue.  
Il complète la documentation technique et le rapport ML en se concentrant sur la logique d'usage plutôt que sur les détails de mise en œuvre.

---

## Public visé

Cette documentation s'adresse à :
- l'équipe projet, pour assurer la cohérence fonctionnelle ;
- les enseignants et évaluateurs, pour comprendre les fonctionnalités proposées ;
- les utilisateurs finaux souhaitant explorer ou prédire la performance énergétique d'un logement.

---

## Navigation dans l'application

L'application comprend trois pages principales accessibles via la barre latérale de navigation Streamlit :

1. **Page Contexte** - Exploration et visualisation des données DPE.  
2. **Page Prédiction** - Saisie de caractéristiques d'un logement pour obtenir une prédiction de classe énergétique et de consommation.  
3. **Page Analyse / Export** - Consultation et téléchargement des graphiques et données générées.

---

## Fonctionnalités principales

### Page "Contexte"
- Affiche plusieurs visualisations interactives issues du jeu de données DPE.  
- Filtres disponibles : localisation (région, département), type de logement, année de construction, classe énergétique.  
- Objectif : comprendre la répartition et les tendances des performances énergétiques.

**Exemples de graphiques :**
- Histogramme des classes DPE par région.
- Carte des consommations moyennes.
- Boxplot surface vs consommation.

---

### Page "Prédiction"
- Permet à l'utilisateur de saisir les caractéristiques d'un logement (surface, année, chauffage, énergie principale, etc.).  
- Le modèle de classification prédit la **classe DPE (A-G)**.  
- Le modèle de régression estime la **consommation énergétique (kWh/m²/an)**.  
- Les résultats sont présentés sous forme de carte ou encadré coloré avec légende.

**Interactions utilisateur :**
- Formulaire dynamique (widgets Streamlit).
- Bouton "Lancer la prédiction".
- Message d'erreur clair en cas de saisie incorrecte.

---

### Page "Analyse et export"
- Possibilité d'exporter les graphiques affichés au format `.png`.  
- Possibilité d'exporter les tables au format `.csv`.  
- Sauvegarde automatique dans le dossier `/exports/` local.

**Boutons disponibles :**
- "Exporter le graphique (.png)"
- "Exporter les données (.csv)"

---

## Cas d'usage

| Cas | Description | Acteur principal | Résultat attendu |
|-----|--------------|------------------|------------------|
| CU1 | Visualiser les performances énergétiques d'une région | Utilisateur | Graphiques filtrés selon la région choisie |
| CU2 | Obtenir une prédiction DPE à partir des caractéristiques d'un logement | Utilisateur | Classe DPE et consommation estimée affichées |
| CU3 | Exporter les graphiques au format PNG | Utilisateur | Fichier PNG téléchargé ou sauvegardé localement |
| CU4 | Exporter les données filtrées au format CSV | Utilisateur | Fichier CSV contenant les données visibles |
| CU5 | Consulter les métriques de prédiction dans la documentation | Enseignant | Accès au rapport ML via le menu latéral ou le dépôt GitHub |

---

## Description technique simplifiée

- **Langage principal :** Python 3.11  
- **Framework web :** Streamlit  
- **Bibliothèques principales :** pandas, scikit-learn, matplotlib, shap, joblib  
- **Backend :** Chargement des modèles de classification et de régression depuis `/app/model/`  
- **Stockage :** Données d'entrée et de sortie locales (`/data/`, `/exports/`)  
- **Déploiement :** Render (hébergement gratuit de l'application Streamlit)  

---

## Lien vers l'application et les documents associés

- **Application en ligne :** (à insérer : URL Render publique)  
- **Dépôt GitHub :** [https://github.com/Modou010/m2_enedis](https://github.com/Modou010/m2_enedis)  
- **Documentation technique :** [`docs/doc_technique.md`](./doc_technique.md)  
- **Rapport ML :** [`docs/rapport_ml.md`](./rapport_ml.md)  
- **Matrice de traçabilité projet :** [`docs/trace_project.md`](./trace_project.md)

---

## Annexes - Captures d'écran

### Page Accueil
![capture_accueil](https://github.com/Modou010/m2_enedis/blob/Rina/docs/assets/img1.png)  
*(à insérer : capture d'écran illustrant les visualisations principales de la page Contexte)*

### Page Prédiction
![capture_prediction](assets/capture_prediction.png)  
*(à insérer : capture d'écran montrant le formulaire de saisie et la zone de résultat)*

### Page Analyse / Export
![capture_export](assets/capture_export.png)  
*(à insérer : capture d'écran avec les boutons d'exportation et un graphique sauvegardé)*

---

Auteurs : Modou, Nico, Rina  
Version : 1.0 - Novembre 2025
