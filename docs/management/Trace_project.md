## Annexe - Matrice de traçabilité projet (Epics → US → Livrables → Fichiers)

Cette matrice relie chaque **Epic** du backlog Taiga à ses **User Stories (US)**, livrables attendus et fichiers du dépôt correspondants.

| Épopée | User Story | Livrable attendu | Fichier(s) concerné(s) | Statut |
|---------|-------------|------------------|------------------------|--------|
| E01 - Données & Nettoyage | US 1.1 - Extraction DPE | Données ADEME consolidées | `src/etl.py`, `data/raw/`, `data/processed/` | ✅ |
|  | US 1.2 - Nettoyage & typage | Dataset propre + log nettoyage | `src/etl.py`, `src/features.py` | ✅ |
|  | US 1.3 - Sélection variables | Liste features retenues | `src/features.py` | ✅ |
| E02 - Modélisation ML | US 2.1 - Classification DPE | `classification_model.pkl` + métriques | `src/train.py`, `app/model/classification_model.pkl` | ✅ |
|  | US 2.2 - Régression conso | `regression_model.pkl` + métriques | `src/train.py`, `app/model/regression_model.pkl` | ✅ |
|  | US 2.3 - Interprétation ML | Figures + `rapport_ml.md` | `src/evaluate.py`, `docs/rapport_ml.md` | 🚧 |
| E03 - Interface utilisateur | US 3.1 - Page Contexte | Page Streamlit interactive | `app/pages/context.py` | ✅ |
|  | US 3.2 - Page Prédiction | Formulaire + affichage résultats | `app/pages/predict.py` | ✅ |
|  | US 3.3 - Export données/graphes | Boutons `st.download_button` | `app/components/exports.py` | 🚧 |
| E04 - Déploiement & API | US 4.1 - Déploiement Render | App en ligne + URL publique | `Procfile`, `runtime.txt`, Render dashboard | 🚧 |
|  | US 4.2 - API Predict | Endpoint `/predict` | `app/app.py` (fonction `predict()`) | 🚧 |
|  | US 4.3 - Healthcheck | Endpoint `/health` | `app/app.py` | ✅ |
|  | US 4.4 - Docker | Image locale fonctionnelle | `docker/Dockerfile` | 🚧 |
| E05 - Documentation & Vidéo | US 5.1 - Doc technique | `docs/doc_technique.md` complet | `docs/doc_technique.md` | 🚧 |
|  | US 5.2 - Doc fonctionnelle | Pages + filtres + exports | `docs/doc_fonctionnelle.md` | 🚧 |
|  | US 5.3 - Rapport ML | Résultats & interprétation | `docs/rapport_ml.md` | 🚧 |
|  | US 5.4 - Vidéo démo | Lien YouTube privé | `README.md` (section "Demo") | ⛔ |
| E06 - Gestion de projet | US 6.1 - Rôles | `docs/roles.md` + Taiga assignations | `docs/roles.md` | ✅ |
|  | US 6.2 - Sprints & burndown | Capture burndown / Kanban | `docs/assets/burndown.png` | 🚧 |
|  | US 6.3 - Rétrospective | Section "Leçons apprises" | `docs/doc_technique.md` | 🚧 |
|  | US 6.4 - Check final | README + rendu GitHub | `README.md`, `Render URL` | ✅ |

> 🔹 Légende : ✅ Réalisé | 🚧 En cours | ⛔ Non implémenté