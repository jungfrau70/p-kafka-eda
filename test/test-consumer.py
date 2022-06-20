
from kafka import KafkaConsumer 

brokers = ["10.11.76.177:9092", "10.11.76.177:9093", "10.11.76.177:9094"]

# consumer works like a python generator
consumer = KafkaConsumer("telegraf-kr1-metric", bootstrap_servers=brokers) 

for message in consumer:
  print(message)
