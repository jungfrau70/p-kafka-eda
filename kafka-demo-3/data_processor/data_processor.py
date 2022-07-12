import configparser
import faust
import json
import subprocess
import uuid
from config import KAFKA_TOPIC_REQUEST, KAFKA_TOPIC_RESPONSE, KAFKA_CONSUMER_GROUP, KAFKA_BOOTSTRAP_SERVERS

class REQUEST(faust.Record):
    request_id: str
    region: str
    az: str
    tennant: str
    command: str

class RESPONSE(faust.Record):
    request_id: str
    region: str
    az: str
    tennant: str    
    result: str

print (KAFKA_BOOTSTRAP_SERVERS)
app = faust.App('agent', 
                broker=KAFKA_BOOTSTRAP_SERVERS,
                store='memory://',
)

request_topic = app.topic(KAFKA_TOPIC_REQUEST, value_type=REQUEST)
response_topic = app.topic(KAFKA_TOPIC_RESPONSE)


# Consumer & Producer
@app.agent(request_topic)
async def agent(requests: faust.Stream):
    async for req in requests:
        print(req.request_id)
        result = RESPONSE(
            request_id = req.request_id,
            region = req.region,
            az = req.az,
            tennant = req.tennant,
            result = subprocess.check_output(req.command, shell=True).decode('utf-8')
            # result = subprocess.check_output('ls -al', shell=True).decode('utf-8')
        )

        print(result)
        await response_topic.send(
            value = result
        )

if __name__ == '__main__':

    # Start the Faust App
    app.main()   