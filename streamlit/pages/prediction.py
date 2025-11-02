
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
import plotly.graph_objects as go
import plotly.express as px
from io import BytesIO
import os

@st.cache_resource
def load_models():
    import joblib, os
    if not os.path.exists("models/classification_model.pkl") or not os.path.exists("models/regression_model.pkl"):
        return None, None

    try:
        model_classification = joblib.load("models/classification_model.pkl")
        model_regression = joblib.load("models/regression_model.pkl")
        return model_classification, model_regression
    except Exception as e:
        return None, None

@st.cache_resource
def prepare_input_data(data_dict, encode=True):
    """Préparer les données d'entrée pour la prédiction"""
    df = pd.DataFrame([data_dict])
    
    if encode:
        # Encoder les variables catégorielles (même encodage que lors de l'entraînement)
        type_batiment_map = {'maison': 0, 'appartement': 1, 'immeuble': 2}
        energie_map = {
            'Electricite': 0,
            'Gaz_naturel': 1,
            'Fioul domestique': 2,
            'Reseau_de_chauffage_urbain': 3,
            'Autres': 4
        }
        
        # Vérifier si les valeurs existent dans les maps
        if df['type_batiment'].iloc[0] not in type_batiment_map:
            st.warning(f" Type de bâtiment '{df['type_batiment'].iloc[0]}' non reconnu")
        if df['type_energie_recodee'].iloc[0] not in energie_map:
            st.warning(f" Type d'énergie '{df['type_energie_recodee'].iloc[0]}' non reconnu")
        
        df['type_batiment'] = df['type_batiment'].map(type_batiment_map)
        df['type_energie_recodee'] = df['type_energie_recodee'].map(energie_map)
    
    return df

