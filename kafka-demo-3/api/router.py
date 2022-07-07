import asyncio
import json
import time

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from fastapi import APIRouter
from schema import REQUEST, RESPONSE
from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC_REQUEST, KAFKA_TOPIC_RESPONSE
from uuid import uuid4
from fastapi import FastAPI

# route = APIRouter()
# route = FastAPI()
# producer = AIOKafkaProducer(loop=loop,bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

# @app.post("/cmds/{cmd_id}")
# async def requester(cmd_id: int, req: REQUEST):
#     request_id = str(uuid4())
#     req.request_id = request_id
#     msg = json.dumps(req.__dict__).encode('utf-8')

#     producer = AIOKafkaProducer(
#         bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
#         transactional_id=request_id)
#     await producer.start()
#     try:
#         async with producer.transaction():
#             res = await producer.send_and_wait(KAFKA_TOPIC_REQUEST, msg)
#             print(request_id, res)
#     except Exception as ex:
#         print("Exception happened :",ex)            
#     finally:
#         await producer.stop()
#         ret = asyncio.create_task(consume(request_id))
#         print (type(ret))        


# @route.post("/cmds/{cmd_id}")
# async def produce(cmd_id: int, req: REQUEST):
    
#     await producer.start()
#     # await produce(loop)

#     request_id = str(uuid4())
    # await producer.send(req, str.encode(json.dumps(request_id)))    
    # asyncio.create_task(consume(request_id))

    # try:
    #     req.request_id = request_id
    #     try:
    #         print(request_id)
    #         value_json = json.dumps(req.__dict__).encode('utf-8')
    #         print(f'Sending message with request: {value_json}')
    #         # loop.run_until_complete(produce(loop, req))
    #         await producer.send_and_wait(KAFKA_TOPIC_REQUEST, value=value_json)
    #         await producer.stop()
    #         return request_id
    #     except Exception as ex:
    #         print("Exception happened :",ex)    
    # finally:
    #     await producer.stop()

        # ret = asyncio.create_task(consume(request_id))
        # print (type(ret))

# async def consume(reqeust_id: str):
#     consumer = AIOKafkaConsumer(KAFKA_TOPIC_RESPONSE, loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS) #, group_id=KAFKA_CONSUMER_GROUP)
#     await consumer.start()

#     try:
#         async for resp in consumer:
#             record = json.loads(resp.value)
#             # print(f'Consumer msg: {record}')
#             # print(record['request_id'])
#             request_id_received = record['request_id']
#             try:
#                 if reqeust_id == request_id_received:
#                     print(f'Matched msg: {resp}')
#                     await consumer.stop()
#                     return 200
#                 else:
#                     print(f'Mismatched')   
#             except Exception as ex:
#                 print("Exception happened :",ex)                      
#     finally:
#         await consumer.stop()
