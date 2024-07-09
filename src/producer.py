from kafka import KafkaProducer
import json
import time
import csv

csv_file_path = 'data/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.csv'

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        producer.send('new', value=row)

# transactions = [
#     {"transaction_id": "3", "amount": 100, "timestamp": "2024-07-05 10:00:00"},
#     {"transaction_id": "4", "amount": 150, "timestamp": "2024-07-05 10:01:00"},
#     # Ajoutez plus de transactions ici
# ]

# for transaction in transactions:
#     producer.send('new', value=transaction)
#     time.sleep(1)

producer.flush()
producer.close()
