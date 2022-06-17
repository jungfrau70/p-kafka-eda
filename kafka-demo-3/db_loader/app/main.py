import logging
import faust
import json
import config_loader as config_loader
import metrics
# from prometheus_client import start_http_server
from db import DB

class Result(faust.Record):
    region: str
    az: str
    uuid: str    
    result: str

SERVICE_NAME = "db-loader"
config = config_loader.Config()

logging.basicConfig(
    level=logging.getLevelName(config.get(config_loader.LOGGING_LEVEL)),
    format=config.get(config_loader.LOGGING_FORMAT))

logger = logging.getLogger(__name__)


app = faust.App(SERVICE_NAME, broker=config.get(config_loader.KAFKA_BROKER),
                web_host=config.get(config_loader.WEB_HOST), web_port=config.get(config_loader.WEB_PORT))
topic = app.topic('order_results', value_type=Result)

db = DB()


# @app.agent(average_changelog_topic)
# async def on_average_event(stream) -> None:
#     async for msg_key, msg_value in stream.items():
#         metrics.AVERAGE_TOPIC_RECEIVED_CNT.inc()
#         logger.info(f'Received new average message {msg_key}, {msg_value}')
#         serialized_message = json.loads(msg_value)
#         await db.save_average(pair_name=msg_key.decode(), value=serialized_message['average'])
#         metrics.AVERAGE_TOPIC_SAVED_CNT.inc()


# @app.agent(processed_data_topic)
# async def on_processed_data_event(stream) -> None:
#     async for msg_key, msg_value in stream.items():
#         # metrics.PROCESSED_DATA_RECEIVED_CNT.inc()
#         logger.info(f'Received new pair message {msg_key}, {msg_value}')
#         serialized_message = json.loads(msg_value)

# Consumer
@app.agent(topic)
async def order_agent(records: faust.Stream):
    async for record in records:
        print(record.region, record.az, record.uuid)
        
        # print(record.result)
        count = 0
        for row in record.result.split('\n'):
            if count <= 2:
                pass
                count += 1
            else:                        
                field = [ col for col in row.split() ]
                if len(field) > 2:
                # row=Record([ col for col in row.split() ])
                    print(f"Record for {field[0]}: {field[2]} {field[8]}")
                    await db.save_currency(pair_name="pair_name", value=100)

        # for pair_name, pair_value in serialized_message.items():
        #     print(pair)
            # await db.save_currency(pair_name=pair_name, value=pair_value)
            # metrics.PROCESSED_DATA_SAVED_CNT.inc()


# @app.task
# async def on_started() -> None:
#     logger.info('Starting prometheus server')
#     start_http_server(port=config.get(config_loader.PROMETHEUS_PORT))
