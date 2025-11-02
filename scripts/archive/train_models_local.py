#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script d'entraînement des modèles ML pour GreenTech Solutions
- Classification (ADEME)
- Régression (Enedis)
Exécution :
python scripts/train_models_local.py --ademe_path data/donnees_ademe_finales_nettoyees_69_final_pret.csv --enedis_path data/donnees_enedis_finales_69.csv [--sample 10000]
"""

import argparse
import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(description="Entraîne les modèles classification et régression GreenTech Solutions")
    parser.add_argument("--ademe_path", required=True, help="Chemin vers le fichier ADEME (classification)")
    parser.add_argument("--enedis_path", required=True, help="Chemin vers le fichier Enedis (régression)")
    parser.add_argument("--sample", type=int, default=None, help="Taille d'échantillon (optionnelle)")
    args = parser.parse_args()

    # Création des dossiers
    os.makedirs("streamlit/model", exist_ok=True)
    os.makedirs("docs/assets", exist_ok=True)
    os.makedirs("docs", exist_ok=True)

    print("=== Étape 1 : Chargement des données ADEME ===")
    df_ademe = pd.read_csv(args.ademe_path, low_memory=False)
    if args.sample:
        df_ademe = df_ademe.sample(n=min(args.sample, len(df_ademe)), random_state=42)
    print(f"✓ Données ADEME chargées : {df_ademe.shape[0]} lignes, {df_ademe.shape[1]} colonnes")

    print("=== Étape 2 : Chargement des données Enedis ===")
    df_enedis = pd.read_csv(args.enedis_path, low_memory=False)
    if args.sample:
        df_enedis = df_enedis.sample(n=min(args.sample, len(df_enedis)), random_state=42)
    print(f"✓ Données Enedis chargées : {df_enedis.shape[0]} lignes, {df_enedis.shape[1]} colonnes")

    # === Classification ===
    print("\n=== Étape 3 : Préparation des données pour la classification ===")
    target_class = "etiquette_dpe"
    df_ademe = df_ademe.dropna(subset=[target_class])
    X_class = df_ademe.drop(columns=[target_class])
    y_class = df_ademe[target_class]

    num_cols = X_class.select_dtypes(include=np.number).columns.tolist()
    cat_cols = X_class.select_dtypes(exclude=np.number).columns.tolist()

    preprocessor_class = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ]
    )

    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

    clf = Pipeline(steps=[
        ("preprocessor", preprocessor_class),
        ("model", RandomForestClassifier(random_state=42, n_estimators=200))
    ])

    print("=== Étape 4 : Entraînement du modèle de classification ===")
    clf.fit(X_train_c, y_train_c)

    y_pred_c = clf.predict(X_test_c)
    acc = accuracy_score(y_test_c, y_pred_c)
    f1 = f1_score(y_test_c, y_pred_c, average="weighted")

    print(f"Accuracy : {acc:.3f}")
    print(f"F1-score : {f1:.3f}")

    cm = confusion_matrix(y_test_c, y_pred_c, labels=np.unique(y_test_c))
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=np.unique(y_test_c), yticklabels=np.unique(y_test_c))
    plt.xlabel("Prédit")
    plt.ylabel("Réel")
    plt.title("Matrice de confusion - Classification DPE")
    plt.tight_layout()
    plt.savefig("docs/assets/confusion_matrix.png")
    plt.close()

    joblib.dump(clf, "streamlit/model/classification_model.pkl")
    print("✓ Modèle de classification sauvegardé dans streamlit/model/classification_model.pkl")

    # === Régression ===
    print("\n=== Étape 5 : Préparation des données pour la régression ===")
    target_reg = "Consommation annuelle moyenne par logement de l'adresse (MWh)"
    df_enedis = df_enedis.dropna(subset=[target_reg])
    X_reg = df_enedis.drop(columns=[target_reg])
    y_reg = df_enedis[target_reg]

    num_cols_r = X_reg.select_dtypes(include=np.number).columns.tolist()
    cat_cols_r = X_reg.select_dtypes(exclude=np.number).columns.tolist()

    preprocessor_reg = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols_r),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols_r)
        ]
    )

    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

    reg = Pipeline(steps=[
        ("preprocessor", preprocessor_reg),
        ("model", RandomForestRegressor(random_state=42, n_estimators=200))
    ])

    print("=== Étape 6 : Entraînement du modèle de régression ===")
    reg.fit(X_train_r, y_train_r)

    y_pred_r = reg.predict(X_test_r)
    rmse = mean_squared_error(y_test_r, y_pred_r, squared=False)
    mae = mean_absolute_error(y_test_r, y_pred_r)
    r2 = r2_score(y_test_r, y_pred_r)

    print(f"RMSE : {rmse:.3f}")
    print(f"MAE : {mae:.3f}")
    print(f"R² : {r2:.3f}")

    plt.figure(figsize=(6, 6))
    plt.scatter(y_test_r, y_pred_r, alpha=0.6)
    plt.plot([y_test_r.min(), y_test_r.max()], [y_test_r.min(), y_test_r.max()], "r--")
    plt.xlabel("Valeurs réelles")
    plt.ylabel("Valeurs prédites")
    plt.title("Régression - Valeurs réelles vs prédites")
    plt.tight_layout()
    plt.savefig("docs/assets/regression_plot.png")
    plt.close()

    joblib.dump(reg, "streamlit/model/regression_model.pkl")
    print("✓ Modèle de régression sauvegardé dans streamlit/model/regression_model.pkl")

    # Résumé
    duration = time.time() - start_time
    minutes, seconds = divmod(duration, 60)

    summary_path = Path("docs/results_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("Résultats d'entraînement - GreenTech Solutions\n")
        f.write(f"Durée totale : {minutes:.0f} min {seconds:.1f} s\n\n")
        f.write("=== Classification (ADEME) ===\n")
        f.write(f"Accuracy : {acc:.3f}\n")
        f.write(f"F1-score : {f1:.3f}\n")
        f.write("Modèle : RandomForestClassifier\n\n")
        f.write("=== Régression (Enedis) ===\n")
        f.write(f"RMSE : {rmse:.3f}\n")
        f.write(f"MAE : {mae:.3f}\n")
        f.write(f"R² : {r2:.3f}\n")
        f.write("Modèle : RandomForestRegressor\n")

    print("\n=== Entraînement terminé ===")
    print(f"Durée totale : {minutes:.0f} min {seconds:.1f} s")
    print("Résultats enregistrés dans docs/results_summary.txt")

if __name__ == "__main__":
    main()
