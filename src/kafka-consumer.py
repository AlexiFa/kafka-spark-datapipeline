from kafka import KafkaConsumer

consumer = KafkaConsumer('new', bootstrap_servers='localhost:9092')

for message in consumer:
    key = message.key.decode() if message.key else None
    value = message.value.decode()
    print(f'Consumed message: {key} {value}')