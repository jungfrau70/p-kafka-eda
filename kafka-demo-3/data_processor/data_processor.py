import configparser
import faust
import json
import subprocess
import uuid

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8') 

REQUEST_TOPIC=config['kafka']['requestTopic']
RESPONSE_TOPIC=config['kafka']['responseTopic']
SERVER=config['kafka']['server'].split(',')
REGION=config['command']['region']
AZ=config['command']['az']
COMMAND=config['command']['command']

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

app = faust.App('agent', 
                broker=SERVER,
                store='memory://',
)

request_topic = app.topic(REQUEST_TOPIC, value_type=REQUEST)
response_topic = app.topic(RESPONSE_TOPIC)


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