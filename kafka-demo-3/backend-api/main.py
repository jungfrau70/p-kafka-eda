import asyncio
import json
import time
import websockets

from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from typing import Union
from uuid import uuid4
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from schema import REQUEST, RESPONSE
from config import KAFKA_TOPIC_REQUEST, KAFKA_TOPIC_RESPONSE, KAFKA_CONSUMER_GROUP, KAFKA_BOOTSTRAP_SERVERS

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.post("/cmds/{cmd_id}")
async def requester(cmd_id: int, req: REQUEST):
    request_id = str(uuid4())
    req.request_id = request_id
    msg = json.dumps(req.__dict__).encode('utf-8')

    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        transactional_id=request_id)
    await producer.start()
    try:
        async with producer.transaction():
            res = await producer.send_and_wait(KAFKA_TOPIC_REQUEST, msg, partition=1)
            # print(request_id, res)
    except Exception as ex:
        print("Exception happened :",ex)            
    finally:     
        await producer.stop()
        ret = await asyncio.create_task(consume(request_id))

async def consume(request_id: str):
    print(request_id)    
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC_RESPONSE, 
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, 
        group_id=KAFKA_CONSUMER_GROUP,
        auto_offset_reset="latest"
    )
    await consumer.start()
    try:
        async for resp in consumer:
            record = json.loads(resp.value)
            # print(f'Consumer msg: {record}')
            # print(record['request_id'])
            # print(record)
            request_id_received = record['request_id']                    
            try:
                if request_id == request_id_received:
                    print(f'Matched msg: {resp}')
                    return 200            
                else:
                    print(f'Mismatched')   
                    print("request_id: ", request_id)
                    print("request_id_received: ", request_id_received)                                        
            except Exception as ex:
                print("Exception happened :",ex)
            finally:
                await consumer.commit()
                # await consumer.__del__()     
                await consumer.stop()                            
    finally:
        await consumer.commit()
        # await consumer.__del__()             
        await consumer.stop()
        