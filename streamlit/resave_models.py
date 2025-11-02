import joblib
import os

print(" Conversion des modèles en cours...")

try:
    os.makedirs('models', exist_ok=True)

    # Classification
    print(" Chargement du modèle de classification...")
    model_classif = joblib.load('models/best_model_classification_RandomForest.pkl')
    print(" Sauvegarde du nouveau modèle de classification...")
    joblib.dump(model_classif, 'models/classification_model.pkl')
    print(" Classification OK")

    # Régression
    print(" Chargement du modèle de régression...")
    model_regress = joblib.load('models/best_model_regression_DecisionTreeRegressor.pkl')
    print(" Sauvegarde du nouveau modèle de régression...")
    joblib.dump(model_regress, 'models/regression_model.pkl')
    print(" Régression OK")

    print("\n CONVERSION RÉUSSIE !")

except Exception as e:
    print(f"\n ERREUR : {e}")
    import traceback
    traceback.print_exc()
