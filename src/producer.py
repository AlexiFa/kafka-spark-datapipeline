from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transactions = [
    {"transaction_id": "3", "amount": 100, "timestamp": "2024-07-05 10:00:00"},
    {"transaction_id": "4", "amount": 150, "timestamp": "2024-07-05 10:01:00"},
    # Ajoutez plus de transactions ici
]

for transaction in transactions:
    producer.send('new', value=transaction)
    time.sleep(1)

producer.flush()
producer.close()
