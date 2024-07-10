from kafka import KafkaConsumer
import json
import pandas as pd
from sqlalchemy import create_engine

table_name = 'trafic'
# Configurer le consommateur Kafka
consumer = KafkaConsumer(
    'new',
    bootstrap_servers=['localhost:9092'],
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Configurer la connexion à PostgreSQL
engine = create_engine('postgresql://myuser:mypassword@localhost:5432/mydatabase')

# Traiter les messages et les écrire dans PostgreSQL
for message in consumer:
    # Convertir le message en DataFrame Pandas
    df = pd.DataFrame([message.value])

    print(df.head())
    
    # Nettoyage des données
    # Supprimer les colonnes non intéressantes
    columns_to_keep = ['Station', 'Trafic', 'Réseau', 'Ville', 'Arrondissement pour Paris']
    df = df[columns_to_keep]
    
    # Suppression des lignes avec des valeurs manquantes dans les colonnes importantes
    df.dropna(subset=['Station', 'Trafic'], inplace=True)
    
    # Écrire dans PostgreSQL
    df.to_sql(table_name, engine, if_exists='append', index=False)
    
    print(f"Processed and wrote message: {message.value}")