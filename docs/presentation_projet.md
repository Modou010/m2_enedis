# Présentation du projet *GreenTech Solutions*

## Introduction  
Le projet **GreenTech Solutions** s'inscrit dans une démarche de modélisation et de visualisation des performances énergétiques des logements à partir des **Diagnostics de Performance Énergétique (DPE)**.  
Dans un contexte de transition écologique et de hausse du coût de l'énergie, comprendre et anticiper les consommations des bâtiments constitue un enjeu majeur pour les politiques publiques, les acteurs du bâtiment et les particuliers.  

Ce projet a été réalisé dans le cadre du **Master 2 SISE – Statistique et Informatique pour la Science des donnéEs** (Université Lyon 2, année universitaire 2025-2026).  
L'objectif est de construire un pipeline complet — de la collecte à la visualisation — sur un périmètre restreint mais représentatif : **le département du Rhône**, choisi pour son volume de données, sa diversité de logements et sa pertinence géographique pour les étudiants du master.

---

## Données et périmètre  
Les données utilisées proviennent du portail **ADEME Data**, sections **DPE Logements existants** et **DPE Logements neufs** pour le **département du Rhône**.  
Chaque enregistrement contient des informations telles que la consommation énergétique annuelle, les émissions de gaz à effet de serre, la surface habitable, le type de chauffage et la classe énergétique (A à G).  

Les principales étapes de **préparation et d'harmonisation** ont inclus :  
- le filtrage des données par **région et département**,  
- la gestion des valeurs manquantes et des doublons,  
- la **conversion des formats** (dates, unités, typage),  
- et la consolidation en fichiers **Parquet** prêts à l'usage analytique.  

Le jeu de données final offre une vision détaillée du parc immobilier rhodanien, permettant d'expérimenter des approches de modélisation réalistes et transposables à d'autres territoires.

---

## Méthodologie et pipeline de travail  
Le pipeline s'appuie sur les étapes classiques du **cycle de la donnée** :  
1. **Extraction et préparation** des données ADEME du Rhône ;  
2. **Analyse exploratoire** (corrélations, distributions, cartographies) ;  
3. **Construction de features** pertinentes pour la prédiction de la classe DPE ;  
4. **Modélisation** (régression, arbres de décision, forêts aléatoires) ;  
5. **Évaluation** (validation croisée, métriques adaptées) ;  
6. **Préparation au déploiement** (app Streamlit, conteneurisation, automatisation).  

La pipeline technique est aujourd'hui **quasi complète**, mais certaines briques sont encore en phase d'esquisse ou de simulation :  
- le **déploiement effectif de l'application Streamlit** reste à finaliser ;  
- la **dockerisation** est en préparation ;  
- un **scénario de réentraînement automatique** est prévu sous forme de **simulation conceptuelle**, illustrant comment le système pourrait se mettre à jour lorsque de nouvelles données ADEME seraient disponibles.

Ces choix permettent de conserver une cohérence d'ensemble et de présenter un projet **réaliste et extensible**, même si certaines composantes restent théoriques pour l'instant.

---

## Gestion de projet et approche inclusive  
Le pilotage du projet a combiné **méthodes agiles** et **principes d'inclusion**.  
L'équipe a utilisé **Taiga**, un outil open-source de gestion agile, pour organiser le travail en sprints, suivre les tâches, et répartir les responsabilités de manière transparente.  
Les versions du code et la collaboration technique ont été assurées via **GitHub**, garantissant la traçabilité et la synchronisation du travail à distance.

La dynamique de groupe a été pensée pour permettre la participation effective d'une **personne porteuse de handicap**, en adoptant une **organisation inclusive** :  
- échanges principalement **écrits et asynchrones**,  
- réunions régulières mais flexibles selon les disponibilités,  
- documentation systématique des décisions et des progrès,  
- adaptation du rythme et des tâches aux contraintes individuelles.

Cette méthodologie a renforcé la **cohésion** et la **qualité documentaire** du projet, tout en montrant que l'accessibilité peut être un levier d'efficacité collective.

---

## Résultats et analyses  
Les analyses réalisées sur le département du Rhône ont permis d'identifier plusieurs tendances :  
- les logements anciens présentent une efficacité énergétique nettement moindre que les constructions postérieures à 2010 ;  
- les zones périurbaines tendent à concentrer les étiquettes les plus défavorables, en lien avec le type d'habitat individuel et les modes de chauffage ;  
- les variables les plus influentes dans la classification DPE incluent la surface, la période de construction et la nature du chauffage.

Les modèles développés (forêts aléatoires, gradient boosting) ont montré des performances satisfaisantes, avec un équilibre entre **précision et interprétabilité**.  
Ces résultats constituent une **base solide pour une extension nationale**, qui fait partie des perspectives du projet.

---

## L'application Streamlit  
Une **application interactive Streamlit** a été développée pour rendre les résultats accessibles à un public non technique.  
Elle permet notamment :  
- d'explorer les données du Rhône à travers des graphiques et cartes dynamiques ;  
- de visualiser les performances du modèle sur les classes DPE ;  
- de simuler la classe énergétique d'un logement à partir de paramètres saisis par l'utilisateur.  

Le design de l'application est sobre et fonctionnel.  
L'architecture repose sur un **backend Python** intégrant les modèles entraînés (fichiers `.pkl`) et un **frontend Streamlit** assurant les interactions.  
Le déploiement en ligne et la dockerisation sont en cours, mais des **captures de simulation** seront intégrées dans le rapport pour illustrer les fonctionnalités prévues.

---

## Éléments visuels et suivi du projet  
La présentation écrite sera accompagnée de plusieurs **captures d'écran commentées** :  

### 🔸 Suivi de projet  
![capture_taiga](docs/assets/exemple_taiga.png)  
> *Exemple de tableau de bord Taiga : user stories, tâches, et progression.*  

### 🔸 Collaboration technique  
![capture_github](docs/assets/sshot_github.png)  
> *Structure du dépôt GitHub et historique des commits.*  

### 🔸 Interface Streamlit  
![capture_streamlit](path/to/app_streamlit.png)  
> *Aperçu de la page principale de l'application Streamlit (carte et graphique).*  

### 🔸 Pipeline Python  
![capture_pipeline](path/to/pipeline_diagram.png)  
> *Schéma global du pipeline : ETL, features, training, déploiement.*  

Ces illustrations permettront de montrer concrètement le **niveau d'avancement**, la **méthodologie collaborative** et la **rigueur technique** du projet.

---

## Conclusion et perspectives  
Le projet *GreenTech Solutions* démontre la faisabilité d'un pipeline de data science complet appliqué aux **performances énergétiques** des logements, même à l'échelle départementale.  
Malgré certaines briques encore simulées (déploiement, dockerisation, automatisation du réentraînement), le projet offre une base robuste, reproductible et bien documentée.  

Les perspectives incluent :  
- l'**extension du modèle à l'échelle nationale**,  
- l'intégration de données **météorologiques et socio-économiques**,  
- la **mise en production réelle** de l'application Streamlit,  
- et la **mise en place d'un scénario automatisé de mise à jour des modèles**.

L'approche inclusive, la gestion agile et la rigueur scientifique ont permis de transformer un projet académique en un véritable prototype fonctionnel, ouvrant la voie à des développements plus ambitieux.
