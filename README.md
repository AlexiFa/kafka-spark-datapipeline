# kafka-spark-datapipeline

From relational to non-relational database project at EFREI Paris

## Usage

Clone the repo

```bash
git clone https://github.com/AlexiFa/kafka-spark-datapipeline.git
cd kafka-spark-datapipeline
```

Start zookeeper and kafka server

```bash
docker compose up -d
```

Create a topic in kafka

```bash
docker exec -it my_kafkaserver /opt/kafka/bin/kafka-topics.sh --create --topic new --bootstrap-server localhost:9092
```
<!-- 
Create table in the database

```bash
docker exec -it my_postgres psql -h localhost -U myuser -d mydatabase -c "
CREATE TABLE transactions (
  transaction_id VARCHAR PRIMARY KEY,
  amount FLOAT,
  timestamp TIMESTAMPTZ
);"
``` -->

Run the consumer

```bash
python src/consumer.py
```

Run the producer

```bash
python src/producer.py
```
