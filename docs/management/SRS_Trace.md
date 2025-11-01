# Matrice de traçabilité - Cahier des charges (Greentech Solutions)

Ce document relie chaque exigence du cahier des charges officiel à l'implémentation du projet.
Statut : ⛔ = non implémenté / 🚧 = en cours / ✅ = validé

---

## Pack Standard

| ID | Exigence | Description | Implémentation | Fichier / Section | Statut | Preuve |
|----|-----------|--------------|----------------|-------------------|---------|---------|
| STD-1 | Pages Streamlit | ≥ 3 pages distinctes (Contexte, Carte, Prédiction) | Multi-page Streamlit (`pages/`) | `app/pages/context.py`, `app/pages/map.py`, `app/pages/predict.py` | 🚧 | captures écran |
| STD-2 | Images & icônes | Usage d'images, logos et icônes cohérents | Dossier `assets/` Streamlit | `app/assets/*` | ✅ | affichage UI |
| STD-3 | Carte interactive | Visualisation géographique avec marqueurs et filtres | Plotly Express / Folium / Pydeck | `app/pages/map.py` | 🚧 | capture carte |
| STD-4 | Page Contexte | Présentation et exploration des données DPE | DataFrame + graphiques descriptifs | `app/pages/context.py` | ✅ | |
| STD-5 | Filtres dynamiques | Widgets de sélection (select, checkbox, slider, radio) | st.selectbox / st.slider / st.radio | `app/components/filters.py` | ✅ | |
| STD-6 | ≥4 types de graphes | histogrammes, barres, boxplots, scatter, pie, etc. | Plotly / Altair | `app/pages/context.py`, `app/pages/map.py` | ✅ | |
| STD-7 | Méthodologie Scrum | Planification et suivi sur Taiga.io | backlog & sprints | `taiga_export.csv` | ✅ | capture écran |

---

## Pack Intermédiaire

| ID | Exigence | Description | Implémentation | Fichier / Section | Statut | Preuve |
|----|-----------|--------------|----------------|-------------------|---------|---------|
| INT-1 | Export .png | Sauvegarde des graphiques au format image | Plotly `write_image()` / st.download_button | `app/components/exports.py` | 🚧 | |
| INT-2 | Export .csv | Export des données filtrées | st.download_button(csv) | `app/components/exports.py` | ✅ | |
| INT-3 | Page Prédiction | Estimation DPE (classification) + conso (régression) | Pipeline sklearn + Streamlit UI | `app/pages/predict.py` | 🚧 | |
| INT-4 | Déploiement web | Application hébergée sur Render / Heroku / Shiny | Render (Procfile + runtime.txt) | `Procfile`, `runtime.txt` | 🚧 | lien public |
| INT-5 | OpenData enrichissement | Ajout variable externe (température, météo...) | API Meteo-France / ADEME | `services/opendata.py` | 🚧 | code API |
| INT-6 | Documentation complète | Technique (≤2p), Fonctionnelle (≤2p), ML (4–6p) | Markdown dans `/docs` | `docs/*` | 🚧 | |

---

## 🟥 Pack Expert

| ID | Exigence | Description | Implémentation | Fichier / Section | Statut | Preuve |
|----|-----------|--------------|----------------|-------------------|---------|---------|
| EXP-1 | Actualisation via API | Rafraîchir les données DPE périodiquement | Script API Streamlit / Cron / Requests | `services/opendata.py` | ⛔ | |
| EXP-2 | Ré-entrainement modèle | UI pour lancer le réapprentissage | joblib + st.button("Réentraîner") | `app/pages/retrain.py` | ⛔ | |
| EXP-3 | Exposition API modèle | Endpoint REST (FastAPI / Flask) | Microservice séparé / API interne | `api/app.py` | ⛔ | |
| EXP-4 | Conteneurisation Docker | Dockerfile + build + push image | Dockerfile + CI/CD Render | `docker/Dockerfile` | 🚧 | |
| EXP-5 | Monitoring app | Logs, santé `/health`, suivi erreurs | logger + st.status / Render logs | `app/app.py` | ⛔ | |
| EXP-6 | Accessibilité & UX | Contraste AA, focus, tailles ≥16px | CSS custom Streamlit | `.streamlit/config.toml`, `app/styles/theme.css` | ✅ | |

---

## Documentation & livrables

| ID | Exigence | Description | Fichier | Statut | Preuve |
|----|-----------|--------------|----------|---------|---------|
| DOC-1 | README principal | Informations complètes, structure claire | `README.md` | ✅ | |
| DOC-2 | Documentation technique | ≤2 pages, archi + installation + packages | `docs/doc_technique.md` | 🚧 | |
| DOC-3 | Documentation fonctionnelle | ≤2 pages, description des pages & interactions | `docs/doc_fonctionnelle.md` | 🚧 | |
| DOC-4 | Rapport ML | 4–6 pages, métriques & interprétation | `docs/rapport_ml.md` | 🚧 | |
| DOC-5 | Schéma d'architecture | Draw.io export en PNG | `docs/assets/architecture.png` | 🚧 | |
| DOC-6 | README clair dans /docs | Vue d'ensemble | `docs/README.md` | ✅ | |

---

## Vérification finale

- [ ] Tous les liens Render fonctionnels  
- [ ] Dataset final (`data/processed/`) versionné  
- [ ] Tests de démarrage (`tests/smoke_test.py`) réussis  
- [ ] Environnements reproductibles (`requirements.txt`, `runtime.txt`)  
- [ ] README complet et validé par l'équipe

---

> **Dernière mise à jour** : 01/11/2025  
> **Responsable QA** : Rina