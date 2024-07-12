# kafka-pandas-datapipeline

From relational to non-relational database project at EFREI Paris.

Pipeline that takes data from a csv file, send it through a kafka topic, process it with pandas and then store it in a postgres database.

## Usage

Clone the repo

```bash
git clone https://github.com/AlexiFa/kafka-spark-datapipeline.git
cd kafka-spark-datapipeline
```
### On windows

Open powershell and run

```bash
.\stript.ps1
```

### On other

Start zookeeper and kafka server

```bash
docker compose up -d
```

Create a topic in kafka

```bash
docker exec -it my_kafkaserver /opt/kafka/bin/kafka-topics.sh --create --topic new --bootstrap-server localhost:9092
```

Run the consumer

```bash
python src/consumer.py
```

Run the producer

```bash
python src/producer.py
```

in the postgres container

```bash
psql -h localhost -U myuser -d mydatabase
```

then to see the data stored

```sql
select * from trafic;
```

## Monitoring

Run in your terminal

```bash
streamlit run .\trafic_dashboard.py
```

You will see the data with some graphs on the local port display by the program
