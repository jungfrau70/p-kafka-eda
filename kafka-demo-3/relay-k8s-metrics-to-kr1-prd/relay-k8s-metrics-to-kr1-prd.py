
from kafka import KafkaConsumer, KafkaProducer
import json 

KR1_PRD_TOPIC = "k8s-metrics"
KR1_STG_TOPIC = "k8s-metrics"

kr1_prd_brokers = ['10.11.65.187:9092','10.11.65.187:9093','10.11.65.187:9094']
kr1_stg_brokers = ['10.11.76.177:9092','10.11.76.177:9093','10.11.76.177:9094']

consumer = KafkaConsumer(KR1_STG_TOPIC, bootstrap_servers=kr1_stg_brokers)
producer = KafkaProducer(bootstrap_servers=kr1_prd_brokers)

for message in consumer:
  msg = json.loads(message.value.decode())
  producer.send(KR1_PRD_TOPIC, json.dumps(msg).encode("utf-8"))