import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Configurer la connexion à PostgreSQL
engine = create_engine('postgresql://myuser:mypassword@localhost:5432/mydatabase')

# Fonction pour charger les données depuis PostgreSQL
def load_data():
    query = "SELECT * FROM trafic ORDER BY \"Station\" LIMIT 1000"
    df = pd.read_sql(query, engine)
    df['Trafic'] = pd.to_numeric(df['Trafic'], errors='coerce')
    return df

# Titre de l'application
st.title('Visualisation des données de trafic')

# Charger les données
data = load_data()

# Afficher les données brutes
st.subheader('Données brutes')
st.dataframe(data)

# Graphique du trafic par station
st.subheader('Trafic par station')
fig = px.bar(data, x='Station', y='Trafic', color='Réseau', title='Trafic par station')
st.plotly_chart(fig)


# # Afficher les 5 stations de RER avec le plus grand trafic
# st.subheader('Top 5 des stations RER par trafic')

# # Filtrer les données pour ne garder que les stations RER
# rer_data = data[data['Réseau'] == 'RER']

# # Trier par trafic décroissant et prendre les 5 premières
# top_5_rer = rer_data.nlargest(5, 'Trafic')

# # Afficher un graphique à barres pour les 5 stations RER les plus fréquentées
# fig_top_rer = px.bar(top_5_rer, x='Station', y='Trafic', 
#                      title='Top 5 des stations RER par trafic',
#                      labels={'Trafic': 'Nombre de passagers', 'Station': 'Nom de la station'})
# st.plotly_chart(fig_top_rer)

# # Afficher les données des 5 stations RER les plus fréquentées
# st.subheader('Détails des 5 stations RER les plus fréquentées')
# st.dataframe(top_5_rer[['Station', 'Trafic', 'Ville', 'Arrondissement pour Paris']])
# Sélecteur pour choisir entre métro et RER
reseau_choisi = st.selectbox('Choisissez le réseau', ['RER', 'Métro'])

# Afficher les 5 stations avec le plus grand trafic pour le réseau choisi
st.subheader(f'Top 5 des stations {reseau_choisi} par trafic')

# Filtrer les données pour ne garder que les stations du réseau choisi
reseau_data = data[data['Réseau'] == reseau_choisi]

# Trier par trafic décroissant et prendre les 5 premières
top_5_stations = reseau_data.nlargest(5, 'Trafic')

# Afficher un graphique à barres pour les 5 stations les plus fréquentées
fig_top_stations = px.bar(top_5_stations, x='Station', y='Trafic', 
                          title=f'Top 5 des stations {reseau_choisi} par trafic',
                          labels={'Trafic': 'Nombre de passagers', 'Station': 'Nom de la station'})
st.plotly_chart(fig_top_stations)

# Afficher les données des 5 stations les plus fréquentées
st.subheader(f'Détails des 5 stations {reseau_choisi} les plus fréquentées')
st.dataframe(top_5_stations[['Station', 'Trafic', 'Ville', 'Arrondissement pour Paris']])