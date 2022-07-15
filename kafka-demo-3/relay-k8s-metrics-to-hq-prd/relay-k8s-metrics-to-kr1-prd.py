
from kafka import KafkaConsumer, KafkaProducer
import json 

HQ_TOPIC = "kr-1-stg-k8s-metrics"
KR1_STG_TOPIC = "kr-1-stg-k8s-metrics"

# HQ_brokers = ['192.168.171.132:9092','192.168.171.132:9093','192.168.171.132:9094'] # office
# kr1_stg_brokers = ['192.168.171.132:9092','192.168.171.132:9093','192.168.171.132:9094'] # office

HQ_brokers = ['10.11.65.187:9092','10.11.65.187:9093','10.11.65.187:9094'] # private cloud
kr1_stg_brokers = ['10.11.76.177:9092','10.11.76.177:9093','10.11.76.177:9094'] # private cloud

consumer = KafkaConsumer(KR1_STG_TOPIC, bootstrap_servers=kr1_stg_brokers)
producer = KafkaProducer(bootstrap_servers=HQ_brokers)

for message in consumer:
  producer.send(HQ_TOPIC, message.value)  

  # msg = json.loads(message.value.decode())
  # producer.send(KR1_PRD_TOPIC, json.dumps(msg).encode("utf-8"))
