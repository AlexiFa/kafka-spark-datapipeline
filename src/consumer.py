from kafka import KafkaConsumer
import json
import pandas as pd
from sqlalchemy import create_engine, text

table_name = 'sanitaire'
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

# with engine.connect() as connection:
#     connection.execute(text(f'CREATE TABLE transactions (transaction_id VARCHAR(50), amount INTEGER, timestamp TIMESTAMP)'))
    # connection.execute(text(f'CREATE TABLE IF NOT EXISTS {table_name} ( \
    #                         ligne VARCHAR(50), \
    #                         station VARCHAR(100), \
    #                         accessible_au_publique VARCHAR(2), \
    #                         tarif VARCHAR(20), \
    #                         access_pass_navigo_ou_ticket_t VARCHAR(2), \
    #                         acces_bouton_poussoir VARCHAR(2), \
    #                         en_zone_controlee VARCHAR(2), \
    #                         hors_zone_controlee_station VARCHAR(2), \
    #                         hors_zone_controlee_voie_publique VARCHAR(2), \
    #                         accessibilite_PMR VARCHAR(2), \
    #                         localisation TEXT, \
    #                         coord_geo VARCHAR(100), \
    #                         gestionnaire VARCHAR(100) \
    #                         )'))
#     connection.execute(text(f"DELETE FROM {table_name}"))
# print(f"Table {table_name} created")
# Traiter les messages et les écrire dans PostgreSQL
for message in consumer:
    # Convertir le message en DataFrame Pandas
    df = pd.DataFrame([message.value])
    
    # Effectuer ici tout traitement nécessaire sur df
    # Par exemple :
    # df['amount'] = df['amount'] * 2
    
    # Écrire dans PostgreSQL
    df.to_sql(table_name, engine, if_exists='append', index=False)
    
    print(f"Processed and wrote message: {message.value}")