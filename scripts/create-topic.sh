#!/bin/sh

# Wait until Kafka is ready
# cub kafka-ready -b localhost:9092 1 20

# Create the Kafka topic
/opt/kafka/bin/kafka-topics.sh --create --topic my_topic --bootstrap-server localhost:9092

# Keep the container running
# exec sleep infinity
