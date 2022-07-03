import time
import json
from uuid import uuid4
from confluent_kafka import Producer

from kafka import KafkaConsumer, KafkaProducer
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

topic='request'
resptopic='response'
mybroker='192.168.54.139:9092,192.168.54.139:9093,192.168.54.139:9094'

producer = KafkaProducer(bootstrap_servers=mybroker)
# consumer = KafkaConsumer(resptopic, bootstrap_servers=mybroker)

class REQUEST(BaseModel):
    region: str
    az: str
    uuid: str
    command: str

class RESPONSE(BaseModel):
    region: str
    az: str
    uuid: str    
    result: str

app = FastAPI()

@app.post("/cmds/{cmd_id}")
def requester(cmd_id: int, req: REQUEST):
    request_id = str(uuid4())
    req.uuid = request_id
    msg = json.dumps(req.__dict__).encode('ascii')

    try:
        producer.send(topic, msg)
        # print(req.uuid)
    except Exception as ex:
        print("Exception happened :",ex)

    # while True:
    #     # StopIteration if no message after 1sec
    consumer = KafkaConsumer(resptopic, bootstrap_servers=mybroker, consumer_timeout_ms=10000)
    # consumer = KafkaConsumer(resptopic, bootstrap_servers=mybroker)
    for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
    # for message in consumer:
    #     print(message.uuid)
    #     request_id_received = message.uuid
    #     print(message.uuid)
    #     try:
    #         if request_id == request_id_received:
    #             consumer.close()
    #             print(message)
    #             return message
    #         else:
    #             print(message)                
    #     except Exception as ex:
    #         print("Exception happened :",ex)