def show():
    st.title(" Prédiction de Performance Énergétique")
    st.markdown("### Estimez l'étiquette DPE et le coût énergétique d'un logement")
    
    # Charger les modèles
    model_classif, model_regress = load_models()
    
    if model_classif is None or model_regress is None:
        st.info(" Placez vos modèles dans le dossier `models/` avec les noms :\n- `classification_model.pkl`\n- `regression_model.pkl`")
        return
    
    # Onglets pour les deux modes
    tab1, tab2 = st.tabs([" Prédiction individuelle", " Prédiction par lot (CSV)"])
    st.markdown("""
<style>
/* Conteneur global des tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

/* Style général des onglets */
.stTabs [data-baseweb="tab"] {
    background-color: #e8f5e9;   /* vert clair */
    color: #1b5e20;              /* texte vert foncé */
    border-radius: 6px 6px 0 0;
    padding: 8px 16px;
    font-weight: 500;
    font-size: 15px;
    border: none !important;
    transition: all 0.3s ease;
    border-bottom: 3px solid transparent !important;
}

/* Onglet actif — même couleur que la navbar */
.stTabs [aria-selected="true"] {
    background-color: #1b5e20 !important;  /* vert foncé */
    color: white !important;
    font-weight: 600;
    border: none !important;
    border-bottom: 3px solid #1b5e20 !important;
}

/* Hover — reste vert, pas d'orange */
.stTabs [data-baseweb="tab"]:hover {
    background-color: #2e7d32 !important;  /* vert moyen */
    color: white !important;
    border-bottom: 3px solid #e8f5e9 !important;
}
</style>
""", unsafe_allow_html=True)
    
    # TAB 1 : Prédiction individuelle
    with tab1:
        st.markdown("#### Saisissez les caractéristiques du logement")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Caractéristiques du bâtiment")
            
            type_batiment = st.selectbox(
                "Type de bâtiment (type_batiment)",
                options=['maison', 'appartement', 'immeuble'],
                help="Sélectionnez le type de construction du logement"
            )
            
            surface_habitable = st.number_input(
                "Surface habitable en m² (surface_habitable_logement)",
                min_value=10.0,
                max_value=500000.0,
                value=100.0,
                step=5.0,
                help="Surface totale habitable du logement en mètres carrés"
            )
            
            type_energie = st.selectbox(
                "Source d'énergie principale (type_energie_recodee)",
                options=['Electricite', 'Gaz_naturel', 'Fioul domestique', 
                        'Reseau_de_chauffage_urbain', 'Autres'],
                help="Énergie utilisée pour le chauffage et l'eau chaude"
            )
        
        with col2:
            st.markdown("##### Consommations énergétiques")
            
            conso_5_usages_par_m2 = st.number_input(
                "Consommation annuelle par m² (conso_5_usages_par_m2_ef)",
                min_value=0.0,
                max_value=500000.0,
                value=200.0,
                step=10.0,
                help="Consommation énergétique par m² pour chauffage, eau chaude, refroidissement, éclairage et auxiliaires (kWh/m²/an)"
            )
            
            conso_ecs = st.number_input(
                "Eau chaude sanitaire (conso_ecs_ef)",
                min_value=0.0,
                max_value=500000.0,
                value=2000.0,
                step=100.0,
                help="Consommation annuelle pour l'eau chaude (douches, bains, cuisine) en kWh/an"
            )
            
            conso_auxiliaires = st.number_input(
                "Ventilation et pompes (conso_auxiliaires_ef)",
                min_value=0.0,
                max_value=500000.0,
                value=500.0,
                step=50.0,
                help="Consommation des équipements auxiliaires (VMC, circulateurs, etc.) en kWh/an"
            )
            
            conso_refroidissement = st.number_input(
                "Climatisation (conso_refroidissement_ef)",
                min_value=0.0,
                max_value=500000.0,
                value=0.0,
                step=50.0,
                help="Consommation pour la climatisation/refroidissement en kWh/an (0 si pas de clim)"
            )
        
        st.markdown("##### Coûts énergétiques")
        col1, col2 = st.columns(2)
        
        with col1:
            cout_ecs = st.number_input(
                "Coût annuel eau chaude (cout_ecs)",
                min_value=0.0,
                max_value=500000.0,
                value=300.0,
                step=10.0,
                help="Coût annuel pour l'eau chaude sanitaire en €/an"
            )
            
        
        with col2:
            cout_eclairage = st.number_input(
                "Coût annuel éclairage (cout_eclairage)",
                min_value=0.0,
                max_value=500000.0,
                value=80.0,
                step=5.0,
                help="Coût annuel pour l'éclairage en €/an"
            )
            
        
        # Calculer automatiquement certaines valeurs
        conso_5_usages_ef = conso_5_usages_par_m2 * surface_habitable
        
        st.info(f" Consommation totale estimée : **{conso_5_usages_ef:,.0f} kWh/an**")
        
        # Bouton de prédiction
        if st.button(" Lancer la prédiction", type="primary", use_container_width=True):
            with st.spinner("Analyse en cours..."):
                # Préparer les données
                input_data = {
                    'conso_auxiliaires_ef': conso_auxiliaires,
                    'cout_eclairage': cout_eclairage,
                    'conso_5_usages_par_m2_ef': conso_5_usages_par_m2,
                    'conso_5_usages_ef': conso_5_usages_ef,
                    'surface_habitable_logement': surface_habitable,
                    'cout_ecs': cout_ecs,
                    'type_batiment': type_batiment,
                    'conso_ecs_ef': conso_ecs,
                    'conso_refroidissement_ef': conso_refroidissement,
                    'type_energie_recodee': type_energie
                }
                
                df_input = prepare_input_data(input_data)
                
                # Prédictions
                try:
                    # Classification (étiquette DPE)
                    etiquette_pred = model_classif.predict(df_input)[0]
                    
                    # Probabilités si disponible
                    if hasattr(model_classif, 'predict_proba'):
                        probas = model_classif.predict_proba(df_input)[0]
                        classes = model_classif.classes_
                    else:
                        probas = None
                    
                    # Régression (coût total)
                    cout_pred = model_regress.predict(df_input)[0]
                    
                    # Afficher les résultats
                    st.markdown("---")
                    st.balloons()
                    st.markdown("### Résultats de la prédiction")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Couleur selon l'étiquette
                        colors_dpe = {
                            'A': '#00A550', 'B': '#52B153', 'C': '#C3D545',
                            'D': '#FFF033', 'E': '#F39200', 'F': '#ED2124', 'G': '#CC0033'
                        }
                        color = colors_dpe.get(etiquette_pred, '#666')
                        
                        st.markdown(f"""
                        <div style="background: white; padding: 2rem; border-radius: 15px; 
                                    border-left: 8px solid {color}; text-align: center;
                                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <h3 style="color: {color}; margin: 0;">Étiquette DPE prédite</h3>
                            <h1 style="font-size: 72px; margin: 1rem 0; color: {color};">{etiquette_pred}</h1>
                            <p style="color: #666; margin: 0;">Classification énergétique</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style="background: white; padding: 2rem; border-radius: 15px; 
                                    border-left: 8px solid #2E7D32; text-align: center;
                                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <h3 style="color: #2E7D32; margin: 0;">Coût annuel prédit</h3>
                            <h1 style="font-size: 48px; margin: 1rem 0; color: #2E7D32;">{cout_pred:,.0f} €</h1>
                            <p style="color: #666; margin: 0;">Coût total des 5 usages</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Distribution des probabilités
                    if probas is not None:
                        st.markdown("---")
                        st.markdown("#### Distribution des probabilités")
                        
                        fig_proba = go.Figure(data=[
                            go.Bar(
                                x=classes,
                                y=probas * 100,
                                marker_color=[colors_dpe.get(c, '#666') for c in classes],
                                text=[f"{p*100:.1f}%" for p in probas],
                                textposition='outside'
                            )
                        ])
                        
                        fig_proba.update_layout(
                            xaxis_title="Étiquette DPE",
                            yaxis_title="Probabilité (%)",
                            height=350,
                            showlegend=False
                        )
                        
                        st.plotly_chart(fig_proba, use_container_width=True)
                    
                    
                    # Estimation économies potentielles
                    if etiquette_pred in ['E', 'F', 'G']:
                        economie_potentielle = cout_pred * 0.4  # 40% d'économie possible
                        st.info(f" Économies potentielles après rénovation : **{economie_potentielle:,.0f} €/an**")
                
                except Exception as e:
                    st.error(f" Erreur lors de la prédiction : {e}")
                    import traceback
                    st.code(traceback.format_exc())
    
    # TAB 2 : Prédiction par lot
    with tab2:
        st.markdown("#### Uploader un fichier CSV pour prédictions multiples")
        
        # Template téléchargeable
        st.markdown("##### Format du fichier requis")
        
        template_data = {
            'conso_auxiliaires_ef': [500],
            'cout_eclairage': [80],
            'conso_5_usages_par_m2_ef': [200],
            'conso_5_usages_ef': [20000],
            'surface_habitable_logement': [100],
            'cout_ecs': [300],
            'type_batiment': ['maison'],
            'conso_ecs_ef': [2000],
            'conso_refroidissement_ef': [0],
            'type_energie_recodee': ['Electricite']
        }
        
        template_df = pd.DataFrame(template_data)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.dataframe(template_df, use_container_width=True)
        with col2:
            csv_template = template_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=" Télécharger template",
                data=csv_template,
                file_name="template_prediction.csv",
                mime="text/csv"
            )
        
        st.markdown("---")
        
        # Upload du fichier
        uploaded_file = st.file_uploader(
            "Choisir un fichier CSV",
            type=['csv'],
            help="Le fichier doit contenir toutes les colonnes du template"
        )
        
        if uploaded_file is not None:
            try:
                df_batch = pd.read_csv(uploaded_file)
                
                st.success(f" Fichier chargé : {len(df_batch)} lignes")
                st.dataframe(df_batch.head(), use_container_width=True)
                
                if st.button(" Lancer les prédictions", type="primary"):
                    with st.spinner(f"Prédiction en cours pour {len(df_batch)} logements..."):
                        # Préparer les données
                        df_prepared = df_batch.copy()
                        
                        # Encoder les variables catégorielles
                        type_batiment_map = {'maison': 0, 'appartement': 1, 'immeuble': 2}
                        energie_map = {
                            'Electricite': 0, 'Gaz_naturel': 1, 'Fioul domestique': 2,
                            'Reseau_de_chauffage_urbain': 3, 'Autres': 4
                        }
                        
                        df_prepared['type_batiment'] = df_prepared['type_batiment'].map(type_batiment_map)
                        df_prepared['type_energie_recodee'] = df_prepared['type_energie_recodee'].map(energie_map)
                        
                        # Prédictions
                        predictions_dpe = model_classif.predict(df_prepared)
                        predictions_cout = model_regress.predict(df_prepared)
                        
                        # Ajouter les prédictions au dataframe original
                        df_batch['etiquette_dpe_predite'] = predictions_dpe
                        df_batch['cout_total_predit'] = predictions_cout.round(0)
                        
                        st.markdown("---")
                        st.markdown("### Résultats des prédictions")
                        
                        # Statistiques
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            st.metric(" Total logements", len(df_batch))
                        with col2:
                            cout_moyen = df_batch['cout_total_predit'].mean()
                            st.metric(" Coût moyen", f"{cout_moyen:,.0f} €")
                        with col3:
                            etiquette_mode = df_batch['etiquette_dpe_predite'].mode()[0]
                            st.metric(" Étiquette la plus fréquente", etiquette_mode)
                        with col4:
                            pct_bonnes = (df_batch['etiquette_dpe_predite'].isin(['A', 'B', 'C']).sum() / len(df_batch)) * 100
                            st.metric(" Bonnes classes (A-C)", f"{pct_bonnes:.1f}%")
                        
                        # Graphiques
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            etiq_counts = df_batch['etiquette_dpe_predite'].value_counts().sort_index()
                            colors_dpe = {
                                'A': '#00A550', 'B': '#52B153', 'C': '#C3D545',
                                'D': '#FFF033', 'E': '#F39200', 'F': '#ED2124', 'G': '#CC0033'
                            }
                            
                            fig_distrib = go.Figure(data=[
                                go.Bar(
                                    x=etiq_counts.index,
                                    y=etiq_counts.values,
                                    marker_color=[colors_dpe.get(x, '#666') for x in etiq_counts.index],
                                    text=etiq_counts.values,
                                    textposition='outside'
                                )
                            ])
                            
                            fig_distrib.update_layout(
                                title="Distribution des étiquettes DPE",
                                xaxis_title="Étiquette",
                                yaxis_title="Nombre",
                                height=350
                            )
                            
                            st.plotly_chart(fig_distrib, use_container_width=True)
                        
                        with col2:
                            fig_cout = px.histogram(
                                df_batch,
                                x='cout_total_predit',
                                nbins=30,
                                labels={'cout_total_predit': 'Coût prédit (€)'},
                                color_discrete_sequence=['#2E7D32']
                            )
                            
                            fig_cout.update_layout(
                                title="Distribution des coûts prédits",
                                height=350,
                                showlegend=False
                            )
                            
                            st.plotly_chart(fig_cout, use_container_width=True)
                        
                        # Afficher le tableau complet
                        st.markdown("#### Tableau des résultats")
                        st.dataframe(df_batch, use_container_width=True, height=400)
                        
                        # Export
                        csv_results = df_batch.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label=" Télécharger les résultats (CSV)",
                            data=csv_results,
                            file_name="predictions_resultats.csv",
                            mime="text/csv",
                            type="primary"
                        )
            
            except Exception as e:
                st.error(f"Erreur lors du traitement du fichier : {e}")
                import traceback
                st.code(traceback.format_exc())

if __name__ == "__main__":
    show()