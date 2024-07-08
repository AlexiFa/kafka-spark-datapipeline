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
sudo docker compose up -d
```

Create a topic in kafka

```bash
sudo docker exec -it my_kafkaserver /opt/kafka/bin/kafka-topics.sh --create --topic new --bootstrap-server localhost:9092
```
