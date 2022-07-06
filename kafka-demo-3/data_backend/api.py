import asyncio
import json
import time
import websockets

from fastapi import FastAPI
from kafka import KafkaConsumer, KafkaProducer
from pydantic import BaseModel
from typing import Union
from uuid import uuid4
from aiokafka import AIOKafkaProducer

topic='request'
resptopic='response'
mybroker='192.168.54.139:9092,192.168.54.139:9093,192.168.54.139:9094'

# producer = KafkaProducer(bootstrap_servers=mybroker)
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
async def requester(cmd_id: int, req: REQUEST):
    request_id = str(uuid4())
    req.uuid = request_id
    msg = json.dumps(req.__dict__).encode('utf-8')

    producer = AIOKafkaProducer(
        bootstrap_servers=mybroker,
        transactional_id=request_id)
    await producer.start()
    try:
        async with producer.transaction():
            res = await producer.send_and_wait(topic, msg)
            print(request_id, res)
    except Exception as ex:
        print("Exception happened :",ex)            
    finally:
        await producer.stop()