from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

messages = [('key3', 'value3'), ('key4', 'value4')]

for key, value in messages:
    producer.send('new', key=key.encode(), value=value.encode())
producer.flush()
producer.close()
print('All messages sent.')