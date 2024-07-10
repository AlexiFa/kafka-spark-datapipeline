from kafka import KafkaProducer
import json
import csv
import chardet

csv_file_path = 'data/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.csv'

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open(csv_file_path, 'rb') as file:
    result = chardet.detect(file.read()) 
    encodings = result['encoding']

with open(csv_file_path, 'r', encoding=encodings) as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        producer.send('new', value=row)

producer.flush()
producer.close()
