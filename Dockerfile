FROM apache/kafka

CMD sleep 5;/opt/kafka/bin/kafka-topics.sh --create --topic my_topic --bootstrap-server localhost:9092