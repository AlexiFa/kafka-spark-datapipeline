from kafka import KafkaConsumer
import json
import pandas as pd
from sqlalchemy import create_engine

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
    
    # Effectuer ici tout traitement nécessaire sur df
    # Par exemple :
    # df['amount'] = df['amount'] * 2
    
    # Écrire dans PostgreSQL
    df.to_sql('transactions', engine, if_exists='append', index=False)
    
    print(f"Processed and wrote message: {message.value}")