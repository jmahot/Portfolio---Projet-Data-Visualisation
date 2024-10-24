import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px
import folium
from folium import Marker
import matplotlib.pyplot as plt

st.set_page_config(
        layout="wide"
)

with st.sidebar:
    selected = option_menu("Menu", ["Portfolio", 'Project DataViz : Parcoursup'], 
        icons=['person', 'search'], menu_icon="house", default_index=0)
    st.sidebar.markdown("<h2 style='text-align: center;'>Julie MAHOT</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center;'>Student in <strong>M1 Data Engineering</strong> at EFREI</p>", unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns((1,3,1))
    with cent_co:
        st.image("logoefrei.png", width=150)

    st.sidebar.write("---")
    st.sidebar.subheader("My contact :")
    st.sidebar.markdown("""
        <div style="display: flex; flex-direction: column; align-items: left;">
            <a href="https://github.com/jmahot" target="_blank" style="margin-bottom: 10px;">
                <img src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="width: 110px; height: 35px; color:black; border:solid; border-radius:10px;">
            </a>
            <a href="https://www.linkedin.com/in/julie-mahot/" target="_blank" style="margin-bottom: 10px;">
                <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" style="width: 110px; height: 35px; color:black; border:solid; border-radius:10px;">
            </a>
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <a href="mailto:julie.mahot@gmx.fr">
                    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" style="width: 110px; height: 35px; color:black; border:solid; border-radius:10px; margin-right:10px">
                </a>
                <span style="font-size: 15px; color: black;">julie.mahot@gmx.fr</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div style="text-align: center; margin-top: 50px; font-size: 12px; color: gray;">
            <hr style="margin-top: 50px; border: 1px solid gray;">
            &copy; 2024 Julie Mahot. Tous droits réservés.
        </div>
        """, unsafe_allow_html=True)


if selected == "Portfolio":
    st.title("Welcome to my Portfolio about Data Science ! 👋")
    # Introduction
    st.write("## About me :")
    with st.container():
        col1,col2 = st.columns((1,6))
        with col1:
            st.image("Photo de profil - MAHOT_Julie.png", width=150)
        with col2:
            st.write("My name is **Julie MAHOT**. I'm a french student in M1 Data Engineering at the engineering school **EFREI Paris** Pathéon-Assas.")
            st.write("I'm passionate about Data Science, innovations about science and technology, and I love learning ! 💻🎓")

            st.write("#### My major assets :")
            st.write("- Experience of complex data analysis projects \n- Analytical mind, sense of creativity and rigour \n- Ability to transform raw data into relevant information 🔎📊")

    st.write("---")

    # CV button download
    with open("CV Julie Mahot 2024.pdf", "rb") as file:
        cv_pdf = file.read()
    st.download_button(
        label="Download my CV",
        data=cv_pdf,
        file_name="CV Julie Mahot 2024.pdf",
        mime="application/pdf"
    )

    st.write("---")

    # Compétences
    st.write("## My technical competences :")
    with st.container():
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            # Langages de programmation
            st.write("**Programming languages :**")
            st.write("- Python, C, Java, Bash Linux")
            st.write("- SQL, UML")
            st.write("- HTML, CSS, JS, React.js")

        with col2:
            # Librairies Data Science (Python)
            st.write("**Data Science Librairies (Python) :**")
            st.write("- Selenium, BeatifulSoup, Scrapy")
            st.write("- Pandas, Numpy, Scikit-Learn, Matplotlib, Seaborn, Plotly")
            st.write("- Folium, GeoPandas")
            st.write("- PySpark, Apache Kafka, Hadoop, Docker")

        with col3:
            # Outils & Logiciels
            st.write("**Tools & Software :**")
            st.write("- Streamlit \n- Matlab\n- MySQL\n- Github\n- Figma\n- Power Query Excel\n- Power BI\n- Jupyter Notebook\n- Microsoft Azure\n- Microsoft Office")

        with col4:
            # Algorithmes d'Analyse de données ML
            st.write("**Algorithms ML Data Analysis :**")
            st.write("- Logistic Regression\n- KNN\n- K-Means\n- RandomForest\n- Decision Trees")

    st.write("---")

    # My projects
    st.write("## My projects :")

    st.write("#### 📌 Project : Tableau de Répartition des Bandes de Fréquences")
    st.write("""
            |  🗂️ **Réponse à un appel d’offre avec les données de l’ANFR**
            |  📅 **Juin-Juillet 2024**
            |  ⚙️ **Équipe de 5 élèves**
        """)
    st.write("Développement d'un site interactif avec Streamlit pour visualiser l'occupation des bandes de fréquences en France.")
    st.write("""
        - **Préparation des données** 
        - **Analyse exploratoire des données (EDA)**  
        - **Création de frises interactives** pour la visualisation du spectre d’occupation par bande de fréquence, affectataires, année, etc.  
        - **Réalisation de cartes interactives** avec des filtres intégrés pour afficher l’occupation du spectre selon leurs coordonnées GPS  
        - **Identification des zones de tension spectrale** pour les JO Paris 2024
        """)

    st.write("#### 📌 Project : Analyse de données immobilières ")
    st.write("""
            |🗂️ **Avec les données DVF provenant du data.gouv.fr**
            |📅 **Juin 2024 (1 semaine)**
            |⚙️ **Équipe de 4 élèves**
        """)
    st.write("""
        - **Préparation des données :**  
            - Nettoyage, transformation et prétraitement des données pour l'analyse.
        - **Analyse exploratoire des données (EDA) :**  
            - Identification de la variable cible  
            - Utilisation de visualisations statistiques (histogrammes, scatter plots) pour examiner les distributions et corrélations  
            - Étude des tendances de prix par département avec des cartes créées en GeoPandas
        - **Modélisation machine learning (ML) :**  
            - Application de techniques de clustering pour segmenter les données  
            - Développement d'un modèle prédictif des prix en utilisant des algorithmes de régression
        """)

    st.write("#### 📌 Project : Advanced Web Programming")
    st.write("""
            |🗂️ **Projet réalisé à AGH University of Krakow**
            |📅 **Novembre 2023 - Décembre 2023**
            |⚙️ **Équipe de 3 élèves**
        """)
    st.write("""
        - **Projet e-commerce d'artbooks** : Développement d'un site avec un front-end interactif et un back-end sur serveur MySQL.
        - **Gestion des rôles** : Trois types de rôles (invités, utilisateurs, administrateurs) avec des permissions spécifiques.
        - **Panneau d'administration** : Gestion des produits et des utilisateurs avec des options d'ajout, d'édition et de suppression.
        """)


    st.write("---")


    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("My contact :")
            st.markdown("""
            <div style="display: flex; flex-direction: column; align-items: left;">
                <a href="https://github.com/jmahot" target="_blank" style="margin-bottom: 10px;">
                    <img src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="width: 110px; height: 35px; color:black; border:solid; border-radius:10px;">
                </a>
                <a href="https://www.linkedin.com/in/julie-mahot/" target="_blank" style="margin-bottom: 10px;">
                    <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" style="width: 110px; height: 35px; color:black; border:solid; border-radius:10px;">
                </a>
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <a href="mailto:julie.mahot@gmx.fr">
                        <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" style="width: 110px; height: 35px; color:black; border:solid; border-radius:10px; margin-right:10px">
                    </a>
                    <span style="font-size: 15px; color: black;">julie.mahot@gmx.fr</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.subheader("📨 Contact Me")
            contact_form = """
            <form action="https://formsubmit.co/74044b4d95a0af6cc3c065ab2fbf78fd" method="POST" style="display: flex; flex-direction: column; gap: 10px;">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required style="padding: 8px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;">
                <input type="email" name="email" placeholder="Your email" required style="padding: 8px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;">
                <textarea name="message" placeholder="Your message here" required style="padding: 8px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc; height: 100px;"></textarea>
                <button type="submit" style="padding: 10px 15px; font-size: 16px; color: white; background-color: #c9868c; border: none; border-radius: 5px; cursor: pointer;">Send</button>
            </form>
            <style>
                form {
                    max-width: 400px;
                }
            </style>
            """
            
            st.markdown(contact_form, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-size: 12px; color: gray;">
        <hr style="margin-top: 100px; border: 1px solid gray;">
        &copy; 2024 Julie Mahot. Tous droits réservés.
    </div>
    """, unsafe_allow_html=True)

if selected == "Project DataViz : Parcoursup":
    # dataset
    @st.cache_data
    def load_data():
        data = pd.read_csv('fr-esr-parcoursup_2020.csv', sep=';')
        return data
    df = load_data()
    
    with st.container():
        st.markdown('<div class="center">', unsafe_allow_html=True)
        st.title("Dashboard Parcoursup 2020 - Data Visualization")
        st.markdown("""
            <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                width: 100%;  /* Aucune limite de largeur ici */
            }
            .container {
                max-width: 800px;  /* Ajuster cette valeur selon la largeur souhaitée */
                margin: 0 auto;  /* Centre le conteneur */
            }
            </style>
            """, unsafe_allow_html=True)

        st.markdown("""
        # Projet de Data Visualisation

        J'ai réalisé ce projet dans le cadre du cursus **Master 1 en Data Engineering** à **EFREI Paris**. 
        Il a été conçu pour le cours de **Data Visualisation** dispensé par **Monsieur Mano Joseph MATHEW, Enseignant-chercheur de la majeure "Data and Artificial Intelligence", Responsable de la majeure "Bio-Informatics" ainsi que Responsable du Département de Biologie à Efrei Paris**. 
        L'objectif principal de ce projet est d'explorer et de visualiser des données de manière interactive, 
        permettant ainsi une meilleure compréhension des tendances et des insights. 
        Merci de votre attention et bonne exploration !
        """)
        st.write("**Nom du Dataset** : 'Parcoursup 2020 - vœux de poursuite d'études et de réorientation dans l'enseignement supérieur et réponses des établissements'")
        st.write("Voici un aperçu du tableau de données :")
        st.write(df)


        st.header("📊 Satistiques Globales :")
        # Sous-section : Nombre de candidats par filière
        st.subheader("Visualisation du Nombre de candidats par filière")
        candidats_par_filiere = df.groupby('Filière de formation')['Effectif total des candidats en phase principale'].sum().reset_index()
        fig1 = px.pie(candidats_par_filiere, 
                    names='Filière de formation', 
                    values='Effectif total des candidats en phase principale', 
                    title='Répartition des Candidats par Filière')
        st.plotly_chart(fig1)

        fig = px.line_polar(candidats_par_filiere, r=candidats_par_filiere['Effectif total des candidats en phase principale'], theta=candidats_par_filiere['Filière de formation'], line_close=True, title='Radar Chart')
        st.plotly_chart(fig)

        fig = px.line(df, x=candidats_par_filiere['Effectif total des candidats en phase principale'], y=candidats_par_filiere['Filière de formation'], title='Time Series Plot')
        st.plotly_chart(fig)

        st.subheader("Diagramme en barre : Nombre de candidats par filière")
        df_grouped = df.groupby('Filière de formation')['Effectif total des candidats en phase principale'].sum().reset_index()
        top_10_filieres = df_grouped.nlargest(10, 'Effectif total des candidats en phase principale')
        plt.figure(figsize=(12, 6))
        plt.bar(top_10_filieres['Filière de formation'], top_10_filieres['Effectif total des candidats en phase principale'], color='skyblue')
        plt.title('Nombre de candidats par filière (Top 10)')
        plt.xlabel('Filière')
        plt.ylabel('Nombre de candidats en phase principale')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(plt)

        st.subheader("Mention au Bac des candidats admis par filière")
        mentions_bac = df.groupby('Filière de formation')[[
            '% d’admis néo bacheliers sans information sur la mention au bac',
            '% d’admis néo bacheliers sans mention au bac',
            '% d’admis néo bacheliers avec mention Assez Bien au bac',
            '% d’admis néo bacheliers avec mention Bien au bac',
            '% d’admis néo bacheliers avec mention Très Bien au bac'
        ]].mean().reset_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        mentions_bac.set_index('Filière de formation').plot(kind='bar', stacked=True, ax=ax, color=['lightgray', 'orange', 'lightblue', 'green', 'darkblue'])
        ax.set_title('Répartition des Mentions au Bac par Filière')
        ax.set_xlabel('Filière de formation')
        ax.set_ylabel('Pourcentage d\'Admis')
        ax.legend(title='Mention', bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)

        # Sous-section : Statistiques géographiques
        st.subheader("🗺️📍 Répartition des mentions au bac à Paris")

        # Répartition des mentions au bac à Paris
        paris_data = df[df['Département de l’établissement'] == 'Paris']
        mention_counts = {
            'Sans mention': paris_data['% d’admis néo bacheliers sans mention au bac'].sum(),
            'Mention Assez Bien': paris_data['% d’admis néo bacheliers avec mention Assez Bien au bac'].sum(),
            'Mention Bien': paris_data['% d’admis néo bacheliers avec mention Bien au bac'].sum(),
            'Mention Très Bien': paris_data['% d’admis néo bacheliers avec mention Très Bien au bac'].sum(),
        }
        mentions_df = pd.DataFrame(list(mention_counts.items()), columns=['Mention', 'Effectif'])
        # Visualisation
        fig, ax = plt.subplots(figsize=(8, 5))  # Taille du graphique
        ax.bar(mentions_df['Mention'], mentions_df['Effectif'], color=['#FF6347', '#FFD700', '#4CAF50', '#00BFFF'])
        ax.set_ylabel('Effectif des admis néo bacheliers')
        ax.set_title('Répartition des mentions au bac')
        ax.set_xticklabels(mentions_df['Mention'], rotation=15)
        st.pyplot(fig)

        # Section Statistiques Établissements
        st.header("🏫 Statistiques par Établissement")

        st.subheader("Filtres")
        # Filtre par filière
        filiere_options = df["Filière de formation"].unique()
        selected_filieres = st.multiselect("Choisissez les filières :", options=filiere_options)

        # Filtre par statut
        statut_options = df["Statut de l’établissement de la filière de formation (public, privé…)"].unique()
        selected_statuts = st.multiselect("Choisissez le statut :", options=statut_options)

        # Filtre par académie
        academie_options = df["Académie de l’établissement"].unique()
        selected_academies = st.multiselect("Choisissez l'académie :", options=academie_options)

        # Bouton pour réinitialiser les filtres
        if st.button("Réinitialiser tous les filtres"):
            selected_filieres = []
            selected_statuts = []
            selected_academies = []

        # Filtrage du DataFrame selon les sélections
        filtered_df = df[
            (df["Filière de formation"].isin(selected_filieres) | (len(selected_filieres) == 0)) &
            (df["Statut de l’établissement de la filière de formation (public, privé…)"].isin(selected_statuts) | (len(selected_statuts) == 0)) &
            (df["Académie de l’établissement"].isin(selected_academies) | (len(selected_academies) == 0))
        ]


        st.write("Données filtrées :", filtered_df)

        # Carte mondiale des établissements (pour une visualisation géographique)
        st.subheader("🌍 Carte mondiale des établissements")

        st.write("#### Localisation des établissements")
        st.write(f"Nombre total d'établissements : {len(df)}")
        filtered_df[['Latitude', 'Longitude']] = filtered_df['Coordonnées GPS de la formation'].str.split(',', expand=True).astype(float)
        df_gps = filtered_df.dropna(subset=['Latitude', 'Longitude'])
        @st.cache_data
        def create_map(data):
            m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=6)
            
            for _, row in data.iterrows():
                popup_content = f"""
                <strong>Nom de l'établissement :</strong> {row["Établissement"]}<br>
                <strong>Filière :</strong> {row['Filière de formation']}<br>
                <strong>Statut :</strong> {row['Statut de l’établissement de la filière de formation (public, privé…)']}<br>
                <strong>Académie :</strong> {row['Académie de l’établissement']}<br>
                <strong>Nombre de candidats :</strong> {row['Effectif total des candidats en phase principale']}<br>
                <strong>Taux d'accès (bac général) :</strong> {row['Dont taux d’accès des candidats ayant un bac général ayant postulé à la formation']}%<br>
                <strong>Taux d'accès (bac techno) :</strong> {row['Dont taux d’accès des candidats ayant un bac technologique ayant postulé à la formation']}%
                """
                
                # Ajouter le marqueur avec le popup
                Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=folium.Popup(popup_content, max_width=300),
                    icon=folium.Icon(color='blue')
                ).add_to(m)
            
            return m
        map_data = create_map(df_gps)

        st.components.v1.html(map_data._repr_html_(), height=1000)

        # Dashboard par établissement sélectionné
        st.subheader("📈 Dashboard pour l'établissement sélectionné :")

        establishment = st.selectbox("Sélectionner un établissement", df['Établissement'].unique())

        etab_choisi = df[df['Établissement'] == establishment]

        # Étape 1 : Nombre de candidats ayant fait une confirmation de voeux
        st.write(f"Nombre de candidats ayant fait une confirmation de voeux : {int(etab_choisi['Effectif total des candidats pour une formation'].mean())}")

        # Étape 2 : Nombre de candidats ayant reçu une proposition d'admission
        st.write(f"Nombre de candidats ayant reçu une proposition d'admission : {int(etab_choisi['Effectif total des candidats ayant reçu une proposition d’admission de la part de l’établissement'].mean())}")
        st.write(f"Rang du dernier candidat appelé : {int(etab_choisi['Effectif total des candidats ayant accepté la proposition de l’établissement (admis)'].mean())}")

        # Étape 3 : Nombre de candidats ayant accepté une proposition d'admission
        st.write(f"Nombre de candidats ayant accepté une proposition d'admission : {int(etab_choisi['Effectif total des candidats ayant accepté la proposition de l’établissement (admis)'].mean())}")
        # Afficher les pourcentages
        effectifs_phase_principale = int(etab_choisi['Effectif total des candidats en phase principale'].mean())
        effectifs_phase_complementaire = int(etab_choisi['Effectif total des candidats en phase complémentaire'].mean())
        st.write(f"% en phase principale : {100 * (effectifs_phase_principale / (effectifs_phase_principale + effectifs_phase_complementaire)):.2f}%")
        st.write(f"% en phase complémentaire : {100 * (effectifs_phase_complementaire / (effectifs_phase_principale + effectifs_phase_complementaire)):.2f}%")

        
        # Calcul des valeurs pour le diagramme
        confirmation_voeux = int(etab_choisi['Effectif total des candidats pour une formation'].mean())
        proposition_admission = int(etab_choisi['Effectif total des candidats ayant reçu une proposition d’admission de la part de l’établissement'].mean())
        acceptation_admission = int(etab_choisi['Effectif total des candidats ayant accepté la proposition de l’établissement (admis)'].mean())

        effectifs_phase_principale = int(etab_choisi['Effectif total des candidats en phase principale'].mean())
        effectifs_phase_complementaire = int(etab_choisi['Effectif total des candidats en phase complémentaire'].mean())

        # Préparation des données pour le diagramme
        categories = [
            'Confirmation de voeux',
            'Proposition d\'admission',
            'Acceptation d\'admission',
            'Phase principale',
            'Phase complémentaire'
        ]

        values = [
            confirmation_voeux,
            proposition_admission,
            acceptation_admission,
            effectifs_phase_principale,
            effectifs_phase_complementaire
        ]
        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color=['blue', 'orange', 'green', 'red', 'purple'])
        plt.title('Statistiques des Candidats')
        plt.xlabel('Catégories')
        plt.ylabel('Nombre de Candidats')
        plt.xticks(rotation=45)
        st.pyplot(plt)
        
        # Autres statistiques
        st.subheader("📊 Autres statistiques de l'établissement sélectionné")

        col1, col2 = st.columns(2)

        with col1:
            series = ['Bac Général', 'Bac Technologique']
            effectifs = [etab_choisi['Effectif des candidats néo bacheliers généraux en phase principale'].mean(),
                        etab_choisi['Effectif des candidats néo bacheliers technologiques en phase principale'].mean()]

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(series, effectifs, color=['skyblue', 'lightgreen'])
            ax.set_title('Répartition des néo-bacheliers par série')
            ax.set_xlabel('Séries de Bac')
            ax.set_ylabel('Effectif')
            st.pyplot(fig)
                        
        with col2:
            effectifs = {
                "Sans information": etab_choisi['Dont effectif des admis néo bacheliers sans information sur la mention au bac'].mean(),
                "Sans mention": etab_choisi['Dont effectif des admis néo bacheliers sans mention au bac'].mean(),
                "Mention Assez Bien": etab_choisi['Dont effectif des admis néo bacheliers avec mention Assez Bien au bac'].mean(),
                "Mention Bien": etab_choisi['Dont effectif des admis néo bacheliers avec mention Bien au bac'].mean(),
                "Mention Très Bien": etab_choisi['Dont effectif des admis néo bacheliers avec mention Très Bien au bac'].mean()
            }
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(effectifs.keys(), effectifs.values(), color='lightblue')
            ax.set_title('Répartition des Mentions au Bac des Néo-bacheliers Admis')
            ax.set_ylabel('Effectif')
            ax.set_xlabel('Mention au Bac')
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(fig)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 50px; font-size: 12px; color: gray;">
            <hr style="margin-top: 100px; border: 1px solid gray;">
            &copy; 2024 Julie Mahot. Tous droits réservés.
        </div>
        """, unsafe_allow_html=True)